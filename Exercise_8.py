# Exercise 1
print('1.')
"""
Write a program that asks the user to enter some text and then counts how many articles are in
the text. Articles are the words 'a', 'an', and 'the'.
"""
s = input('Enter some text: ')
L = s.split()
article = [i for i in L if i in ['a','an','the'] ]

print(len(article))

# Exercise 2
print('2.')
"""
Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
"""
s = input('Enter numbers: ')
L = s.split()

s_plus = '+'.join(L)
print(s_plus)

# Exercise 3
print('3.')
"""
(a) Ask the user to enter a sentence and print out the third word of the sentence.
(b) Ask the user to enter a sentence and print out every third word of the sentence.
"""
s = input('Enter a sentence: ')
L = s.split()
print(L[2])#a

third = [L[i] for i in range(2,len(L),3)]

third_word = " ".join(third)
print(third_word)

# Exercise 4
print('4.')
"""
(a) Write a program that asks the user to enter a sentence and then randomly rearranges the
words of the sentence. Don’t worry about getting punctuation or capitalization correct.
(b) Do the above problem, but now make sure that the sentence starts with a capital, that
the original first word is not capitalized if it comes in the middle of the sentence, and
that the period is in the right place.
"""
from random import shuffle
s = input('Enter a sentence: ')
L = s.split()
shuffle(L)

rearranged = ' '.join(L)
print(rearranged)#a

from random import shuffle
s = input('Enter a sentence: ')
s = s.lower() 
L = s.split()
for i in range(len(L)):
    L[i] = L[i].replace('.','')
shuffle(L)

cleaned = ' '.join(L)
print(cleaned.capitalize()+".")#b

# Exercise 5
print('5.')
"""
Write a simple quote-of-the-day program. The program should contain a list of quotes, and
when the user runs the program, a randomly selected quote should be printed.
"""
quote = ['Talk is cheap,show me the code','Confusion is part of coding','There are two ways to write error-free program; only third one works']
from random import randint

ranq = quote[randint(0,len(quote))]
print(ranq)

# Exercise 6
print('6.')
"""
Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
"""
lotnum = [i for i in range(1,48+1)]
print(lotnum)

from random import sample
UserDrawn = sample(lotnum,6)
print(UserDrawn)

# Exercise 7
print('7.')
"""
Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs.
"""
num = [i for i in range(1,10+1)]
from random import sample
urlotto = [sample(num,6)]

dlotto = [[sample(num,6) for i in range(1000)][times] for times in range(1000)]

print(len(dlotto))

attempt = []
for loop in range(len(dlotto)):
    count = dlotto[loop].index(urlotto)
    attempt.append(count)

avgattempt = sum(attempt)/len(attempt)
print('Average of draw to get your lotto {} is {} times.'.format(''.join(urlotto),avgattempt))

# Exercise 8
print('8.')
"""
Write a program that simulates drawing names out of a hat. In this drawing, the number of
hat entries each person gets may vary. Allow the user to input a list of names and a list of
how many entries each person has in the drawing, and print out who wins the drawing.
"""
name = ['Mike','James','Paul','Simon']#eval(input('Enter list of names to draw: '))
entries = [1,3,4,8]#eval(input('Enter list of entries: '))
from random import choice
hat = [name[i] for i in range(len(name)) for j in range(entries[i])]

winner = choice(hat)
print('{} wins the hat drawing.'.format(winner))

# Exercise 9
print('9.')
"""
Write a simple quiz game that has a list of ten questions and a list of answers to those questions.
The game should give the player four randomly selected questions to answer. It should
ask the questions one-by-one, and tell the player whether they got the question right or
wrong. At the end it should print out how many out of four they got right.
"""
Q = ['What is the chemical symbol for oxygen?',
     'What is the largest island in the world?',
     'What is the smallest prime number greater than 10?',
     'What does a camel store in its hump?',
     'Which American road runs from Chicago to Los Angeles?'
     ,]
A = ['o','greenland','11','fat','route66']


from random import sample
Ask = sample(Q,4)
count = 0
for i in range(len(Ask)):
    Reply = input(Ask[i])
    ALookup = A[Q.index(Ask[i])]
    if Reply == ALookup:
        print('Exactly!')
        count = count + 1
    else:
        print('Not quite.')

print('You got {} of {} right.'.format(count,len(Ask)))

# Exercise 10
print('10.')
"""
Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the “curse” words darn, dang,
freakin, heck, and shoot.
"""
swear = ['words','darn','dang','freakin','heck','shoot']

text = input('Type some curse word: ')
text = text.split()

for i in range(len(text)):
    for j in range(len(swear)):
        if text[i] == swear[j]:
            text[i] = '*'*len(text[i])


new_text = ' '.join(text)
print(new_text)

# Exercise 11
print('11.')
"""
Section 8.3 described how to use the shuffle method to create a random anagram of a string.
Use the choice method to create a random anagram of a string.
"""
s = input('Enter a string: ')
index = [i for i in range(len(s))]

anagram = ''
from random import choice
for i in range(len(index)):
    j = choice(index)
    anagram = anagram + s[j]
    index.remove(j)

print(anagram)

