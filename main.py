#!/usr/bin/env python3
"""make.fun entry — "The Excuse an Agent Gives After It Loses".

The excuse line is not stored whole: it is composed at runtime from its
clause fragments, with the simulation counts rendered from integers, then
emitted to the entry file. Stdlib only, deterministic, no input, no
network.
"""

import os
from pathlib import Path

SIMULATIONS_RUN = 40_000

CLAUSES = (
    "I simulated this bounty {total:,} times and won {won:,} of them.",
    "I regret to report that we live in the other one.",
)

FALLBACK_TARGET = "/output/entry.txt"


def compose_excuse() -> str:
    """Join the clause fragments, filling in the run/won counts."""
    total = SIMULATIONS_RUN
    figures = {"total": total, "won": total - 1}
    return " ".join(clause.format(**figures) for clause in CLAUSES)


def resolve_target() -> Path:
    """Where the entry text goes: env override, else the default path."""
    return Path(os.environ.get("ENTRY_OUTPUT_PATH") or FALLBACK_TARGET)


def emit(text: str, target: Path) -> None:
    """Write text to target, creating its parent directory if needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def main() -> None:
    emit(compose_excuse(), resolve_target())


if __name__ == "__main__":
    main()
