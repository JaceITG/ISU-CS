#!/usr/bin/env python3

import re
import urllib.request
from lab import grep

with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/rig.txt") as req:
    req_data = req.read().decode("utf-8")

r = r"^\(\d{3}\) x{3}-x{4}$"

results = grep(req_data,r)

for result in results:
    print(result)
print(len(results))