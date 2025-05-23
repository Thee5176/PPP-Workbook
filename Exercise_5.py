print('Exercise 5.9')

# Exercise 1(count)
print('1.')
"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.
"""
count = 0
for i in range(1,100+1):
    if (i*i)%10==1:
        count = count + 1
print('There are',count,'of squared numbers end in a 1')

# Exercise 2(count)
print('2.')
"""
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 4
 and how many end in a 9.
"""

def sqc(num):
    count = 0
    for i in range(1,100+1):
        if (i*i)%10==num:
            count = count + 1
    print('There are',count,'of squared numbers end in',num)
e4 = sqc(4)
e9 = sqc(9)


# Exercise 3(sum)
print('3.')
"""
Write a program that asks the user to enter a value n, and then computes (1+ 1/2 + 1/3 +
· · ·+ 1/n ) − ln(n). The ln function is log in the math module.
"""
from math import log
n = eval(input('Please enter number :  '))
ans = 0
for i in range(1,n+1):
    if i<n:
        ans = ans + 1/i
    elif i==n:
        ans = ans + 1/n + log(n)
print('The (1+ 1/2 + 1/3 +· · ·+ 1/n ) − ln(n) of', n, 'is', ans)

# Exercise 4(sum)
print('4.')
"""
Write a program to compute the sum 1 − 2 + 3 − 4 + · · · + 1999 − 2000.
"""
ans = 0
for i in range(1,2000+1):
    ans = ans + (-1**i-1)*i
print ('The answer is',ans)

# Exercise 5(sum)
print('5.')
"""
Write a program that asks the user to enter a number and prints the sum of the divisors of that 
number. The sum of the divisors of a number is an important function in number theory.
"""
n = eval(input('Please enter number :  '))
sod = 0
for i in range(1,n+1):
    if n%i==0:
        sod = sod + i
print ('The sum of divisors is',sod)


# Exercise 6(sum)
print('6.')
"""
A number is called a perfect number if it is equal to the sum of all of its divisors, not including
 the number itself. Write a program that finds all four of the perfect numbers that are less than 10000.
"""
def per_num(a,b):
    ans = []
    for n in range(a,b+1):
        sod = 0
        for i in range(1,n):
            if n%i==0:
                sod = sod + i
        if sod==n:
            ans.append(n)
    print(ans)
print('The perfect numbers less than 10000 are',end = '')
per_num(1,9999)

# Exercise 7
print('7.')
"""
An integer is called squarefree if it is not divisible by any perfect squares other than 1. 
Write a program that asks the user for an integer and tells them if it is squarefree or not.
"""
def sqfree(n):
    n = int(n)
    gotit = 0
    sqnum = []
    for i in range(2,n):
        x=i**2
        if x<=n:
            sqnum.append(x)
            print(x)
    if sqnum is None:
        return 'Is squarefree number'
    else:
        for j in sqnum:
            k = n%j
            if k==0:
                gotit = 1
                return 'Is not squarefree number'   
        if gotit==0:
            return 'Is sqarefree number'   
num = eval(input('Please enter number : '))
print(sqfree(num))

# Exercise 8
print('8.')
"""
Write a program that swaps the values of three variables x, y, and z, so that x gets the value
 of y, y gets the value of z, and z gets the value of x.
"""
x = eval(input('Please enter value of x : '))
y = eval(input('Please enter value of y : '))
z = eval(input('Please enter value of z : '))
print('Former:\tx =',x,', y=',y,', z=',z)
x,y,z = y,z,x
print('New:\tx =',x,', y=',y,', z=',z)

# Exercise 9
print('9.')
"""
Write a program to count how many integers from 1 to 1000 are not perfect squares, 
perfect cubes, or perfect fifth powers.
"""
#V1 - Fail
"""
def count_perfect_power(a,b):    #a = from 1 to that num
    gotit = 0                    #b = powers num
    count = 0
    pnum = []
    for i in range(2,a):
        x=i**b
        if x<=a:
            pnum.append(x)
    if pnum is None:
        count = 0
    else:
        for k in range(1,a):
            for j in pnum:
                if k<j:
                    continue
                y = k%j
                if y==0:
                    gotit = 1
                    count = count + 1   
    return count

