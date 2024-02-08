import numpy as np
n=int(input("No of altitudes:"))
a=[]
b=[]
add=0
for i in range(n):
    l=int(input("Enter the altitues:"))
    a.append(l)
print(a)
for j in range(0, len(a)):
    add+=a[j]
    b.append(add)
print(b)
l=np.sort(b)
print(l[-1])