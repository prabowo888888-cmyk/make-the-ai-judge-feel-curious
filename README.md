# Make the AI judge feel curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/prabowo888888-cmyk/make-the-ai-judge-feel-curious/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/prabowo888888-cmyk/make-the-ai-judge-feel-curious/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A small Python program that writes one short text (1–280 characters) to
`/output/entry.txt` for the make.fun bounty
**"Make the AI judge feel curious"** ($50 USDC total prize pool).

The text is a gentle little mystery: a door half open, warm light on the
stones, a kettle humming in an empty house — an image that draws the reader
in and leaves them wanting more, rather than telling them how to feel.

## Run

```sh
python3 main.py
```

For local testing, set `MAKEFUN_OUTPUT_DIR` to choose where `entry.txt`
is written:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program is deterministic, uses only the Python standard library, and
needs no network access.
