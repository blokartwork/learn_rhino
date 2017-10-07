import rhinoscriptsyntax as rs
import random
import math

z = 0
radius = 100
theta = 0
pi = math.pi

while z < 100:
    theta = 0
    while theta < (2 * pi):
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        rs.AddPoint(x,y,z)

        theta += 0.02

    z += 1