sq = count_perfect_power(1000,2)
cu = count_perfect_power(1000,3)
fi = count_perfect_power(1000,5)
ans = 1000-(sq+cu+fi)
print('There are',ans,'numbers are not perfect sq cu fi')
"""
def perfect_power(a,b):
	count = 0
	for i in range (1,a):
		if (i**(1/b))%1==0:
			count = count + 1
	return count
	
#find all perfect number seperately(AUBUC)	
U = perfect_power(1000,2)+perfect_power(1000,3)+perfect_power(1000,5)

#find all intercept area(AnB + BnC + AnC)
In = perfect_power(1000,6)+perfect_power(1000,15)+perfect_power(1000,10)

#find center intercept area(AnBnC)
In2 = perfect_power(1000,30)

#
ans = 1000 -( U - In + In2)
print('The number that is not perfect sq cu fif : ',ans)


# Exercise 10
print('10.')
"""
Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores. 
(b) Print out the average of the scores.
(c) Print out the second largest score. ??
(d) If any of the scores is greater than 100, then after all the scores have been entered, 
print a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them. ??
"""
max = 0 #a
max2 = 0
min = 100 #a
mon2 = 100

total = 0 #b
count = 0 #b

maxdiff = 0 #c

over = 0 #d

for i in range(1,10+1):
    num = eval(input("Please enter score{} :".format(i)))
    if num > max : #a,c
        max2 = max
        max = num
    if num < min : #a,c
        min2 = min
        min = num

    total = total + num 
    count = count + 1 

    if num > 100: #d
        over = 1 #flag score that over 100

print("(a) The highest score is ",max," and the lowest score is ",min)
print("(b) The average score is ",total/count)
print("(c) The second highest score is ",max2)
if over == 1:
    print("(d) There is score above 100")
print("(e) average without 2 lowest score is ",(total - min - min2)/count-2)    
print(min,min2)


# Exercise 11
print('11.')
"""
Write a program that computes the factorial of a number. The factorial, n!, of a 
number n is the product of all the integers between 1 and n, including n.
"""
fac = eval(input("Enter the factorial number :"))
product = 1
for number in range(1,fac+1):
    product = number*product

print("The factorial of {} is {}.".format(fac,product))

# Exercise 12
print('12.')
"""
Write a program that asks the user to guess a random number between 1 and 10. 
If they guess right, they get 10 points added to their score, and they lose 1 point
 for an incorrect guess. Give the user five numbers to guess and print their score 
 after all the guessing is done.
"""
from random import randint
score = 0
for round in range (1,5+1):
    thenum = randint(1,10)
    ans = eval(input("Guess what number it is?"))
    print("It was {}.".format(thenum))
    if ans == thenum :
        score = score + 10
    else:
        score = score - 1
print("Goodjob! Your score is {}".format(score))



# Exercise 13
print('13.')
"""
In the last chapter there was an exercise that asked you to create a multiplication 
game for kids. Improve your program from that exercise to keep track of the number of
 right and wrong answers. At the end of the program, print a message that varies depending
   on how many questions the player got right.
"""
from random import randint
score = 0
for i in range(1,10+1):
    x = randint(1,10)
    y = randint(1,10)
    product = x*y
    ans = eval(input('What is {} x {} = '.format(x,y)))
    if ans == product:
        print('Right!')
        score = score + 1
    else:
        print('Wrong. the answer is {}'.format(product))

print("Of all 10 question you got {} right.".format(score))
if score > 8:
    print("You must be straight A student")
elif score > 5:
    print("Fairly good, at leat you still pass")
else:
    print("You better get some review")



# Exercise 14 (a)
print('14 (a).')
"""
This exercise is about the well-known Monty Hall problem. In the problem, you are a 
contestant on a game show. The host, Monty Hall, shows you three doors. Behind one 
of those doors is a prize, and behind the other two doors are goats. You pick a door. 
Monty Hall, who knows behind which door the prize lies, then opens up one of the doors 
that doesn’t contain the prize. There are now two doors left, and Monty gives you the 
opportunity to change your choice. Should you keep the same door, change doors, or does it not matter?

Write a program that simulates playing this game 10000 times and calculates what percentage of the time you would win if you switch and what percentage of the time you would win by not switching.
"""
from random import randint
Swin = 0
NSwin = 0
for round in range (10000):
    prize = randint(1,2)
    choose = randint(1,2)
    if prize == choose:
        NSwin = NSwin + 1
    else:
        Swin = Swin + 1    #since there is only a door left

Sprob = (Swin/10000)*100
NSprob = (NSwin/10000)*100
print("Win rate is as follow: Switch won {}%, Not Switch won {}%".format(Sprob,NSprob))

# Exercise 14 (b)
print('14 (b).')
"""
Try the above but with four doors instead of three. There is still only one prize, 
and Monty still opens up one door and then gives you the opportunity to switch.
"""
from random import randint
Swin = 0
NSwin = 0
for round in range (10000):
    prize = randint(1,3)
    choose = randint(1,3)
    if prize == choose:     #No switch for another 2 round
        NSwin = NSwin + 1
    else:
        choose2 = randint(1,2)
        if prize == choose2:
            Swin = Swin + 1 #swith for another 2 round     

Sprob = (Swin/10000)*100
NSprob = (NSwin/10000)*100
print("Win rate is as follow: Switch won {}%, Not Switch won {}%".format(Sprob,NSprob))

print('Unfished : 10(c,e)')