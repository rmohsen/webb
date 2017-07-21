from __future__ import absolute_import, unicode_literals
import random
from webb.celery import app


@app.task(name="sum_two_numbers")
def add(x, y):
    return x + y


@app.task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@app.task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)