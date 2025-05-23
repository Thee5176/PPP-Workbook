print('Exercises 2.5_')

name = ('Theerapong')
print('1.')
for i in range(100):
    print(name)


print('2.')
for i in range(9):
    print(name,end='')


print('3.')
for i in range(100):
    print(i+1,name)


print('4.')
for i in range(1,21):
    print(i,i*i,sep = ' --- ')

    
print('5.')
for i in range(28):
    print(8+3*i,end = ',')
print(end='\n')


print('6.')
for i in range(50):
    print(100-2*i,end = ',')
print(end='\n')


print('7.')
for i in range(10):
    print('A',end = '')
for j in range(7):
    print('B',end = '')
for k in range(4):
    print('CD',end = '')
print('E',end = '')
for l in range(6):
    print('F',end = '')
print('G')


print('8.')
temp = input('What is your name: ')
count = eval(input('How many times it be printed: '))
for i in range(count):
    print(temp)


print('9.')
n = eval(input('How many Fibo numbers you would like: '))
a = 1
b = 0
for i in range(n):        
    c = a+b
    print(c,end = ',')
    a = b
    b = c
print(end = '\n')


print('10.')
w = eval(input('How wide the box be: '))
h = eval(input('How high the box be: '))
for i in range (h):
    print('*'*w)


print('11.')
w = eval(input('How wide the box be: '))
h = eval(input('How high the box be: '))
print('*'*w)
for i in range (h-2):
    print('*',end = '')
    for j in range (w-2):
            print(' ',end = '')
    print('*')
print('*'*w)


print('12.')
h = eval(input('How high the triangle be: '))
for i in range (1,h):
    print('*'*i+1)


print('13.')
h = eval(input('How high the triangle be: '))
for i in range (h,0,-1):
    print('*'*i)


#Exercise 14
"""
14.Use for loops to print a diamond like the one below. Allow the user to specify how high the
diamond should be.
    *
   ***
  *****
 *******
  *****
   ***
    *
"""
print('14.')
h = eval(input('How high the diamond be(odd num. only): ')) 
if h%2==1:
    blank = h//2
    for i in range(1,h+1,2):
        print(' '*blank,'*'*i)
        blank = blank - 1
        
        if i==h:
            blank = 1
            for j in range(h-2,0,-2):
                print(' '*blank,'*'*j)
                blank = blank + 1
else:
    print('Please enter odd number')


#Exercise 15    
"""
15.Write a program that prints a giant letter A like the one below. Allow the user to specify how
large the letter should be.
    *
   * *
  *****
 *     *
*       *
"""


print('15.')
h = eval(input('How high the \'A\' be(odd num. 3 or more): '))
if h>=3 and h%2==1:
    Fblank = h-1
    Mblank = -1
    for i in range(1,h+1):
        if i == 1:
            print(' '*Fblank,'*',sep='')
            #create the first dot
        elif i == h//2+1:
            print(' '*Fblank,'*'*h,sep='')
            #create the horizontal one
        elif i > 1:
            print(' '*Fblank,'*',' '*Mblank,'*',sep='')
            #create the left-right stroke
        Fblank = Fblank-1
        Mblank = Mblank+2

print('finished')
        
        
