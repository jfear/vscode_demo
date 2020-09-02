"""Script to demonstrate Debugging"""
from time import sleep


def main():
    print("Hello World")

    for i in range(100):
        if i % 5 == 0:
            print(f"Yay: {i}", end="\r")
            sleep(0.5)

    _val = 2
    lvl1(_val)


def lvl1(val: int):
    print("Level 1")
    _val = val ** 2
    lvl2(_val)


def lvl2(val: int):
    print("Level 2")
    _val = val ** 2
    raise ValueError


if __name__ == "__main__":
    main()
