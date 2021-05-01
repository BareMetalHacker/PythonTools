from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""

def main():
    """
Karel can't get out.  They have her robot daughter.  How did they find out about her?
Only Mischa knew about her and there is no way Mischa would tell anyone.  Would she?
    """
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        else:
            pick_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    else:
        pick_beeper()


if __name__ == "__main__":
    run_karel_program('Invert1.w')