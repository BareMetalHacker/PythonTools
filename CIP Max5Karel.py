from karel.stanfordkarel import *

"""
File: Max5Karel.py
------------------------------
Karel should place 5 beepers in the bottommost row of the world if the world is more than 5 columns wide.
If the world is less than 5 columns wide, Karel should fill the bottommmost row with beepers and not walk through any walls.
"""


def main():
    """
Karel has to install EMP mines to take out the AI drones chasing her.  She has been programmed with the skills to achieve murderous results.
Karel's only moral concern is whether semi-automnomous AI beings can feel pain.
After this job, Karel is done.  The Moscow job took her heart and before she loses her soul as well, she needs to fake her death and retire.

    """
    for i in range(5):
        while no_beepers_present():
            put_beeper()
        if front_is_clear():
            move()


if __name__ == "__main__":
    run_karel_program()