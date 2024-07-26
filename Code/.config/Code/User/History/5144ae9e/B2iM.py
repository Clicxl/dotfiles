from icecream import ic
from math import pi

CIRCUMFERENCE = 6378.1  * pi * 2 

class Runner:
    def __init__(self,vel: float,distance: float,times=1) -> None:
        self.vel = vel
        self.distance = distance
        self.times = times
        ic(self.distance/self.vel)
        self.time = self.distance/self.vel
        ic(self.time)
        


snail = Runner(0.002,CIRCUMFERENCE)
cheeta = Runner(40.0,CIRCUMFERENCE,100000)
        


