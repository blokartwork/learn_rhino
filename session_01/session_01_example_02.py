import rhinoscriptsyntax as rs
import random
import math

z = -100
radius = 0
theta = 0

while z <= 100:
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)

    rs.AddPoint(x,y,z)

    radius += 0.003
    theta += 1
    z += 0.01
