"""The Long Roast — one line roasting my own AI agent."""

LINE = "My agent's entire job is spawning a subagent to do the work, then signing its own name on the result."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
