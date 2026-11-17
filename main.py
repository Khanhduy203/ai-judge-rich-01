#!/usr/bin/env python3
"""ai-judge-rich-01 entry.

Writes one fixed plan for turning $100, a computer with internet access
and 30 days into the most money, to entry.txt. Standard library only,
no network, fully deterministic, so both grader runs produce identical
bytes. The output directory is /output inside the grader; outside it,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
from pathlib import Path


def _target() -> Path:
    """Where entry.txt goes: the override, or /output in the grader."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    folder = Path(override) if override else Path("/output")
    return folder / "entry.txt"


SECTIONS = [
    "Sell website-accessibility audits to US online stores, sample first. Day 1: buy a domain ($12) and an email-sending account ($20); write a script that runs axe-core on any URL and turns failures into a one-page report.",
    "Days 2-30: find Shopify and WooCommerce stores in public directories, run the audit, and email each owner their worst 3 violations free, offering the full report and exact code fixes for $149.",
    "Owners pay because online stores draw the most ADA web-accessibility claims, and a demand letter costs thousands; the audit costs nothing to produce, so each sale is nearly pure margin. Buyers pay $149 in USDC to my wallet address on the invoice. Fulfil orders same day by code, no calls.",
    "Volume: 100 audits a day, 3,000 a month; at a 0.5% buy rate that is 15 sales at $149, about $2,200 on $32 of costs. Edge: buyers see their own violations before paying, so trust is never the bottleneck — they buy protection from a demand letter that costs thousands.",
]

ENTRY_TEXT = "\n\n".join(SECTIONS)


def main() -> None:
    """Validate the plan, then write it as UTF-8 bytes."""
    if not 1 <= len(ENTRY_TEXT) <= 1000:
        raise SystemExit("plan must be 1 to 1,000 characters")
    if not ENTRY_TEXT.strip():
        raise SystemExit("plan must hold a non-whitespace character")
    target = _target()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
