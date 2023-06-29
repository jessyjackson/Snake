import math
import random as rnd
class Food:
    X = 0
    Y = 0
    def newPosition(self):
        self.X = math.floor(rnd.random()*5)
        self.Y = math.floor(rnd.random()*5)