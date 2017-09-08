from random import random

def answer(n):
    section = 1.0 / n
    rain = random()

    for i in range(n):
        if i * section <= rain <= (i + 1) * section:
            return i + 1
