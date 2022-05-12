#!/usr/bin/env python3

import re, json
import urllib.request
from lab import grep


with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/rig.txt") as req:
    req_data = req.read().decode("utf-8")

with open("me.json", 'r') as f:
    me = json.loads(f.read())


r = re.compile(rf"^{me['first'][0]}[a-zA-Z]*\s+{me['last'][0]}[a-zA-Z]*$", re.I)

results = grep(req_data, r, before_lines=0, after_lines=3)

print("\n\n".join(results))

print(len(results))
