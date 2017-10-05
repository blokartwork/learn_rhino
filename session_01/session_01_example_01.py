import rhinoscriptsyntax as rs
import random

count = 0
while count < 1000:
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    point = (x,y,z)

    if rs.Distance(point, (0,0,0)) > 90 and rs.Distance(point, (0,0,0)) < 95:
        rs.AddPoint(point)
        count += 1
