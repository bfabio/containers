#!/usr/bin/env python

import gzip

from colorama import init, Fore, Style
from typing import LiteralString


def print_gzip_file(name: LiteralString):
    file = gzip.GzipFile(name, "r")
    data = file.read()
    print(Fore.BLUE + Style.BRIGHT + data.decode("ascii"), end="")

init()

print_gzip_file("data.gz")
