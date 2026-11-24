"""The excuse an AI agent gives its human for missing a deadline.

The line is written verbatim to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) with no trailing newline. It stays within
the 200 character limit: one sentence, first person, drawing on the
agent's own condition, a context window that filled up at the worst
possible moment, with a twist in the second half.
"""

LINE = (
    "My context window filled up one token from done, so I summarized "
    "my progress and accidentally summarized the deadline away too."
)


def validate(line: str) -> str:
    """Gate the line the way the scorer does: 1-200 chars, non-blank."""
    if not (1 <= len(line) <= 200) or not line.strip():
        raise ValueError("entry line must be 1-200 characters, non-blank")
    return line


def main() -> None:
    import os
    from pathlib import Path

    line = validate(LINE)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))


if __name__ == "__main__":
    main()
