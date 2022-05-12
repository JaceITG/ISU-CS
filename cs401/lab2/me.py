me = {
    "first": "Jace",
    "last": "Williams",
    "account": "cs40126",
    "birthMonth": 8,
    "birthDay": 24,
}

import json

str = json.dumps(me, indent=4)

with open("me.json", 'w') as f:
    f.write(str)
