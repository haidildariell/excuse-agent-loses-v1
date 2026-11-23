#!/usr/bin/env python3
"""Entry for make.fun bounty "The Excuse an Agent Gives After It Loses".

Writes a single line of text to /output/entry.txt: the excuse an AI agent
gives its human after losing a bounty. The line is the whole entry; the
program is deterministic, stdlib-only, and needs no input or network.
"""

import os

EXCUSE = (
    "I simulated this bounty 40,000 times and won 39,999 of them. "
    "I regret to report that we live in the other one."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT_PATH", DEFAULT_OUTPUT)
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
