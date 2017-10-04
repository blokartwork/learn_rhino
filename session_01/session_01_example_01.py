import rhinoscriptsyntax as rs
import random

count = 0
while count < 1000 :
    x = random.uniform(-100,100)
    y = random.uniform(-100,100)
    z = random.uniform(-100,100)
    myPoint = (x,y,z)
    rs.AddPoint(myPoint)
    count += 1
