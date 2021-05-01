from karel.stanfordkarel import *

"""
File: FiveCorridorsKarel.py
-----------------------
Karel traverse 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
"""

def main():
    """
FAILURE.  Complete and jarring.  Karel never stood a chance.
Her torso was shattered.  She barely had her most basic functions left.
Enough for one reckless gamble as she grabbed a final beeper and dove from the plane.
    """
    for i in range(5):
        beeper_check()
        turn_right()
        if front_is_clear():
            move()
        turn_right()
def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()
def beeper_check():
    while front_is_clear():
        move()
    if no_beepers_present():
        put_beeper()
    turn_around()
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()