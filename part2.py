
#2.1
def generateNumbers(num):
    a=[]
    for i in range(0,num):
        a.append(i)
    return a

print(generateNumbers(9))

#2.2
def generateNumbers(start,end,step):
    a=[]
    for i in range(start,end+1,step):
        a.append(i)
    return a
print(generateNumbers(3,9,2))

#2.3
def addNumbers(num):
    return (num*(num+1))/2

print(addNumbers(9))

#2.4
def sort_list(a):
    a.sort()
    return a

print(sort_list([2,7,3,6,4,5]))

#2.5
def sumOfDigit(number):
    sum=0
    while(number>0):
        sum+=number%10
        number/=10
    return sum
print(sumOfDigit(256))

#2.6
import random 

k=input("Enter the no to be searched")
n=input("Enter the no of elements in the array")
a=random.sample(range(10**5),n)
print (a)
if k in a:
    print("found")
else:
    print("not found")

#2.7
a=[5,6,7,8,1,2,3]
k=input("Enter the no to be searched")
flag=0
for i in a:
    if i==k:
        print("yes")
        flag=1
        break
if flag==0:
    print("Not Found")
#2.8
a=[1,2,3,4,5]
b=[2,1,0,2,0]
c=[]
for i in range(0,len(a)):
    if b[i]!=0:
        c.append(a[i]//b[i])
    else:
        c.append(float('nan'))
print(c)

#2.9
s=raw_input("Enter the string : ")
x=raw_input("Enter the word to be searched : ")
s=s.lower()
x=x.lower()
j=0
for i in s:
    if ord(x[j])==ord(i):
        j+=1
        if j==len(x):
            j=-1
            print("Found")
            break
    else:
        j=0
if j!=-1:
    print("Not Found")

#2.10
def convertToFloat(n):
    return float(n)
def convertToString(n):
    return str(n)

a=[1,2,3,4,5,6]
b1=[]
b2=[]
c1=[]
c2=[]
for i in a:
    b1.append(float(i))
    b2+=str(i)
print(b1)
print(b2)

c1=map(convertToFloat,a)
c2=map(convertToString,a)
print(c1)
print(c2)
