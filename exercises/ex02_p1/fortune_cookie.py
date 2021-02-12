"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730287108"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    fortune: int = randint(1, 4)
    if fortune < 3:
        if fortune < 2:
            return "You will adopt a long-haired cat named Tom."
        else:
            return "You will meet the love of your life this year."
    else:
        if fortune < 4:
            return "You will enjoy a large chocolate chip cookie with icecream soon."
        else:
            return "You will read an inspring book this month."


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()