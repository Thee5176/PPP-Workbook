#pylint:disable=W0123
print('Exercise 4.5')

# Exercise 1
print('1.')
"""
Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an inch.
"""
l = eval(input('Enter length in cm : '))
if l>=0:
	print('The length in inch is', l*2.54)
else:
	print('Invalid Number')
	
	
# Exercise 2
print('2.')
"""
Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature
is in. Your program should convert the temperature to the other unit. The conversions
are F = 95/C + 32 and C = 59/(F − 32).
"""
temp = eval(input('Please enter temp : '))
unit = input('Which unit f/c : ')
if unit=='f':
	print('Your temp in Celsius is', 5*(temp-32)/9)
elif unit=='c':
	print('Your temp in Farenheit is',9/5*(temp+32))
else:
	print('invalid unit')	


# Exercise 3
print('3.')
"""
Ask the user to enter a temperature in Celsius. The program should print a message based
on the temperature:
• If the temperature is less than -273.15, print that the temperature is invalid because it is
below absolute zero.
• If it is exactly -273.15, print that the temperature is absolute 0.
• If the temperature is between -273.15 and 0, print that the temperature is below freezing.
• If it is 0, print that the temperature is at the freezing point.
• If it is between 0 and 100, print that the temperature is in the normal range.
• If it is 100, print that the temperature is at the boiling point.
• If it is above 100, print that the temperature is above the boiling point.
"""
temp = eval(input('Enter temp in C : '))
if temp<-273.15:
	print('the temperature is invalid')
elif temp==-273.15:
    print('the temperature is absolute 0')
elif temp<0:
	print('the temperature is below freezing')
elif temp==0:
	print('the temperature is at the freezing point')
elif temp<100:
	print('the temperature is in normal range')
elif temp==100:
	print('the temperature is at the boiling point')
else:
	print('the temperature is above the boiling point')
	
	
# Exercise 4
print('4.')
"""
Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
"""
"""
cre = eval(input('How many credit have you taken : '))
if cre>23:
	if cre>53:
		if cre>83:
			print('Seniors')
		else:
			print('Juniors')
	else:
		print('Sophomore')
else:
	print('Freshman')
"""
cre = eval(input('How many credit have you taken : '))
if cre<24:
	print('Freshman')
elif cre<54:
	print('Sophomore')
elif cre<84:
	print('Juniors')
else:
	print('Seniors')


# Exercise 5
print('5.')
"""
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
"""
from random import randint
n = randint(1,10)
guess = eval(input('Please guess the num from 1-10 :'))
if n==guess:
	print('Yes, you are right')
else:
	print('Pretty close, the number is',n,'.',sep='')


# Exercise 6
print('6.')
"""
A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
program that asks the user how many items they are buying and prints the total cost.
"""
"""
amount = eval(input('How many items are you buying : '))
if amount>10:
	if amount<100:
		cost = amount*7
	else:
		cost = amount*10
else:
	cost = amount*12
print('The total bill cost $',cost,'.', sep='')
"""
amount = eval(input('How many items are you buying : '))
if amount>99:
	cost = amount*7
elif amount>9:
	cost = amount*10
else:
	cost = amount*12
print('The total bill cost $',cost,'.', sep='')


# Exercise 7
print('7.')
"""
Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise
"""
x = eval(input('Enter your first number : '))
y = eval(input('Enter your second number : '))
if abs(x-y)<0.001:
	print('Close.')
else:
	print('Not Close.')


# Exercise 8
print('8.')
"""
A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not.
"""
"""
y = eval(input('Enter a year : '))
if y%400!=0:
	if y%100!=0:
		if y%4==0:
			L = 1
		else:
			L = 0
	else:
		L = 0
else:
	L = 0

if L==1:
	print('Leap Year.')
elif L==0:
	print('not Leap Year.')
"""
y = eval(input('Enter a year : '))
if y%400==0:
	print('Leap Year.')
elif y%100==0:
	print('not Leap Year.')
elif y%4==0:
	print('Leap Year.')
else:
	print('not Leap Year.')
	

# Exercise 9
print('9.')
"""
Write a program that asks the user to enter a number and prints out all the divisors of that
number. [Hint: the % operator is used to tell if a number is divisible by something. See Section
3.2.]
"""
n = eval(input('Enter a number : '))
print('Your devisors are ',end='')
for d in range (1,n+1):
	if n%d==0:
		print(d,end=', ')
print('.')


# Exercise 10
print('10.')
"""
Write a multiplication game program for kids. The program should give the player ten randomly
generated multiplication questions to do. After each, the program should tell them
whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right.
"""
from random import randint
for i in range(1,10+1):
	x = randint(1,10)
	y = randint(1,10)
	print('Question ', i, ': ', x, ' x ', y, sep='', end='')
	a = eval(input(' = '))
	if a==x*y:
		print('Right!')
	else:
		print('Wrong. the answer is', x*y)


# Exercise 11
print('11.')
"""
Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.
Enter hour: 8
am (1) or pm (2)? 1
How many hours ahead? 5
New hour: 1 pm
"""
h = eval(input('Enter hour : '))
r = eval(input('am(1) or pm(2)? '))
n = eval(input('How many hours ahead? '))
nh = h+n
print('New hour :  ',end = '')
if nh<=12:					#print hour
	print(nh,end=' ')
else:
	print(nh%12,end=' ')
	
if (nh//2)%2==1:			#print am/pm
	print('am')
else:
	print('pm')
	

# Exercise 12
print('12.')
"""
A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
how much candy is in the bowl, then you win all the candy. You ask the person in charge the
following: If the candy is divided evenly among 5 people, how many pieces would be left
over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
are less than 200 pieces. Write a program to determine how many pieces are in the bowl.
"""
jar = 0
while True:
	if jar%5==2 and jar%6==3 and jar%7==2:
		print('The number for candy in the jar is: ',jar)
		break
	jar = jar + 1


# Exercise 13
print('13.')
"""
Write a program that lets the user play Rock-Paper-Scissors against the computer. There
should be five rounds, and after those five rounds, your program should print out who won
and lost or that there is a tie.
"""
from random import randint
result = ''
for i in range (1,5+1):
	c = randint(1,3)
	h = eval(input('Rock(1),Paper(2),Scissors(3)...Shoot! : '))
	if h-c==1 or h-c==-2:
		result = result+'1'
	elif h==c:
		result = result+'2'
	else:
		result = result+'0'
for r in range(len(result)):
	if result[r]=='1':
		print('round',r+1,':','Win')
	elif result[r]=='2':
		print('round',r+1,':','Tie')
	else:
		print('round',r+1,':','Lose')

print('Finished')