# Question 1
# 1.1
for i in range (1, 7):
    for h in range (1, i):
        print(h, end = ' ')
    print()
print()

# 1.2
num = int(input('Enter a number:\n'))
sum = 0
for i in range(1, num+1):
    sum += i
print(f'Sum is: {sum}')
print()

# Question 2
# 2.1
n = int(input('Enter a number of elements in a list:'))
array = []
for i in range (0,n):
    inp = int(input())
    array.append(inp)
print('Result is:')
for i in array:
    if i == 500:
        break
    elif i % 5 == 0 and i < 150:
        print(i,end = ' ')
print()

# 2.2
s = input('Enter an input:')
sum = 0
for i in s:
    if i.isdigit():
        sum += int(i)

print(f'Total digits are {sum}')
print()

# 2.3
n = int(input('Enter a number of elements in a list:'))
array = []
for i in range (0,n):
    inp = int(input())
    array.append(inp)

print('Reverse list is:')
for i in range(-1, -(len(array)+1), -1 ):
    print(array[i], end =' ')

print()


#Question 3
# 3.1
def middle_ele(s):
    if len(s) % 2 == 0:
        middle = int( len(s)/ 2 - 1 )
    else:
        middle = int( len(s) / 2 )

    return middle


s = input('Enter a string:\n')
while len(s) < 4:
    s = input('Enter more than four chars\n')

middle = middle_ele(s)
new_string = s[middle-1] + s[middle] + s[middle+1] + s[middle+2]
print(f'Original string is {s}')
print(f'Middle four chars are: {new_string}')
print()

# 3.2
s1 = input('Enter the first string:\n')
s2 = input('Enter the second string:\n')
mid_s1 = middle_ele(s1)
new_string = s1[:mid_s1+1] + s2 + s1[mid_s1+1:]
print(f'Result is {new_string}')

# 3.3
def middle_ele(s):
    if len(s) % 2 == 0:
        middle = int( len(s)/ 2 - 1 )
    else:
        middle = int( len(s) / 2 )

    return middle

def first_middle_last_string(s):
    taken_char = []
    output = ''

    for i in range(0, 2):
        # Take firs, middle and last ele of each string
        index = [0, middle_ele(s[i]), -1]
        temp_string = ''

        for j in range(0, 3):
            temp_string += (s[i][index[j]])
        taken_char.append(temp_string)

    for i in range (0,3): 
        output += taken_char[0][i] + taken_char[1][i]
    
    return output


s1 = input('Input a first string:\n')
s2 = input('Input a second string:\n')
s3 = [s1, s2]
print(f'New string is {first_middle_last_string(s3)}')

# 3.4
s = input('Enter a string:')
output = ''.join( str(i) for i in s if i.islower() )
upper = [str(i) for i in s if i.isupper()]
for i in upper:
    output += i
print(output + '\n')

# 3.5
s = input('Enter a string:\n')
chars_counter, digits_counter, symbols_counter = 0, 0, 0
for i in s:
    if i.isdigit():
        digits_counter += 1
    elif i.isalpha():
        chars_counter += 1
    else:
        symbols_counter += 1
print(f'Total counts of chars, digits and symbols')
print(f'Chars = {chars_counter} Digits = {digits_counter} Symbol = {symbols_counter}')

#Question 4
# 4.1
s = input('Enter a string:')
output = ''
for i in s:
    if i.isdigit():
        output += i
print(output)

# 4.2
s = input('Enter a string:')
output = ''
for i in s:
    if i.isalnum():
        output += i
print(output)

# 4.3
n = int(input('Enter a number of elements: '))
array = []

print('Enter elements')
for i in range(n):
    temp = input()
    array.append(temp)
print()

print(f'''Original list of strings
{array}''')
print(f'''After removing emty strings 
{[i for i in array if len(i) != 0]} ''')

# 4.4
s = input('Enter a string:\n')
s = s.split('-')
print('Display each substring:')
for i in s:
   print(i)

