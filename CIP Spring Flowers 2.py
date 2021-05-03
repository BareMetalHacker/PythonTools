from karel.stanfordkarel import *

"""
File: SpringFlowers.py
------------------------------
Karel starts in the bottom left corner of a world with 2 empty flower stems, facing East.
Karel should bloom both flowers with beepers and end in the bottom right corner of the world facing East.
"""


def main():
    """
Flowers will lie to Karel unless Karel can sing to them.
    """
    for i in range(2):
        stem_finder()
        climb_stem()
        sing_quiet()
        descend_stem()


def stem_finder():
    while front_is_clear():
        move()


def climb_stem():
    turn_left()
    while right_is_blocked():
        move()


def sing_quiet():
    for i in range(3):
        put_beeper()
        move()
        turn_right()
    put_beeper()
    turn_left()


def descend_stem():
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program('SpringFlowers2')