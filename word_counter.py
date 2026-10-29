#!/usr/bin/env python3
import sys, os

def count(filepath):
    with open(filepath, "r") as f:
        text = f.read()
    lines = text.count("\n")
    words = len(text.split())
    chars = len(text)
    return lines, words, chars

if __name__ == "__main__":
    files = sys.argv[1:] or ["/dev/stdin"]
    total_l, total_w, total_c = 0, 0, 0
    for fp in files:
        l, w, c = count(fp)
        total_l += l; total_w += w; total_c += c
        print(f"{fp}: {l} lines, {w} words, {c} chars")
    if len(files) > 1:
        print(f"Total: {total_l} lines, {total_w} words, {total_c} chars")
