#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./get-data.py <file-with-path>")
        sys.exit(1)

    print("Data file provided: " + sys.argv[1])