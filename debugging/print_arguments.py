#!/usr/bin/python3
import sys

# Iterate over the arguments, skipping the script name, using slicing
for arg in sys.argv[1:]:
    print(arg)
