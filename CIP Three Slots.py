from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""


def main():
    """
Beepers float and karel needs to get across the river to escape the AI drones chasing her.  She is made from a dense metal that won't float.  She needs at least 10 beepers at each spot
    """

    while front_is_clear():
        floaters()
        move()
    floaters()


def floaters():
    turn_right()
    move()
    for i in range(10):
        put_beeper()
    turn_around()
    move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program('Slots.w')