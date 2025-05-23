print('Exercise 3.8')



#Exercise 1
print('1.')
"""
Write a program that generates and prints 50 random integers, each between 3 and 6.
"""
from random import randint
for i in range(50):
    n = randint(3,6)
    print(n)

# Exercise 2
print('2.')
"""
Write a program that generates a random number, x, between 1 and 50, a random number y
between 2 and 5, and computes x^y .
"""
from random import randint
x = randint(1,50)
y = randint(2,5)
print('x^y =',x**y)

# Exercise 3
print('3.')
"""
Write a program that generates a random number between 1 and 10 and prints your name
that many times.
"""
from random import randint
x = randint(1,10)
for i in range(x):
    print('Theerapong')

# Exercise 4 ***
print('4.')
"""
Write a program that generates a random decimal number between 1 and 10 with two decimal
places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
"""
from random import randint
def gen_randnum():
    x = randint(1,9)
    y = randint(0,9)
    z = randint(0,9)
    n = str(x)+'.'+str(y)+str(z)
    n = float(n)
    return n

# Exercise 5
print('5.')
"""
Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last
is between 1 and 51.
"""
from random import randint
for i in range(1,51+1):
    rand = randint(1,i)
    print(rand)

# Exercise 6
print('6.')
"""
Write a program that asks the user to enter two numbers, x and y, and computes |x−y|/(x+y).
"""
x = eval(input('Enter first number : '))
y = eval(input('Enter second number : '))
print('the result is', abs(x-y)/(x+y))

# Exercise 7
print('7.')
"""
Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an
expression with the modulo operator, convert the angle to its equivalent between 0◦ and
360◦.
"""
angle = eval(input('Enter angle between −180◦ and 180◦: ')) 

Quadrant = angle//90
Remain = angle%90
ConvAngle = (4+Quadrant)*90+Remain

print('Your Equivalent Angle is', ConvAngle)

# Exercise 8
print('8.')
"""
Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]
"""
s = eval(input('Enter a number of seconds: '))

m_time = s//60
s_time = s%60

print(s,'second is',m_time,'minutes',s_time,'seconds')

# Exercise 9
print('9.')
"""
Write a program that asks the user for an hour between 1 and 12 and for how many hours in
the future they want to go. Print out what the hour will be that many hours into the future.
An example is shown below.
Enter hour: 8
How many hours ahead? 5
New hour: 1 o'clock
"""

now = eval(input('Enter hour: '))
h = eval(input('How many hours ahead? '))

cycle = (now+h)//12
future = abs(now+h)-12*cycle

print('New hour:',future)

# Exercise 10
print('10(a).')
"""
(a) One way to find out the last digit of a number is to mod the number by 10. Write a
program that asks the user to enter a power. Then find the last digit of 2 raised to that
power."""

pwr = eval(input('Enter power: '))

LastDigit = (2**pwr)%10

print('The Last Digit is',LastDigit)

print('10(b).')
""""
(b) One way to find out the last two digits of a number is to mod the number by 100. Write
a program that asks the user to enter a power. Then find the last two digits of 2 raised to
that power."""

pwr = eval(input('Enter power: '))

Last2Digit = (2**pwr)%100

print('The Last 2 Digit is',LastDigit)

print('10(c).')
"""
(c) Write a program that asks the user to enter a power and how many digits they want.
Find the last that many digits of 2 raised to the power the user entered.
"""
pwr = eval(input('Enter power: '))
n = eval(input('How many digits?'))

LastNDigit = (2**pwr)%10**n

print('The Last',n,'Digit is',LastNDigit)

# Exercise 11
print('11.')
"""
Write a program that asks the user to enter a weight in kilograms. The program should
convert it to pounds, printing the answer rounded to the nearest tenth of a pound.
"""
kgweight = eval(input('Enter weight in KG: '))

pdweight = round(kgweight/2.205,1)

print('Your weight in Pound is',pdweight)

