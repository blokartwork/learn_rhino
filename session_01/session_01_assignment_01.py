import rhinoscriptsyntax as rs
import random
import math

z = 0
radius = 10
theta = 0
pi = math.pi
count = 0

while z < 100:
    theta = 0
    while theta < (2 * pi):
        if count % 4 == 0:
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
        else:
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)

        count += 1
        rs.AddPoint(x,y,z)
        theta += 0.02

    if z > 40 and z < 60:
        radius += 1
    else:
        radius += random.uniform(0,1)

    z += 1
