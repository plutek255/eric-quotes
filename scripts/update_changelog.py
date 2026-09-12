#!/usr/bin/env python3
"""Add the current-date quote update marker to CHANGELOG.md."""

from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DATE_MARKER = re.compile(r"^\[(\d{2}\.\d{2}\.\d{4})\]$")
UPDATE_LINE = re.compile(r'^\[(\d{4}-\d{2}-\d{2}T[^\]]+)\] Updated quote to "(.*)"$')


def update_changelog(qotd_path: Path, changelog_path: Path) -> bool:
    quote = qotd_path.read_text(encoding="utf-8").strip()
    content = changelog_path.read_text(encoding="utf-8") if changelog_path.exists() else ""
    lines = content.splitlines()

    # Ignore trailing blank lines when finding the last meaningful line.
    while lines and not lines[-1].strip():
        lines.pop()

    now = datetime.now(timezone.utc)
    date_marker = now.strftime("[%m.%d.%Y]")
    iso_time = now.isoformat(timespec="seconds").replace("+00:00", "Z")

    # Add the date heading only when the current marker is not already present
    # at the end of the changelog. This keeps repeated workflow runs idempotent.
    last_marker_index = next(
        (index for index in range(len(lines) - 1, -1, -1) if DATE_MARKER.fullmatch(lines[index].strip())),
        None,
    )
    if last_marker_index is None or lines[last_marker_index].strip() != date_marker:
        if lines:
            lines.append("")
        lines.append(date_marker)
        lines.append("Added by GitHub Actions")

    lines.append(f'[{iso_time}] Updated quote to "{quote}"')
    changelog_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def main() -> int:
    qotd_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("quotes/qotd.txt")
    changelog_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("CHANGELOG.md")
    update_changelog(qotd_path, changelog_path)
    print(f"updated {changelog_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
