#!/usr/bin/env python3

import re
import urllib.request

def grep(text, regex, before_lines=0, after_lines=0):

    if type(regex) is str:
        regex = re.compile(regex)
    if type(regex) is not re.Pattern:
        raise Exception("Invalid regex type")

    results = []

    lines = text.split("\n")

    for i in range(len(lines)):
        line = lines[i]
        m = regex.search(line)
        if m:
            start = i - before_lines
            end = i + 1 + after_lines
            results.append("\n".join(lines[start:end]))

    return results
