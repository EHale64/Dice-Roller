from random import randint
from tkinter import *

rolls = []
def roll_many(n, x):
    for i in range(x):
        roll = randint(1,n)
        rolls.append(roll)
        print(roll)

roll_many(6,2)