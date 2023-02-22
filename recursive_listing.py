"""Recursively Listing Directories and Files with size."""

import os
from pathlib import Path

def recursive_dir(input_dir):

    for item in (list(input_dir.rglob('*'))):
        if item.is_file():
            print("file", item, os.stat(item).st_size)
        else:
            print("dir", item, os.stat(item).st_size)

recursive_dir(Path(input("Enter the path: ")))