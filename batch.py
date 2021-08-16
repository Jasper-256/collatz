import run
from random import randint
from time import sleep

alreadyTested = 2 ** 68
googl = 10 ** 100
googlBigger = 10 ** 1000
googlMuchBigger = 10 ** 10000

min = alreadyTested
max = googlBigger

while True:
    seed = randint(min, max)
    run.collatz(seed, True, True)
    # sleep(1)
