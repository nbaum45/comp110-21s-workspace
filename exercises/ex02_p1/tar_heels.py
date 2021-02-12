"""Tar Heels exercise redux as a structured program."""

__author__ = "730287108"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(user_input: int) -> str:    
    if user_input % 2 == 0 and user_input % 7 == 0:
        return "TAR HEELS"
    else:
        if user_input % 2 == 0:
            return "TAR"
        else: 
            if user_input % 7 == 0:
                return "HEELS"
            else: 
                return "CAROLINA"


if __name__ == "__main__":
    main()