#!/usr/bin/env python3
import urllib.request
import json
import sys
import os

if len(sys.argv) < 2:
    print("usage: gistdl GIST_ID [DIRECTORY]", file=sys.stderr)
    exit(1)

gist_id = sys.argv[1]

folder = ""
if len(sys.argv) >= 3:
    folder = sys.argv[2]
    os.makedirs(folder, exist_ok=True)

try:
    with urllib.request.urlopen("https://api.github.com/gists/{}".format(gist_id)) as url:
        data = json.loads(url.read().decode())
        for name, value in data["files"].items():
            filename = os.path.join(folder, name)
            with open(filename, 'w') as out:
                out.write(value["content"])
            print("written {}".format(filename))

except Exception as err:
    print("error occured: {}".format(err), file=sys.stderr)
