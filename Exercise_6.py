print('Exercise 6.11')

# Exercise 1
print('1.')
"""
Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every 'a' replaced with 'e'
(k) The string with every letter replaced by a space
"""
text = input('Enter something :')
#a
print(len(text))
#b
print(text*10)
#c
print(text[0])
#d
print(text[:2])
#e
print(text[-3:])
#f
print(text[::-1])
#g
if len(text) >= 7:
    print(text[:6])
else:
    print("Shorter than 7")
#h
print(text[1:-2])
#i
print(text.upper())
#j
for c in text:
   if c=='a':
     print('e',end='')
   else:
       print(c,end='')
print("\n")
#k
for c in text:
   if c.isalpha():
     print(' ',end='')


# Exercise 2
print('2.')
"""
A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.
"""
sen = input('Type one sentence :')
count = 1
for c in sen:
   if c==' ':
      count = count + 1

print('There are {} words in your typing.'.format(count))

# Exercise 3
print('3.')
"""
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the same number of opening
and closing parentheses.
"""
F = input('Enter a parenthesis formula')
Copen = 0
Cclose = 0
for c in F:
   if c == "(":
      Copen = Copen + 1
   if c == ")":
      Cclose = Cclose + 1

if Copen == Cclose:
   print("It seems to parenthesis right")
else:
   print("You got the parenthesis wrong")

# Exercise 4
print('4.')
"""
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""
text = input('Enter a word :')
flag = 0
for c in text:
   if c in "aeiou":
      flag = 1
      break
 
if flag == 1:
   print("Vowel Founded!")
else:
   print("There is no vowel.")

# Exercise 5
print('5.')
"""
Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string.
"""
org_string = input('Type a word :')
new_string = org_string[0] + '*' + org_string[2:] + "!!!"

print(new_string)

# Exercise 6
print('6.')
"""
Write a program that asks the user to enter a string s and then converts s to lowercase, removes
all the periods and commas from s, and prints the resulting string.
"""
s = input('Type a sentence with periods and commas :')
s = s.lower()

for c in s:
   if c in ',.':
      s = s.replace(c,'')

print(s)

# Exercise 7
print('7.')
"""
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
"""
s = input('Type to check if palindrome or not :')

if s == s[::-1]:
   print('Yep, it is')
else: 
   print('Nope not this one')
   
# Exercise 8
print('8.')
"""
At a certain school, student email addresses end with @student.college.edu, while professor
email addresses end with @prof.college.edu. Write a program that first asks the
user how many email addresses they will be entering, and then has the user enter those addresses.
After all the email addresses are entered, the program should print out a message
indicating either that all the addresses are student addresses or that there were some professor
addresses entered.
"""
n = eval(input('How many email addresses are there?'))
prof = 0
stud = 0
for i in range(n):
   emails = input('Type in your email address')
   if '@prof.college.edu' in emails:
      prof = 1
   if '@student.college.edu':
      stud = 1

if prof == 1 and stud == 1 :
   print('There is professor email address')
elif stud == 1:
   print('There are all student email address')   
else:
   print('There is no institution email')

# Exercise 9
print('9.')
"""
Ask the user for a number and then print the following, where the pattern ends at the number
that the user enters.
1
    2
       3
          4
"""
n = eval(input('Enter a number: '))
for i in range(n):
   print("  "*i,end = '')
   print(i+1)

# Exercise 10
print('10.')
"""
Write a program that asks the user to enter a string, then prints out each letter of the string
doubled and on a separate line.
"""
text = input('Enter a word :')
for c in range(len(text)):
   print(text[c]*2)

# Exercise 11
print('11.')
"""
Write a program that asks the user for a word that contains the letter 'a'. The program
should then print the following two lines: On the first line should be the part of the string up
to and including the first 'a', and on the second line should be the rest of the string.
"""
text = input('Enter a word with many \'a\'s in it :')
for c in range(len(str)):
   if str[c] == 'a':
      print(str[:c+1])
      print(str[c+1:])
      

# Exercise 12
print('12.')
"""
Write a program that asks the user to enter a word and then capitalizes every other letter of
that word. So if the user enters 'rhinoceros', the program should print 'rHiNoCeRoS'.
"""
text = input('Enter a word :')
s = ''
for c in range(len(text)):
   if c%2 == 0:
      s = s + text[c].upper()
   else:
      s = s + text[c]

print(s)

# Exercise 13
print('13.')
"""
Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings.
"""
text1 = input('Enter a word :')
text2 = input('Enter the same lenght word :')
s = ''

if len(text1)==len(text2):
   for c in range(len(text1)):
      s = s + text1[c] + text2[c]
   print(s)
else:
   print("Not the same length")


# Exercise 14
print('14.')
"""
Write a program that asks the user to enter their name in lowercase and then capitalizes the
first letter of each word of their name.
"""
name = input('Enter your name :')
print(name.capitalize())

# Exercise 15
print('15.')
"""
When I was a kid, we used to play this game called Mad Libs. The way it worked was a friend
would ask me for some words and then insert those words into a story at specific places
and read the story. The story would often turn out to be pretty funny with the words I had
given since I had no idea what the story was about. The words were usually from a specific
category, like a place, an animal, etc.

