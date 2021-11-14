from random import randint
# import statistics

rolls = []
def roll_many(n, x):
    for i in range(x):
        roll = randint(1,n)
        rolls.append(roll)
        print(roll)

roll_many(6,2)