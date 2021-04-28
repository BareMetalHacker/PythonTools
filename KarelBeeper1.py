from karel.stanfordkarel import *

"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""

def main():
    """
Mischa.  It had to be Mischa.  Only she could have told them about her daughter.
The semi-autonomous killer drones were being directed by someone or something and that entity had her daughter.
    """

    move()
    pick_beeper()
    turn_left()
    move()
    move()
    put_beeper()
    turn_right()
    move()
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == "__main__":
    run_karel_program()