#!/usr/bin/env python

# ^ shebang line to specify wich interpreter to use

from sys import stdin # Imports stdin from sys package


def say_hi():
    """
    Asks for a stranger's name and greets him
    """
    # Ask for name
    print("What's your name?")
    # Read input from stdin and remove trailing whitespaces
    name = stdin.readline().strip()
    # Print personalized greeting
    print("Hello %s!" % name)

# Only say hi when run from the command line
if __name__ == "__main__":
    say_hi()