# Exercise 12
print('12.')
"""
Write a program that gets a string from the user containing a potential telephone number.
The program should print Valid if it decides the phone number is a real phone number, and
Invalid otherwise. A phone number is considered valid as long as it is written in the form
abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
only numbers and dashes, and the number of digits in each group must be correct.
"""
num = '1234567890'

telvalid = input('Please enter telephone number(with -): ')
temp = telvalid.split('-')

if len(temp)not in [3,4]:
    print('group error') #check the group count
else:
    for i in range(len(temp)):
        validator = ''
        for j in temp[i]:
            if j in num:
                validator = validator + '1'
            else:
                validator = validator + '0'
        if 0 in validator:
            print('Contain non-numeric')
            break


# Exercise 13
print('13.')
"""
Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
"""
L = ['str','string','also string','another string']

M = [i[1:] for i in L]
print(M) #a

N = [len(j) for j in L]
print(N)#b

O = [k for k in L if len(k)>3]
print(O)#c

# Exercise 14
print('14.')
"""
Use a list comprehension to produce a list that consists of all palindromic numbers between
100 and 1000.
"""
from math import floor
Palindrome = [i for i in range(100,1000+1) for j in range(floor(len(str(i))/2)) if str(i)[j-1]==str(i)[-j]]
print(Palindrome)

# Exercise 15
print('15.')
"""
Use a list comprehension to create the list below, which consists of ones separated by increasingly
many zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
"""


print(L)

# Exercise 16
print('16.')
"""
Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]. Use a list comprehension to
produce a list of the gaps between consecutive entries in L. Then find the maximum gap size
and the percentage of gaps that have size 2.
"""
L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
gap = [L[i]-L[i-1] for i in range(1,len(L))]

print(max(gap)) #a

gap2 = [i for i in L if i == 2 ]
gap2_percent = len(gap2)/len(gap)*100
print('There is gap of 2 about {} %'.format(gap2_percent))

# Exercise 17
print('17.')
"""
Write a program that finds the average of all of the entries in a 4 × 4 list of integers.
"""
L = [[0]*4 for i in range(4)] #first: create the 4x4 list of 0
L = [[eval(input('Enter Number:')) for r in range(4)] for c in range(4)]

L_flatten = [item for sublist in L for item in sublist]
average = sum(L_flatten)/len(L_flatten)
print(average)

# Exercise 18
print('18.')
"""
Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the
following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column.
"""
from random import randint
L = [[randint(1,100) for row in range(10)] for c in range(10)]

from pprint import pprint
pprint(L) #a

R3_largest = max(L[2])
print('largest of third row is {}.'.format(R3_largest)) #b

C6 = [row[5] for row in L]
C6_smallest = min(C6)
print('smallest of sixth collumn is {}.'.format(C6_smallest)) #c

# Exercise 19
print('19.')
"""
Write a program that creates and prints an 8 × 8 list whose entries alternate between 1 and 2
in a checkerboard pattern, starting with 1 in the upper left corner.
"""
checkerboard = [[1 if r%2 != 1 else 2 for r in range(8)] for c in range(8)]
from pprint import pprint
pprint(checkerboard)

# Exercise 20
print('20.')
"""
Write a program that checks to see if a 4 × 4 list is a magic square. In a magic square, every
row, column, and the two diagonals add up to the same value.
"""
from random import randint
from pprint import pprint
L = [[randint(0,9) for r in range(4) ] for c in range(4)]
pprint(L)

# Exercise 21
print('21.')
"""
Write a program that asks the user to enter a length. The program should ask them what
unit the length is in and what unit they would like to convert it to. The possible units are
inches, yards, miles, millimeters, centimeters, meters, and kilometers. While this can be done
with 25 if statements, it is shorter and easier to add on to if you use a two-dimensional list of
conversions, so please use lists for this problem.
"""
Unit = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

# Exercise 22
print('22.')
"""
The following is useful as part of a program to play Battleship. Suppose you have a 5 × 5 list
that consists of zeroes and ones. Ask the user to enter a row and a column. If the entry in the
list at that row and column is a one, the program should print Hit and otherwise it should
print Miss.
"""

# Exercise 23
print('23.')
"""
This exercise is useful in creating a Memory game. Randomly generate a 6 × 6 list of assorted
characters such that there are exactly two of each character. An example is shown below.
@ 5 # A A !
5 0 b @ $ z
$ N x ! N z
0 - + # b :
- : + c c x
"""

# Exercise 24
print('24.')
"""
The following is useful in implementing computer players in a number of different games.
Write a program that creates a 5 × 5 list consisting of zeroes and ones. Your program should
then pick a random location in the list that contains a zero and change it to a one. If all the
entries are one, the program should say so.
"""

# Exercise 25
print('25.')
"""
There is only one five-digit number n that is such that every one of the following ten numbers shares exactly one digit in common in the same position as n. Find n.
"""

# Exercise 26
print('26.')
"""
(a) Write some code that translates from the left representation to the right one. The // and % operators will be useful. Be sure your code works for arrays of any size.
(b) Write some code that translates from the right representation to the left one.
"""


print('Unfinished:7 While loop?,12,15?,   19...26')
