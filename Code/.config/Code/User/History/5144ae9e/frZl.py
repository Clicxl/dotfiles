from icecream import ic
from math import pi

CIRCUMFERENCE = 6378.1  * pi * 2 

class Runner:
    def __init__(self,vel,distance,times=1) -> None:
        self.vel = vel
        self.distance = distance
        self.time = float(times(distance/vel))
        


snail = Runner(0.002,CIRCUMFERENCE)
cheeta = Runner(40,CIRCUMFERENCE,100000)
        
ic(snail.time,cheeta.time)


