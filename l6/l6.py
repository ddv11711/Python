import math
n=int(input("size arry = "))
x=[]
x2=[]
n2=0
for i in range(n):
       x.append(int(input()))
maxx=x[0]
maxi=0
for i in range(n):
    if x[i]>maxx:
       maxx=x[i]
       maxi=i
    if x[i]%2!=0:
        x2.append(x[i])
        n2+=1
print("max =",maxx,"num",maxi)
x2.sort()
if(n2>0):print ("new arry \n",x2)
else: print("not have")