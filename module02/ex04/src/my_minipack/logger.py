import time
from random import randint
import os


def log(func):
    def another_function(*args, **kwargs):
        start = time.time()
        resultat = func(*args, **kwargs)
        end = time.time()
        name = ' '.join(func.__name__.split("_"))
        for n in name:
            n = n.upper()
        ls = f'({os.getenv("USER")})Running: {name}'
        for _ in range(19 - len(name)):
            ls += ' '
        t = end - start
        if t < 1:
            ls += f'[exec-time = {t * 1000:.3f} ms ]\n'
        else:
            ls += f'[exec-time = {t:.3f} s ]\n'
        with open("machine.log", "a", encoding="utf-8") as f:
            f.write(ls)
        return resultat
    return another_function


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
            print("Coffee is ready")

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
