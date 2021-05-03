from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""


def main():
    """
Karel needs to encourage the flowers to bloom by singing to them.
Their are semi-autonomous drone robot killers out there that will kill karel if they hear him.
So karel needs to sneak up and whisper a growth song in each flower's bud.
    """
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
    run_karel_program()