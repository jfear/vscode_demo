from pathlib import Path

CONST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]
def hello_world():
    return "Hello World!"

def current_path():
    return Path(__file__).absolute
