#!/usr/bin/env python3

import re, json
import urllib.request
from lab import grep


with urllib.request.urlopen("https://cs.indstate.edu/~lmay1/assets/rig.txt") as req:
    req_data = req.read().decode("utf-8")

with open("me.json", 'r') as f:
    me = json.loads(f.read())


r = re.compile(rf"^({me['birthMonth']}|{me['birthDay']}|{me['account'][-2:]}) ", re.I)

results = grep(req_data, r, before_lines=1, after_lines=2)

twoline = []
for result in results:
    lines = result.split("\n")
    twoline.append(str(lines[0]+"\n"+lines[1]))

print("\n\n".join(twoline))

print(len(results))
