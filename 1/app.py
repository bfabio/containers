#!/usr/bin/env python

import gzip
from typing import LiteralString

def print_gzip_file(name: LiteralString):
    file = gzip.GzipFile(name, "r")
    data = file.read()
    print(data.decode("ascii"), end="")

print_gzip_file("data.gz")
