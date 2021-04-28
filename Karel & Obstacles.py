from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""

def main():
    """
They talked. They even begged before she was finished.
Karel did not know she was capable of such cold, calculating machine torture in the name of love.
Mischa was gone. Dead. Killed by them. She gave up Karel's daughter.
Now Karel knew who painted the target on her machine back.  It was...
    """
    move()
    turn_left()
    move()
    turn_right()
    for i in range(2):
        pink_beeper()
        pink_return()
    pink_beeper()
    turn_left()
    move()
    move()
def turn_right():
    for i in range(3):
        turn_left()
def turn_around():
    for i in range(2):
        turn_left()
def pink_beeper():
    move()
    turn_right()
    move()
    put_beeper()
def pink_return():
    turn_around()
    move()
    turn_right()

if __name__ == "__main__":
    run_karel_program('Obstacles.w')