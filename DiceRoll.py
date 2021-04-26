import random
#imports random library
min = 1
max = 6
#sets min and max of integers

roll_again = "yes"
#function 'rolls' the dice

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")