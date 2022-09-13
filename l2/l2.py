import math
print("t<x")
x=int(input("x="))
t=int(input("t="))
z=math.sqrt((12*math.pow(x,4)*0.2/math.sqrt(t)-2))*math.sin(t)
print("z= {0:.2f}".format(z))
