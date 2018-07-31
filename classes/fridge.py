"""Demonstrate raiding a refrigerator"""

from contextlib import closing

class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print("taking {}".format(food))

    def close(self):
        print("close fridge door")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)