exp = input('Enter an algebraic expression: ')

new_exp = ''
for i in range(len(exp)):
   if exp[i].isalpha() or exp[i]=='(':
      new_exp = new_exp + '*' + exp[i]
      pass
   elif exp[i] == ')':
      new_exp = new_exp + exp[i] + '*'
   else:
      new_exp = new_exp + exp[i]

print(new_exp)
