
#1.1
a=5
b=6
c=a+b
print(c)

#1.2
print(5+5)
print('5'+'5')

#1.3
p=int(input("enter a no"))
if p%2==0:
    print("even")
else:
    print("odd")

#1.4
def isIsosceles(p,q,r):
    if p==q or q==r or p==r:
        print("isosceles")
    else:
        print("not isosceles")

p=int(input("enter a side"))
q=int(input("enter a side"))
r=int(input("enter a side"))
isIsosceles(p,q,r)


#1.5
def isPrime(x):
    prime=0
    for i in range(2,x//2):
        if x%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False

p=int(input("enter a no"))
print(isPrime(p))

#1.6
p=input("enter a string")
if p==p[::-1]:
    print("palindrome")
else:
    print("Not palindrome")

#1.7
def convert(s):
    h,m=s.split(':')
    h=int(h)
    if 'pm'in s:
        h=h+12
        m=m.replace('pm','')
    if h==24 or h==12:
        h=h-12
        m=m.replace('am','')
    print(str(h)+':'+m)

p=input("enter a time")
convert(p)

#1.8
def discriminant(a,b,c):
    d=b*b-4*a*c
    if d==0:
        return "real"
    elif d>0:
        return "2 real roots"
    elif d<0:
        return "2 imaginary roots"

print(discriminant(4,8,9))
print(discriminant(1,3,1))


#1.9
def leap(x):
    if x%100==0:
        if x%400==0:
            print("leap year")
        else:
            print("non leap year")

    elif x%4==0:
        print("leap year")
    else:
        print("non leap year")

leap(2000)
leap(1900)
leap(2012)

#1.10
p=raw_input("enter a time")
q=raw_input("enter a time")
ph,pm,ps=p.split(':')
ph=int(ph)
pm=int(pm)
ps=int(ps)
qh,qm,qs=q.split(':')
qh=int(qh)
qm=int(qm)
qs=int(qs)
#if ph*60*60+pm*60+ps>qh*60*60+qm*60+qs:
s=ps-qs
m=pm-qm
h=ph-qh
if h<0 or (h==0 and m<0) or (h==0 and m==0 and s<0):
    h=-h
    m=-m
    s=-s
if s<0:
    m=m-1
    s=s+60
if m<0:
    h=h-1
    m=m+60
s=str(s)
h=str(h)
m=str(m)
print(h+":"+m+":"+s)
