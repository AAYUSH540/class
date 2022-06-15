# Function without arguments
# Sum
def sum():
    x=int(input("Number1(sum) = "))
    y=int(input("Number2(sum) = "))
    total = x+y
    print(f"{x} + {y} = {total}")

sum()

print()
# function with arguments
# Sum
x=int(input("Number1(function with arg) = "))
y=int(input("Number2(function with arg) = "))
def sum_arg(x,y):
    total = x+y
    print(f"Sum= {total}")

sum_arg(x,y)

print()
# Average
def avg_arg(x,y):
    average = (x+y)/2
    print("Average = ",average)

avg_arg(x,y)

print()

#Square
def sq_arg(x):
    square = x*x
    print("Square = ",square)

sq_arg(x)

print()

# pass 4 subject marks and cal the %

def per(s1,s2,s3,s4):
    total = s1+s2+s3+s4
    percentage = total / 4
    print(f"Percentage for subject marks({s1},{s2},{s3},{s4} ----> {percentage})")

s1,s2,s3,s4 = eval(input("Enter 4 subject marks : "))
per(s1,s2,s3,s4)

print()

# cal the simple interest by passing the parameters

def interest(p, r, n):
    inter = (p * r * n)/100
    print(f"Interest for (P = {p},R = {r},N = {n} ----> {inter})")


p,r,n= eval(input("Enter P(principle amount) , R(interest rate) , N(time period) : "))
interest(p,r,n)

print()

# H.W.
# cal bonus at 30% on a salary

def bonus1():
    sal1=int(input("Salary : "))
    bon1=sal1*0.3
    print(f"Bonus at 30% on salary({sal1}) ----> {bon1}")

bonus1()

print()

# above program with parameters
def bonus2(sal2):
    bon2=sal2*0.3
    print(f"Bonus at 30% on salary({sal2}) ----> {bon2}")

sal2=int(input("Salary : "))
bonus2(sal2)

print()

# cal factorial
def fact(a):
    i=a
    ans=1
    while i>0:
        ans=ans*i
        i-=1
    print(f"Factorail of {a} ----> {ans}")

a=int(input("Enter Number To Find Factorial : "))
fact(a)

print()

# maximum out of 3 numbers
def maximum(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            max=n1
        else:
            max=n3
    else:
        if n2>n3:
            max=n2
        else:
            max=n3
    print(f"Maximum out of {n1} , {n2} , {n3} ----> {max}")

n1,n2,n3=eval(input("Enter 3 numbers to find max : "))
maximum(n1,n2,n3)

print()

# calculate tax on product by 18%
def tax(price):
    total=price+(price*0.18)
    print(f"Price of product = {price} , Tax = {price*0.18} ----> Total price = {total}")

price=int(input("Price of Product : "))
tax(price)

print()

# calculate fair by passing kilometer and rate of kilometer
def fair(kilometer,rate_of_kilometer):
    fair_value=kilometer*rate_of_kilometer
    print(f"Fair value of {kilometer}*{rate_of_kilometer} ----> {fair_value}")

kilometer,rate_of_kilometer=eval(input("Enter kilometer , rate of kilometer : "))
fair(kilometer,rate_of_kilometer)


