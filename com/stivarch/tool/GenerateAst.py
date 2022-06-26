#!/usr/bin/env python

import sys

def main(args):
    if(len(args) != 1):
        print("Usage: generate_ast <output directory>")
        exit(64)
    print(args[0])


main(sys.argv)

