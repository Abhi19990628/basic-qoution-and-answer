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


def sum_of_half(arr,n):
    sumfirst=0
    sumsecound=0
    for i in range(n):
        if i < n // 2 :
            sumfirst+=arr[i]
        else:
            sumsecound+=arr[i]
    print("sum first half in array :", sumfirst,end="\n")
    print("sum secound half in array :", sumsecound,end="\n")
arr=[12,23,24,77,12,10]
n=len(arr)
sum_of_half(arr,n)      

x=440
y=220
z=100
if x>y and x>z :
    print("x is greter")
elif y>x and y>z:
    print("y is grater")
else:
    print("z is big")
    
def is_perfect_number(number):
    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i
    return divisor_sum == number

# Example usage:
num = 28  # Change this number to check different numbers
if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    
def are_anagrams(num1, num2):
    # Convert numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Check if the lengths of the strings are equal
    if len(str_num1) != len(str_num2):
        return False
    
    # Sort the digits in both strings and compare
    return sorted(str_num1) == sorted(str_num2)

# Test the function
num1 = 1234
num2 = 4321
if are_anagrams(num1, num2):
    print(f"{num1} and {num2} are anagrams.")
else:
    print(f"{num1} and {num2} are not anagrams.")

def avg_even_index(arr):
    # Initialize variables to store sum and count
    total = 0
    count = 0
    
    # Iterate over even indices and accumulate sum
    for i in range(0, len(arr) , 2):
        total += arr[i]
        count += 1
    
    # Check if there are even-indexed elements
    if count == 0:
        return 0  # Return 0 if no even-indexed elements
    
    # Calculate and return the average
    return total / count

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
print("Average of even-indexed elements:", avg_even_index(arr))



   
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    
class car:
    def __init__(self,door,engine,clour,type):
        self.door=door
        self.engine=engine
        self.clour=clour
        self.type=type
    def driving(self):
        print("car used for dirving")
class audi(car):
    def __init__(self,door,engine,clour,type,hoursepower):
        super().__init__(door,engine,clour,type)
        self.hoursepower=hoursepower
l=audi(5,"v8","red","diesel",32000)
print(l.engine)
print(l.door)
print(l.type)
print(l.clour)
print(l.hoursepower)
l.driving()

def plamdrome(arr):
    start_pos=0 
    end_pos=-1
    while end_pos>=start_pos:
        if not arr[start_pos]==arr[end_pos]:
            return False
        start_pos=start_pos+1
        end_pos=end_pos-1
    return True
arr=[168]
print(plamdrome(arr))

l=[12,21,22,22,12,3,21,2,]
d=[]
for i in range (len(l)):
    for j in range (i+1,len(l)):
        if l[i]==l[j] and l[i] not in d:
            d.append(l[i])
print(d)

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
         self.balance+=amount
         print(f"deposit {amount} in rupes . current balance is {self.balance} in rupes ")
    def withdrow(self,amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"withdraw {amount} in rupes .current balance is {self.balance} in rupes")
        else:
            print("inficent balance")
            
    def check_balance(self):
        print(f"Account balance: {self.balance} rupes.")
        
        
l=BankAccount("11231")
l.deposit(1000)
l.withdrow(10)
l.check_balance()
