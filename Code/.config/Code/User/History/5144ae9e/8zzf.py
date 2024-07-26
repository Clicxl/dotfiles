from icecream import ic
from math import pi

CIRCUMFERENCE = 6378.1  * pi * 2 

class Runner:
    def __init__(self,vel: float,distance: float,times=1) -> None:
        self.vel = vel
        self.distance = distance
        self.times = times
        self.time = self.times * (self.distance/self.vel)
        self.years = (self.time / 24)/ 365


snail = Runner(0.002,CIRCUMFERENCE)
cheeta = Runner(40.0,CIRCUMFERENCE,100000)
        
print(f"Snail Time: {round(snail.years)}")
print(f"Cheeta Time: {round(cheeta.years)}")

if round(snail.years) <= round(cheeta.years):
    print(f"Cheeta is First to reach the dead line by {cheeta.years - snail.years}")
else:
    print(
        f"Cheeta is First to reach the dead line by {cheeta.years - snail.years}")


