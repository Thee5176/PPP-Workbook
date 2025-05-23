print('Exercise 7.7')

# Exercise 1
print('1.')
"""
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the result.
(g) Print how many integers in the list are less than 5.
"""
L = eval(input('Enter 5 number as a list: '))
print(sum(L)) #a
print(L[-1]) #b
L.reverse()
print(L) #c
if 5 in L: #d
    print("there is a 5 in it")
else:
    print('No')

countf = L.count(5)
print('There are {} fives in the list'.format(countf)) #e

del L[0]
del L[-1]
L.sort()
print(L) #f

count = 0
for i in L :
    if i < 5:
        count = count + 1
print('There are {} integers less than 5.'.format(count)) #g


# Exercise 2
print('2.')
"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
"""
from random import randint
ran = []
for i in range(20) :
    ran.append(randint(1,100))
print(ran) #a
ranavg = sum(ran)/len(ran)
print(ranavg) #b
print('{} is largest and {} is smallest'.format(max(ran),min(ran))) #c
ran.sort()
print("""
      2 Largest:   {}
      2 Smallest:  {}
      """.format(ran[-2:],ran[:2])) #d
print('There are {} numbers in list'.format(len(ran))) #e

# Exercise 3
print('3.')
"""
Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
The final list should equal [4,5,6,25,10,17,4,5,6,10,17]
"""
L = [8,9,10]
L[1] = 17 #a
L = L + [4,5,6] #b
del L[0] #c
L.sort() #d
L = L * 2 #e
L.insert(3,25) #f
print(L)

# Exercise 4
print('4.')
"""
Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10.
"""
L = eval(input('Enter List of number between 1 to 12: ')) 
#[1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(len(L)) :
    if L[i] > 10:
        L[i] = 10     
print(L)

# Exercise 5
print('5.')
"""
Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.
"""
L = input('Enter List of strings: ')
L = L[1:-1].split(",")
for i in range(len(L)) :
    s = str(L[i])[1:]
    L[i] = s
print(L)

# Exercise 6
print('6.')
"""
Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
"""
L1 = []
for i in range(49+1):
    L1.append(i)
print(L1) #a

L2 = L1[1:] + [50]
for i in range(len(L2)):
    L2[i] = L2[i]**2
print(L2) #b

L3 = []
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alpha)):
    s = alpha[i]*(i+1)
    L3.append(s)
print(L3) #c

# Exercise 7
print('7.')
"""
Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L
and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].
"""
L = eval(input('Enter List of integers: '))
M = eval(input('Enter List of integers: '))
N = []
for i in range(len(L)):
    sum = L[i] + M[i]
    N.append(sum)
print(N)

# Exercise 8
print('8.')
"""
Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer.
"""
L = eval(input('Enter List of integers: '))
M = []
for i in L:
    factor = 1/i
    M.append(factor)
print(M)

# Exercise 9
print('9.')
"""
When playing games where you have to roll two dice, it is nice to know the odds of each
roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
17%. You can compute these mathematically, but if you don’t know the math, you can write
a program to do it. To do this, your program should simulate rolling two dice about 10,000
times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12.
"""
SS = [2,3,4,5,6,7,8,9,10,11,12]
SP = []
from random import randint
for i in range(10000):
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    sum = dice1+dice2
    SP.append(sum)

for i in SS:
    count = SP.count(i)
    chance = count/len(SP)*100
    print('{}:{}%'.format(i,round(chance,2)))    

# Exercise 10
print('10.')
"""
Write a program that rotates the elements of a list so that the element at the first index moves
to the second index, the element in the second index moves to the third index, etc., and the
element in the last index moves to the first index.
"""
L = [1,2,3,4,5,6]

for i in range(len(L)):
    L = L[1:] + [L[0]]
    print(L)


# Exercise 11
print('11.')
"""
Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
"""
L = []
for i in range(10):
    L.append(1)
    hold = [0]*i
    L = L + hold
print(L)

# Exercise 12
print('12.')
"""
Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
"""
from random import randint
L = []
for i in range(100):
    L.append(randint(0,1))

run_list = []
count = 0
for i in range(len(L)):
    if L[i]==0:
        count = count + 1
    else:
        run_list.append(count)
        count = 0
longest = max(run_list)
print('Longest run of zero is {}'.format(longest))
print(L)

# Exercise 13
print('13.')
"""
Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
"""
L = [1,1,2,3,4,3,0,0]
L_nodup = []
for i in L:
    if i not in L_nodup:
        L_nodup.append(i)
print(L_nodup)

# Exercise 14
print('14.')
"""
Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists.
"""
feet_conversion_unit = ['inches','yards','miles','millimeters','centimeters','meters','kilometers']
feet_conversion_value = [12,1/3, 0.0001893939,304.8,30.48,0.3048,0.0003048]

feet_len = eval(input('Enter Lenght in feet: '))
unit = eval(input('Which unit to convert to?'))

final_unit = feet_conversion_unit[unit-1]
final_value = feet_conversion_value[unit-1]
final_len = feet_len * final_value
print('{} feets = {} {}'.format(feet_len,final_len,final_unit))

# Exercise 15
print('15.')
"""
There is a provably unbreakable cipher called a one-time pad. The way it works is you shift
each character of the message by a random amount between 1 and 26 characters, wrapping
around the alphabet if necessary. For instance, if the current character is y and the shift is 5,
then the new character is d. Each character gets its own shift, so there needs to be as many
random shifts as there are characters in the message. As an example, suppose the user enters
secret. The program should generate a random shift between 1 and 26 for each character.
Suppose the randomly generated shifts are 1, 3, 2, 10, 8, and 2. The encrypted message would
be thebmv.
(a) Write a program that asks the user for a message and encrypts the message using the
one-time pad. First convert the string to lowercase. Any spaces and punctuation in the
string should be left unchanged. For example, Secret!!! becomes thebmv!!!
using the shifts above.
(b) Write a program to decrypt a string encrypted as above.
"""
s = input('Enter sting to encrypt: ')
one_time = []
encrypted_s = ''
alpha = 'abcdefghijklmnopqrstuvwxyz'

s = s.lower()
from random import randint
for i in s:
    one_time.append(randint(1,26))

for i in range(len(s)):
    if s[i].isalpha():
        x = alpha.index(s[i])
        x_shift = (x + one_time[i])%26

        encrypted_s = encrypted_s + alpha[x_shift]
    else:
        encrypted_s = encrypted_s + i
print(encrypted_s)#a

decrypted_s = ''

for i in range(len(encrypted_s)):
    if encrypted_s[i].isalpha():
        x = alpha.index(encrypted_s[i])
        x_shiftback = (x - one_time[i])%26
        if x_shiftback < 0:
            x_shiftback = 26 - x_shiftback
        decrypted_s = decrypted_s + alpha[x_shiftback]
    else:
        decrypted_s = decrypted_s + i
print(decrypted_s)#b
print('Finished')