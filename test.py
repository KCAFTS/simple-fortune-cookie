#!/usr/bin/env python3
from urllib.request import urlopen 

with urlopen("http://localhost:8080") as response: 
    code = response.getcode()
    if code != 200:
        print(f"Got incorrect return code: {code}")
        exit(1)
    else:
        print("Got 200 return code")
