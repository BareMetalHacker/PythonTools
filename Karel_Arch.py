from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""


def main():
    """
How could Karel lure her hunters out in the open.
She needs to start somewhere.
Perhaps here at the Arch shoe could create the opportunity.
    """
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()