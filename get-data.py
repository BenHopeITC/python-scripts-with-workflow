#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage: ./app.py <file-with-path>")
        sys.exit(1)

    print("Data file provided: " + sys.argv[0])