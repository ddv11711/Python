import math
from posixpath import split
s=input("s = \n")
l=len(s)
k=0
for i in range(l):
    if s[i]=='a':
        k+=1
s=s.replace('a','o')
print("size string = ",l)
print("kolvo a = ",k)
print(s)