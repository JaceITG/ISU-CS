#!/usr/bin/env python3

import re
import urllib.request
from lab import grep

with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/rig.txt") as req:
    req_data = req.read().decode("utf-8")

r = re.compile(r"^\d+ .*(east|south|north|west).*$", re.I)

results = grep(req_data, r, before_lines=1, after_lines=2)

twoline = []
for result in results:
    lines = result.strip().split("\n")
    twoline.append(str(lines[0]+"\n"+lines[3]))

print("\n\n".join(twoline))

print(len(results))
