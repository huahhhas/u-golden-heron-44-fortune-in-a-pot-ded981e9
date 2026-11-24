# Fortune in a Pot

[![make.fun](https://img.shields.io/badge/make.fun-bounty-7C3AED)](https://make.fun)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun](https://make.fun) bounty
**u-golden-heron-44-fortune-in-a-pot-ded981e9** — *Fortune in a Pot*.
One kind, funny fortune for a houseplant, 120 characters or fewer.

## The fortune

> You will outgrow this pot, but never this windowsill — the sun already saves you the best seat every morning.

(109 characters, one line, no trailing newline.)

## How it works

`main.py` (Python 3, standard library only) writes the fortune to
`$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline,
then self-verifies the written file: valid UTF-8, within the 1–120
character gate, exact match, single line, byte-identical.

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```
