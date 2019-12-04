
#3.1
import numpy

a=[[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(j,end=" ")
    print("")
print("\ntranspose")
a=numpy.transpose(a)
for i in a:
    for j in i:
        print(j,end=" ")
    print("")

#3.2
import random

b=[]
for j in range(0,1000):
    a=[]
    for i in range(0,1000):
        a.append(random.randint(0,255))
    b.append(a)
"""
for i in b:
    for j in i:
        print(j,end="\t")
    print("")
"""

x,y=input("Enter the top-left coordinate").split(",")
p,q=input("Enter the bottom-right coordinate").split(",")
x,y,p,q=int(x),int(y),int(p),int(q)

#roi=[[0]*(p-x+1) for i in range(0,q-y+1)]
"""
for i in range(0,q-y+1):
    for j in range(0,p-x+1):
        roi[i][j]=b[i+y-1][j+x-1]
"""
roi=[i[x-1:p] for i in b[y-1:q]]

for i in roi:
    for j in i:
        print(j,end="\t")
    print("")

#3.3
import numpy

a=numpy.arange(30).reshape(6,5)
print(a)
b=a[-1,:]
a=numpy.delete(a,-1,0)
c=a[:,-1]
a=numpy.delete(a,-1,1)
print("a -\n"+ str(a))
print("b -"+ str(b))
print("c -"+ str(c))

#3.4
import random

a=[]
for i in range(0,150):
    b=[]
    for j in range(0,100):
        c=[]
        for k in range(3):
            c.append(random.randint(0,255))
        b.append(c)
    a.append(b)
#a[2][2][2]=266
flag=0
for i in range(0,150):
    for j in range(0,100):
        for k in range(3):
            if a[i][j][k] not in range(0,256):
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        break
if flag==1:
    print("error")
else:
    print("all ok")