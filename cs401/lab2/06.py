#!/usr/bin/env python3

import re
import urllib.request
from lab import grep

with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/rig.txt") as req:
    req_data = req.read().decode("utf-8")

r = re.compile(r"(ny|ca|in)[a-z]*, (ny|ca|in)", re.I)

results = grep(req_data, r, before_lines=2, after_lines=1)

print("\n\n".join(results))

print(len(results))
