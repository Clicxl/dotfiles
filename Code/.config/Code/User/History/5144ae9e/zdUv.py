from icecream import ic
from math import pi

CIRCUMFERENCE = 6378.1  * pi * 2 

class Runner:
    def __init__(self,vel: float,distance: float,times=1) -> None:
        self.vel = vel
        self.distance = distance
        self.times = times
        self.time = self.times * (self.distance/self.vel)
        


snail = Runner(0.002,CIRCUMFERENCE)
cheeta = Runner(40.0,CIRCUMFERENCE,100000)
        
print(f"Snail Time: {snail.time}")
print(f"Cheeta Time: {cheeta.time}")


