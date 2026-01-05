#!/usr/bin/env python3
from __future__ import annotations

import glob
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml
from dateutil.parser import isoparse


@dataclass
class PostError:
    file: str
    message: str


REQUIRED_FIELDS = [
    "layout",
    "title",
    "date",
    "last_modified_at",
    "categories",
    "tags",
    "excerpt",
]

# Minimal Mistakes expects categories/tags often as lists; we enforce that.
LIST_FIELDS = ["categories", "tags"]

ALLOWED_LAYOUTS = {"single", "home", "archive"}  # 'single' is typical for posts


def parse_front_matter(text: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """
    Returns (front_matter_dict, error_message).
    """
    if not text.startswith("---\n"):
        return None, "Missing front matter start delimiter '---'"

    # Find second '---' delimiter
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return None, "Missing front matter end delimiter '---'"

    fm_raw = parts[0].removeprefix("---\n")
    try:
        fm = yaml.safe_load(fm_raw) or {}
    except Exception as e:
        return None, f"YAML parse error in front matter: {e}"
    if not isinstance(fm, dict):
        return None, "Front matter must be a YAML mapping/object"
    return fm, None


def validate_date(value: Any, field: str) -> Optional[str]:
    if value is None:
        return f"Missing '{field}'"
    # Accept strings like "2024-02-01 08:00:00 +0000" or ISO8601
    if not isinstance(value, str):
        return f"'{field}' must be a string"
    try:
        # isoparse doesn't like "+0000" without colon sometimes; normalize it.
        v = value.strip()
        if v.endswith(" +0000"):
            v = v.replace(" +0000", "+00:00")
        isoparse(v)
        return None
    except Exception:
        return f"'{field}' is not a parseable date/time: {value!r}"


def validate_post(path: Path) -> List[PostError]:
    errors: List[PostError] = []
    text = path.read_text(encoding="utf-8", errors="replace")

    fm, err = parse_front_matter(text)
    if err:
        return [PostError(str(path), err)]

    for field in REQUIRED_FIELDS:
        if field not in fm or fm[field] in (None, "", []):
            errors.append(PostError(str(path), f"Missing or empty required field '{field}'"))

    # layout sanity
    layout = fm.get("layout")
    if isinstance(layout, str) and layout not in ALLOWED_LAYOUTS:
        errors.append(PostError(str(path), f"Unexpected layout '{layout}'. Allowed: {sorted(ALLOWED_LAYOUTS)}"))

    # list fields
    for lf in LIST_FIELDS:
        if lf in fm:
            if not isinstance(fm[lf], list):
                errors.append(PostError(str(path), f"'{lf}' must be a YAML list"))
            else:
                # Ensure list elements are strings
                bad = [x for x in fm[lf] if not isinstance(x, str)]
                if bad:
                    errors.append(PostError(str(path), f"'{lf}' must contain only strings (bad: {bad!r})"))

    # date fields
    for df in ["date", "last_modified_at"]:
        msg = validate_date(fm.get(df), df)
        if msg:
            errors.append(PostError(str(path), msg))

    # last_modified_at >= date (best-effort check)
    try:
        date_raw = fm.get("date")
        lm_raw = fm.get("last_modified_at")
        if isinstance(date_raw, str) and isinstance(lm_raw, str):
            d = isoparse(date_raw.replace(" +0000", "+00:00").strip())
            lm = isoparse(lm_raw.replace(" +0000", "+00:00").strip())
            if lm < d:
                errors.append(PostError(str(path), "last_modified_at is earlier than date"))
    except Exception:
        # If parsing fails, we already reported it above.
        pass

    return errors


def main() -> int:
    files = sorted(glob.glob("_posts/**/*.md", recursive=True))
    if not files:
        print("No posts found under _posts/. Skipping.")
        return 0

    all_errors: List[PostError] = []
    for f in files:
        all_errors.extend(validate_post(Path(f)))

    if all_errors:
        print("Front matter validation failed:\n")
        for e in all_errors:
            print(f"- {e.file}: {e.message}")
        print(f"\nTotal errors: {len(all_errors)}")
        return 1

    print(f"Front matter validation passed for {len(files)} post(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