Write a Mad Libs program. It should prompt the user for various types of words (e.g., a
noun, a verb, an adverb, etc.) and then insert those words into a story at specific places.
Finally, print the full story with the inserted words.
"""
Disaster = input('Enter Disaster: ')
City = input('Enter City name: ')
Play = input('Enter a child play: ')

print("There was a {} when we went to {} for the field trip. So we decided to play {}.".format(Disaster,City,Play))

# Exercise 16
print('16.')
"""
Write a program that generates the 26-line block of letters.
"""
alpha = 'abcdefghijklmnopqrstuvwxyz'

for c in range(len(alpha)):
   s = ''
   for ch in range(len(alpha)):
      ch = (c + ch)%26
      s = s + alpha[ch]
   print(s + '\n')

# Exercise 16.5
print('16.5.')
"""
Companies often try to personalize their offers to make them more attractive. One simple
way to do this is just to insert the person’s name at various places in the offer. Of course,
companies don’t manually type in every person’s name; everything is computer-generated.
Write a program that asks the user for their name and then generates an offer like the one
below.
"""
s = input('Enter Name: ')

name = s[:s.index(' ')]

print("""
I am pleased to offer you our new Platinum Plus Rewards card
at a special introductory APR of 47.99%. {}, an offer
like this does not come along every day, so I urge you to call
now toll-free at 1-800-314-1592. We cannot offer such a low
rate for long, {}, so call right away.""".format(name,name))

# Exercise 17
print('17.')
"""
The goal of this exercise is to see if you can mimic the behavior of the in operator and the
count and index methods using only variables, for loops, and if statements.
(a) Without using the in operator, write a program that asks the user for a string and a letter
and prints out whether or not the letter appears in the string.
(b) Without using the count method, write a program that asks the user for a string and a
letter and counts how many occurrences there are of the letter in the string.
(c) Without using the index method, write a program that asks the user for a string and
a letter and prints out the index of the first occurrence of the letter in the string. If the
letter is not in the string, the program should say so.
"""
print('(a)')
s = input('Enter string')
c = input('Which character to find?')
flag = 0
for i in s:
   if i == c:
      flag = 1

if flag == 1 :
   print('Found it!')
else:
   print('Not Found.')

print('(b)')
s = input('Enter string')
c = input('Which character to search for?')
for i in s :
   count = 0
   if i == c:
      count = count + 1
print('There are {} {}'.format(count,c))

print('(c)')
s = input('Enter string')
c = input('Which character to search for?')
count = 0
for i in s :
   count = count + 1
   if i == c:
      print('Index for {} is {}'.format(c,count))


# Exercise 18
print('18.')
"""
Write a program that asks the user for a large integer and inserts commas into it according
to the standard American convention for commas in large numbers.
"""
num = input('Enter large number :')
new_num = ''
for i in range(len(num)):
   if (len(num)-i-1)%3  == 0 and i != len(num)-1 :
      new_num = new_num + num[i] +','
   else:
      new_num =  new_num +num[i]
print(new_num)

# Exercise 19
print('19.')
"""
Write a program that converts a time from one time zone to another. The user enters the time
in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
is that of the original time and the second is the desired time zone.
"""
t = input('Time: (am/pm)')
szone = input('Starting zone: ')
ezone = input('Ending zone: ')

t = t.lower()
timezone = "ECMP"

hour = t[:t.index(':')]
if hour.isnumeric():                          # Check if time is number
   if szone[0] and ezone[0] in timezone : # Validate time zone
      start = timezone.index(szone[0])
      end = timezone.index(ezone[0])
      new_hour = int(hour) + (start-end)       # Convert hour to new time zone
      if new_hour > 12:                   # Convert time round the clock
         new_hour = new_hour%12
         if 'am' in t :
            t = t.replace('am','pm')
         elif 'pm' in t :
            t = t.replace('pm','am')
         else:
            print("Error am/pm not found")
   else:
      print('Error timezone Not Found')
else:
   print('Data Type Error')

new_t = str(new_hour) + t[t.index(':'):]
print(new_t)

# Exercise 20
print('20.')
"""
Write a program that returns a random anagram of a string—in other words, a random rearrangement of the
letters of that string.
"""


# Exercise 21
print('21.')
"""
A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
characters is to pick out the characters at even indices, put them first in the encrypted string,
and follow them by the odd characters. For example, the string message would be encrypted
as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd
characters are e, s, g (at indices 1, 3, and 5).
(a) Write a program that asks the user for a string and uses a method to encrypt the string.
(b) Write a decryption program for the encryption method in part (a).
"""
print('(a)')
s = input('Enter string: ')

evenstr = ''
oddstr = ''
for i in range(len(s)):
   if i%2 == 0:
      evenstr = evenstr + s[i]
   else:
      oddstr = oddstr + s[i]
enc_s = evenstr + oddstr
print('Encrypted: '+ enc_s)

print('(b)')
import math
sepindex = math.ceil(len(enc_s)/2)              # find the first index of oddstr
oddenc = enc_s[sepindex:]
evenenc = enc_s[:sepindex]

dec_s = ''
for i in range(min(len(oddenc),len(evenenc))) : # shuffle 1 by 1 back in
   dec_s += evenenc[i]
   dec_s += oddenc[i]
if len(dec_s) != len(enc_s):                    # 1 character extra for odd lenght string
   dec_s += evenenc[-1]

print(dec_s)

# Exercise 22
print('22.')
"""
A more general version of the above technique is the rail fence cipher, where instead of breaking
things into evens and odds, they are broken up by threes, fours or something larger. For
instance, in the case of threes, the string secret message would be broken into three groups. The
first group is sr sg, the characters at indices 0, 3, 6, 9 and 12. The second group is eemse, the
characters at indices 1, 4, 7, 10, and 13. The last group is ctea, the characters at indices 2, 5, 8,
and 11. The encrypted message is sr sgeemsectea.

