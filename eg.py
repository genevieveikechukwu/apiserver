import re

operation_type = 'can you please subtract 9 from 20 for me please?'
bad_chars = ['?', '!', '@', '.', '#', '%', '&' ',' ']', '[', '[]', ]

for i in bad_chars:
    operation_type = operation_type.replace(i, '')
# print(operation_type)
main_sentence = operation_type.split()
print(main_sentence)

# To print only a num
regex = '\d+'
match = re.findall(regex, operation_type)
print(match)
new = match
# convert to str
a = ''.join(map(str, new[0]))
b = ''. join(map(str, new[1]))
# # convert to float
x = float(a)
y = float(b)
print(x)
print(y)


operation_add = ['add', 'addition', 'increment', '+']
operation_sub = ['subtract', 'minus', 'remove', '-']
operation_multiply = ['multiply', 'multiplicattion', '*']
check1 = any(item in operation_add for item in main_sentence)
check2 = any(item in operation_sub for item in main_sentence)
check3 = any(item in operation_multiply for item in main_sentence)

result = ''
if check1 is True:
   print( x + y)
   result = 'Addition'
   print(result)
elif check2 is True:
    print( x - y)
    result = 'Subtraction'
elif check3 is True:
    result = 'Multiplication'
    print( x * y)
#     print('not available')

    