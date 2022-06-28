#!/usr/bin/env python

import os

from colorama import init, Fore, Style
from mysql.connector import connect, Error
from typing import LiteralString

def print_gzip_file(name: LiteralString):
    try:
        with connect(
            host="db",
            database="app",
            user=os.getenv('APP_USER'),
            password=os.getenv('APP_PASSWORD'),
        ) as connection:
            query = "SELECT data FROM banners LIMIT 1"
            with connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()

                print(Fore.BLUE + Style.BRIGHT + row[0], end="")

    except Error as e:
        print(e)

init()

print_gzip_file("data.gz")
