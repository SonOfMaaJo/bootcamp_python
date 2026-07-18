# Thi is my first package create during bootcamp python

to build run the following command:
```bash build.sh
```
for example:
```python
from my_minipack.logger import CoffeeMachine
if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)```

you will find the file machine.log in the current folder and then run:
```bash
cat machine.log```

to see the output of the file machine.log

good, luck !!!
