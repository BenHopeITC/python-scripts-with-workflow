#!/usr/bin/env python3

import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./get-data.py <file-with-path>")
        sys.exit(1)

    dataFile = sys.argv[1]

    print("Data file provided: " + dataFile)

    with open(dataFile) as csvfile:
        csvReader = csv.reader(csvfile)
        for id in csvReader:
            print("Data ID provided: " + id[0])

    