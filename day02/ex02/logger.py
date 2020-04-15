#! /usr/bin/env python3

import time
from random import randint
import functools
from string import capwords
import getpass
from math import floor

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        exectime = time.time() - start
        if int(exectime) > 0:
            units = "s"
        else:
            exectime = exectime * 1000
            units = "ms"
        f = open("machine.log", "a")
        username = getpass.getuser()
        f.write("({})Running: {}    [ exec-time = {} {}]\n".format(
            username,
            capwords(func.__name__.replace('_', ' ')),
            round(exectime, 3),
            units))
        f.close()
        
        return ret
        
    return wrapper

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