(a) Write a program the asks the user for a string and uses the rail fence cipher in the threes
case to encrypt the string.
(b) Write a decryption program for the threes case.
(c) Write a program that asks the user for a string, and an integer determining whether to
break things up by threes, fours, or whatever. Encrypt the string using the rail-fence
cipher.
(d) Write a decryption program for the general case.
"""
s =  input('Enter string to encrypt: ')

oneth = s[0::3]
twoth = s[1::3]
threeth = s[2::3]
enc = oneth + twoth + threeth
print('(a):',enc)



# Exercise 23
print('23.')
"""
In calculus, the derivative of x^4 is 4x^3. The derivative of x^5 is 5x^4. The derivative of x^6 is
6x^5. This pattern continues. Write a program that asks the user for input like x^3 or x^25
and prints the derivative.
"""
q = input('Find derivative of powered of x: ')

pownum = q[q.index('^')+1:]
if pownum.isnumeric():
   cof = int(pownum)
   new_pownum = cof - 1
   diffq = str(cof) + q[:q.index('^')+1] + str(new_pownum)
   print(diffq)
else:
   print('Powered Number Error')


# Exercise 24
print('24.')
"""
In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or 3(x+5).
Write a program that asks the user for an algebraic expression and then inserts multiplication
symbols where appropriate.
"""
exp = input('Enter an algebraic expression: ')

new_exp = ''
for i in range(len(exp)):
   if exp[i].isalpha() or exp[i]=='(':
      new_exp = new_exp + '*' + exp[i]
   elif exp[i] == ')' and exp[i].isnumeric():
      new_exp = new_exp + exp[i] + '*'
   else:
      new_exp = new_exp + exp[i]

print(new_exp)


print('Unfinished : 20,22(b,c,d)') #Deadline: 5/5/2024