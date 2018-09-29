""" python script run on the HOST to generate a keymap file.
"""
import sys

for i, line in enumerate(open(sys.argv[1])):
    X = line.split()
    print(i, X)