# Exercise 12
print('12.')
"""
Write a program that asks the user for a number and prints out the factorial of that number.
"""
from math import factorial
n = eval(input('Enter Factorial Number: '))

nFac = factorial(n)

print('The Factorial of',n,'is',nFac)

# Exercise 13
print('13.')
"""
Write a program that asks the user for a number and then prints out the sine, cosine, and
tangent of that number.
"""
from math import sin, cos, tan
n = eval(input('Enter number :'))

nsin = sin(n)
ncos = cos(n)
ntan = tan(n)

print('sin of',n,'is',nsin)
print('cos of',n,'is',ncos)
print('tan of',n,'is',ntan)

# Exercise 14
print('14.')
"""
Write a program that asks the user to enter an angle in degrees and prints out the sine of that angle.
"""
n = eval(input('Enter an angle :'))

nsin = sin(n)

print('sine of',n,'is',nsin)

# Exercise 15
print('15.')
"""
Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in
15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown
below:
0 --- 0.0 1.0
15 --- 0.2588 0.9659
30 --- 0.5 0.866
...
345 --- -0.2588 0.9659
"""
from math import sin, cos
for i in range(0,345+1,15):
    isin = round(sin(i),4)
    icos = round(cos(i),4)

    print(i," --- ",isin,icos)

# Exercise 16
print('16,')
"""
Below is described how to find the date of Easter in any year. Despite its intimidating appearance,
this is not a hard problem. Note that ⌊x⌋ is the floor function, which for positive numbers
just drops the decimal part of the number. For instance ⌊3.14⌋ = 3. The floor function is part
of the math module.
C = century (1900’s → C = 19)
Y= year (all four digits)
m = (15 + C − ⌊C/4⌋ − ⌊8C+13/25⌋) mod 30
n = (4 + C − ⌊C/4⌋) mod 7
a = Y mod 4
b = Y mod 7
c = Y mod 19
d = (19c + m) mod 30
e = (2a + 4b + 6d + n) mod 7
Easter is either March (22+d+e) or April (d+e−9). There is an exception if d = 29 and e = 6.
In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
18. Write a program that asks the user to enter a year and prints out the date of Easter in that
year.
"""
Year = eval(input("In what year you want to check the easter date? "))

from math import floor
C = floor(Year/100)
Y = Year
m = (15+C - floor(C/4) - floor(8*C+13/25)) % 30
n = (4+C - floor(C/4)) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19*C+m) % 30
e = (2*a + 4*b + 6*d + n) % 7
z = {2, 5, 10, 13, 16, 21, 24, 39}

if d==29 and e == 6 :
    print("It's on April 19")
elif d==28 and e == 6 and m in z :
    print("It's on April 18")
elif 22+d+e <= 31 :
    print("It's on March",22+d+e)
else:
    print("It's on April",d+e-9)


# Exercise 17
print('17.')
"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
determine how many leap years there have been between 1600 and that year.
"""
CheckYear = eval(input("Please enter the year after 1600 :"))

count = 0
for year in range (1600,CheckYear+1):
    if year%400==0 :
        count = count + 1
    elif year%100==0:
        count = count
    elif year%4==0 :
        count = count + 1

print("There are",count,"leap years between 1600 and",CheckYear)

# Exercise 18
print('18.')
"""
Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]
"""
change = eval(input("Enter the change less than a bucks :"))
qua = change//0.25
dim = (change-qua*0.25)//0.1
nic = (change-(qua*0.25+dim*0.1))//0.05
pen = (change-(qua*0.25+dim*0.1+nic*0.05))//0.01

print("There would be",qua,"quarters,",dim,"dimes,",nic,"nickels, and",pen," pennies")

# Exercise 19
print('19.')
"""
Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
rectangle and a 4 × 8.
0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1
"""


w = eval(input("Enter width of the square :"))
h = eval(input("Enter height of the square :"))

count = 0
for i in range(h):
    for j in range(0,w):
        num = (count*w+j)%10
        print(num, end = " ")
    print("\n")
    count = count + 1
        



print("Finished")