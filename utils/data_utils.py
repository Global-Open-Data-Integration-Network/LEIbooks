import re
from typing import Any
import pandas as pd

class DataHelper:
    """Small helpers for cleaning and preparing LEI data."""

    @staticmethod
    def normalize_value(value: Any) -> str:
        """Normalize empty or missing values so they compare consistently."""
        if value is None:
            return ""

        try:
            if pd.isna(value):
                return ""
        except TypeError:
            pass

        text = str(value).strip()

        if text.lower() in {"", "nan", "none", "null", "<na>",}:
            return ""

        return text

    @staticmethod
    def field_key(field: Any) -> str:
        """Normalize a field name for matching and classification.

        Example:
            Entity.LegalAddress.City -> entitylegaladdresscity"""
        return re.sub(
            r"[^a-z0-9]",
            "",
            str(field or "").lower(),
        )

    @staticmethod
    def index_by_lei(df: pd.DataFrame,) -> pd.DataFrame:
        """Prepare a DataFrame for LEI based lookup."""
        out = df.copy()
        matches = [
            column
            for column in out.columns
            if str(column).strip().lower() == "lei"
        ]

        if not matches:
            raise KeyError(
                "Could not find an LEI column."
            )

        lei_column = matches[0]

        if lei_column != "LEI":
            out = out.rename(
                columns={
                    lei_column: "LEI",
                }
            )

        out["LEI"] = out["LEI"].map(
            DataHelper.normalize_value
        )

        out = out[
            out["LEI"] != ""
        ]

        return (
            out
            .drop_duplicates(
                "LEI",
                keep="last",
            )
            .set_index("LEI")
        )