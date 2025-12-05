import time
import requests
from typing import Optional, Dict, Any, Iterator, List
import pandas as pd

class GLEIFAPI:
    """
    Minimal client for GLEIF's JSON:API.

    - Reuses a single HTTP session
    - Exponential backoff on transient errors
    - Convenience methods for LEI attributes and ISINs (with pagination)
    - Helper to build summary and long-form DataFrames
    """

    def __init__(
        self,
        base_url: str = "https://api.gleif.org/api/v1",
        accept: str = "application/vnd.api+json",
        timeout: int = 30,
        retries: int = 3,
        backoff: float = 1.5,
    ):
        self.base_url = base_url.rstrip("/")
        self.headers = {"Accept": accept}
        self.timeout = timeout
        self.retries = retries
        self.backoff = backoff
        self.session = requests.Session()

    def _get(self, path_or_url: str, params: Optional[Dict[str, Any]] = None):
        """
        GET with basic retries/backoff. Accepts either a full URL or a path.
        """
        url = (
            path_or_url
            if path_or_url.startswith("http")
            else f"{self.base_url}/{path_or_url.lstrip('/')}"
        )
        for i in range(self.retries):
            resp = self.session.get(
                url, headers=self.headers, params=params, timeout=self.timeout
            )
            if resp.status_code == 200:
                return resp.json()
            else:
                time.sleep(self.backoff ** (i + 1))
                continue
            raise RuntimeError(
                f"GET {url} failed ({resp.status_code}): {resp.text[:300]}"
            )

        return {}

    def fetch_lei_attrs(self, lei: str):
        """
        Return the attributes block for a single LEI record.
        """
        payload = self._get(f"lei-records/{lei}")
        return (payload.get("data") or {}).get("attributes", {}) or {}

    def all_pages(self, query: str, max_pages: Optional[int] = None) -> Iterator[Dict[str, Any]]:
        """
        Paginate through API responses, following 'next' links until exhausted or max_pages is reached.
        """
        url = query
        page_count = 0
        
        while url:
            if max_pages is not None and page_count >= max_pages:
                break
            
            body = self._get(url)
            
            # Handle empty or invalid responses
            if not body or not isinstance(body, dict):
                break
                
            yield body
            
            # Get next page URL from links
            links = body.get("links", {})
            url = links.get("next") if isinstance(links, dict) else None
            page_count += 1


    def fetch_field_modifications(
        self,
        lei: str,
        page_limit: int = 200,
        max_pages: int = 3
    ) -> pd.DataFrame:
        """
        Fetch field-modifications from GLEIF with optional server-side field filtering.
        """
        # Build query URL with pagination parameter (handle existing query params)
        query = f"{self.base_url}/lei-records/{lei}/field-modifications?page[limit]={page_limit}"
        rows: List[Dict[str, Any]] = []

        for page in self.all_pages(query, max_pages=max_pages):
            for it in page.get("data") or []:
                if it.get("type") != "field-modifications":
                    continue

                attrs = it.get("attributes", {})
                full_field = attrs.get("field", "")

                # Pick last part after slash, if exists
                parts = full_field.split("/")

                # keep only EndNode from RR and ignore StartNode
                if any(p.startswith("rr:EndNode") for p in parts):
                    simple_field = parts[-1]
                elif any(p.startswith("rr:StartNode") for p in parts):
                    continue
                else:
                    simple_field = parts[-1]
                    
                rows.append({
                    "Field": simple_field,
                    "Previous value": attrs.get("valueOld"),
                    "New value": attrs.get("valueNew"),
                    "modification_date": attrs.get("date"),
                })

        return pd.DataFrame(rows).drop_duplicates().reset_index(drop=True)
