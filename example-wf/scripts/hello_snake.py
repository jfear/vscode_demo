#!/usr/bin/env python
"""Snakemake debugging Example"""
from random import randint


def main():
    print("Hello Snakemake")
    # TODO: remote debugging. snippet; smdb
    my_tricky_function()


def my_tricky_function():
    print("This is a really tricky script to debug")
    _val = randint(40, 45)
    if _val == 42:
        raise ValueError
    return _val


if __name__ == "__main__":
    main()
