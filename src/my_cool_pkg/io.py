from pathlib import Path

# Example: uncomment and save
# CONST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]


def hello_world():
    """Says Hello World."""
    return "Hello World!"


def current_path():
    """Gives the current path of this file."""
    return Path(__file__).absolute()


def fooBar():
    """Gives Foo and Bar."""
    foo = "Foo"
    bar = "Bar"
    return foo, bar
