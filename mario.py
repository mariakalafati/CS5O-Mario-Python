from cs50 import get_int


def main():
    blocks(height())


def height():
    while True:
        h = get_int("Height: ")
        if h in range(1, 9):
            break
    return h


def blocks(h):
    for i in range(h - 1):
        print(" " * (h - 2 - i), "#" * (i + 1),  "", "#" * (i + 1), end="")
        print()
    print("#" * (h),  "", "#" * (h), end="")
    print()


main()

