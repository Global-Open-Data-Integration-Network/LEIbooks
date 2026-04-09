import re
from typing import Any, Iterable, List, Optional
from xml.dom import minidom
import xml.etree.ElementTree as ET
import pandas as pd
from langcodes import Language
from langcodes.tag_parser import LanguageTagError

class TextXml:
    """Small helpers for text cleanup and XML output."""

    @staticmethod
    def clean(value: Any) -> Optional[str]:
        """Return stripped text, or ``None`` for empty/NA-like values."""
        if value is None:
            return None
        try:
            if pd.isna(value):
                return None
        except TypeError:
            pass
        text = str(value).strip()
        if not text:
            return None
        return re.sub(r"\s+", " ", text)

    @staticmethod
    def is_latin_language(language: Optional[str]) -> bool:
        """Check whether a BCP 47 tag resolves to Latin script."""
        language = TextXml.clean(language)
        if not language:
            return False
        try:
            lang = Language.get(language)
            if not lang.is_valid():
                return False
            resolved = lang.maximize().to_dict()
            return resolved.get("script") == "Latn"
        except LanguageTagError:
            return False

    @staticmethod
    def is_ascii_text(value: Optional[str]) -> bool:
        """Return ``True`` only when cleaned text is ASCII."""
        value = TextXml.clean(value)
        if not value:
            return False
        return value.isascii()

    @staticmethod
    def truncate_with_plus(
        value: Optional[str], max_length: Optional[int]
    ) -> Optional[str]:
        """Truncate to ``max_length`` and append ``+`` when shortened."""
        if value is None or max_length is None:
            return value
        if max_length <= 0:
            return None
        if len(value) <= max_length:
            return value
        if max_length == 1:
            return "+"
        return value[: max_length - 1] + "+"

    @staticmethod
    def canonical(value: Optional[str]) -> Optional[str]:
        """Build a canonical key for deduplication."""
        value = TextXml.clean(value)
        if not value:
            return None
        value = value.casefold()
        value = re.sub(r"[^\w\s-]", "", value)
        value = re.sub(r"\s+", " ", value).strip()
        return value or None

    @staticmethod
    def unique(values: Iterable[Optional[str]]) -> List[str]:
        """Keep unique non-empty values in original order."""
        result: List[str] = []
        seen: set = set()
        for value in values:
            text = TextXml.clean(value)
            if not text:
                continue
            key = TextXml.canonical(text)
            if not key or key in seen:
                continue
            seen.add(key)
            result.append(text)
        return result

    @staticmethod
    def deduplicate(
        values: Iterable[Optional[str]], excluded: Iterable[Optional[str]]
    ) -> List[str]:
        """Drop values already excluded or already seen."""
        excluded_keys = {
            TextXml.canonical(v) for v in excluded if TextXml.canonical(v)
        }
        result: List[str] = []
        seen: set = set()
        for value in values:
            text = TextXml.clean(value)
            if not text:
                continue
            key = TextXml.canonical(text)
            if not key or key in excluded_keys or key in seen:
                continue
            seen.add(key)
            result.append(text)
        return result

    @staticmethod
    def pretty_xml(
        xml_text: Optional[str],
        wrapper_namespaces: Optional[dict[str, str]] = None,
    ) -> Optional[str]:
        """Pretty-print an XML fragment, including multi-root fragments."""
        if not xml_text:
            return xml_text

        xml_text = xml_text.strip()
        if not xml_text:
            return xml_text

        wrapper_namespaces = wrapper_namespaces or {}
        ns_attrs = " ".join(
            f'xmlns:{prefix}="{uri}"' for prefix, uri in wrapper_namespaces.items()
        )

        try:
            wrapped_xml = f"<root {ns_attrs}>{xml_text}</root>"
            dom = minidom.parseString(wrapped_xml)
            pretty = dom.toprettyxml(indent="  ")
            pretty = re.sub(r'^<\?xml[^>]*\?>\s*', "", pretty)

            lines = [line for line in pretty.splitlines() if line.strip()]
            if lines and lines[0].strip().startswith("<root"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "</root>":
                lines = lines[:-1]

            return "\n".join(lines).strip()

        except Exception:
            return xml_text

    @staticmethod
    def add_xml_text(
        parent: ET.Element,
        tag: str,
        value: Optional[str],
        max_length: Optional[int] = None,
        transform=None,
    ) -> None:
        """Create ``tag`` under ``parent`` when cleaned text is present."""
        value = transform(value) if transform else TextXml.clean(value)
        value = TextXml.truncate_with_plus(value, max_length)
        if value:
            child = ET.SubElement(parent, tag)
            child.text = value