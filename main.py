li=[1,2,3,4,5,6,7,8]
s=li[0]
for i in li:
    if i>s:
        s=i
print(s)


li=[1,2,3,4,5,6,7]
s=0
for i in li:
    s += i
print(s)

li=[1,2,3,4,5,6,8]

p=1
for i in li:
    p=p*i
print(p)

l=[1,2,3,33,3,2,2,1,1,223,2,123,2,1,2,2,3]
l.sort()
print(l[-1])


l=[1,2,3,4,5,6,7,8]
for i in l:
    if i%2==0:
        print("the even no is :",i )
        
    else:
        print("the odd no is :" ,i)
    
    


l=[1,2,3,4,5,6,67,78,78,-1,-23,-432,-3,-2]
p=0
for i in l:
    p += i
print(p)
    
l=[1,2,3,4,5,6,7,8,89,12345,4567]
p=l[0]
for i in l:
    if i>p:
        p=i
print(p)

l=[]
p=1
for i in l:
    p=p*i
print(p)


l=[1,2,3,4,5,6,7,810,100,121,21]
maxi=l[0]
for i in l:
    if i>maxi:
        maxi=i
print(maxi)


# l=[1,2,3,4,5,6,7,8,]
# multi=l[0]
# for i in l:
#     if i>multi:
        
        
# import numpy 
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
 
# # using numpy.prod() to get the multiplications
# result1 = numpy.prod(list1)
# result2 = numpy.prod(list2)
# print(result1)
# print(result2)

from operator import*
l=[1,2,3,4,5]
print("the list is :", l)
p=1
for i in l:
   p = mul(i,p)
print(p)

def multiply_number(list):
    p=1
    for i in list:
        p=p*i
    return p
given_list=[1,2,3,4,5,6,7,8,9]
print("the normal list is:",given_list)
print("multiply the all elements is:")
print(multiply_number(given_list))

l=[1,2,3,4,5,6,7,8,9]
p=1
for i in l:
    p=p*i 
print(p)  



l=[1,2,3,4,5,6,7]
for i in l:
    if i%2==0:
        print("even no is :",i)
        
l=[1,2,3,22,33,21,33,4,3,2234,4567,6543,45676]
for i in l:
    if i%2!=0:
        print("even no id ",i)
        
l=[1,2,3,4,5,6,7,8,9,10,-2,-11,-123,-12]
for i in l:
    if i>0:
        print("postive no is ",i)
    else: i<0
    print("negtive no is ",i)


l=[1,2,3,3,44,4,3,2,21]
i=1
# if element present then return
# exist otherwise not exist
if i in l: 
    print("exist") 
else: 
    print("not exist")

t=[1,2,3,22,21,22,22,2,2,22,22,2,2,22]
x=int(input("enter the no is :"))
for i in t:
    if i == x:
        print(i)
        
        
l=[1,2,3,21,1,2]
a=0
for i in l:
    a += i
avg=a/len(l)
print("sum of l :", a)
print("avarage of no :", avg)

l=["ABHI",12,21,22,11,22,21,2,0]
a=[]
for i in l:
    if l.count(i)>1 and i is not a:
        a.append(i)
print(i)


def factorial(n):
    if n==0:
       return 1
    else:
        return n*factorial (n-1)
        
print(factorial(10))
        
        
        
l=["ABHI",12,21,22,11,22,21,2,0]
a=[]
for i in l:
    if l.count(i)>1 and i not in a:
        a.append(i)
print(a)


l=[1,22,1,22,34,43,43]
a=[]
for i in l:
    if l.count(i)>1 and i not in a:
        a.append(i)
print(a)
        
l=[1,2,3,4,5,6,7,8,9,9]
a=[]
for i in l:
    if l.count(i)>1 and i not in a:
        a.append(i)
        print(a)

def evenodd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(evenodd(10))

def evenodd(n):
    if n%2==0:
        print("even",n)
    else:
        print("odd",n)
        
evenodd(7)
l=[12,21,22,22,12,3,2]
d=[]
for i in range (len(l)):
    for j in range (i+1,len(l)):
        if l[i]==l[j] and l[i] not in d:
            d.append(l[i])
            print(d)
            
            
def shout(txt):
    return txt.upper()
print(shout("hello"))
yellow=shout
print(yellow("abhishek"))


def prag(txt):
    return txt.upper()
def goti(txt):
    return txt.lower()
def geet(func):
    geeting = func("""hi i am abhishek kumar singh i dont get a job """)
    print(geeting)

geet(prag)




def abhi(txt):
    return txt.upper()
def gulli(txt):
    return txt.lower()
def mp(func):
    bolte=func(""" tu ghar kab ayega ga """)
    print(bolte)
    
    
mp(abhi)


def calcution (a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add, sub , mul , div
C=calcution(120,10)
print(C)


def emp(name,sal=10000):
    print("Name:",name ,"sal:",sal)
    
emp("abhishek",900000)
emp("ravi")


def O ( a, b):
    
     def addi(a,b):
         return a+b
     add=addi(a,b)
     return add+5
k=O(2,4)
print(k)


def addition (a):
    if a:
        return a+addition(a-1)
    else:
        return 0 
        
o=addition(10)
print(o)

def ajjj(name,age):
    print(name,age)
    
o=ajjj("abhishek",200)

kal=ajjj
kal("abhi",2992)



for i in range (4,52):
    if i%2==0:
        print(i)
    
l=[22,3,4,2,211,3,2,21,3]
print(max(l))


