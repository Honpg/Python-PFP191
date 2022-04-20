import math
# Q1
# 1.1
def func1(a, b, *c):
    print('Printing values:')
    print(a)
    print(b)
    for i in c:
        print(i)


print('Input three numbers:')
a = int(input())
b = int(input())
c = int(input())
func1(a, b, c)

print()
print()

print('Input two numbers:')
a = int(input())
b = int(input())
func1(a, b)
print()

# 1.2
def calculation(a, b):
    return a + b, a - b


print('Input two number:')
a = int(input())
b = int(input())
res = calculation(a, b)
print(res)
print()

# Q2
# 2.1
def check_use_input(name):
    if name.isdigit():
        print("It is not a name")
        return False
    else:
        return True


def showEmployee(n, *s):
    if len(s) == 0:
        print(f'Name: {n} salary: 9000')
    else:
        print(f'Name: {n} salary: {s[0]}')


name = input("Input name: ")
while check_use_input(name) == False:
    name = input('Input name: ')
salary = int(input('Input salary: '))
showEmployee(name, salary)
print()

name = input('Input name: ')
while check_use_input(name) == False:
    name = input('Input name: ')
showEmployee(name)
print()

#2.2
def inner(a, b):
    return a+b


def outer(a, b):
    result = inner(a, b)
    return result + 5


print('Input two numbers:')
a = int(input())
b = int(input())
print()

result = outer(a, b)
print(result)
print()

# Q3
# 3.1
def factorization(n):
    factor = []
    for i in range (2, int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            factor.append(i)
        while n % i == 0:
            n /= i

    if n > 1:
        factor.append(int(n))
    return factor


print('Input two integer numbers:')
a = int(input())
b =  int(input())
print(f'Common prime divisors of {a} and {b}: ')
for i in factorization(a):
    if i in factorization(b):
        print(i, end = ' ')
print()
print()

# 3.2
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)


print('Input two integer numbers')
a = int(input())
b = int(input())
print(f'GCD of them is {gcd(a, b)}')

# 3.3
lcm = int(a*b/gcd(a, b))
print(f'LCM of them is {lcm}')
print()

# Q4
# 4.1
def check_validation(n):
    if n.isdigit():
        return True
    else:
        return False


n = input('Input an integer: ')
while check_validation(n) == False:
    n = input('Re-input an integer: ')

# 4.2
def bin_convert(n):
    output = ''
    power = int(math.log(n,2) )
    #run pow from highest to 0
    for i in range(power+1, 0, -1):
        #run factor from 0 to 1
        if n <= 1 and power-1 == 0:
            output += str(n)
        else:
            for j in range(2, 0, -1):
                if pow(2, i-1)*(j-1) <= n:
                    output += str(j-1)
                    n -= pow(2, i-1)*(j-1)
                    break
    return output


bin = bin_convert(int(n))
print('N in binary base is: ')
for i in range (0, len(bin)+1, 4):
    print(bin[i : i + 4], end=' ')
print()

# 4.3
def sum_digit(n):
    output = ''
    power = int(math.log(n,10) )
    #run pow from highest to 0
    for i in range(power+1, 0, -1):
        #run factor from 9 to 0
        if n <= 1 and power-1 == 0:
            output += str(n)
        else:
            for j in range(10, 0, -1):
                if pow(10, i-1)*(j-1) <= n:
                    output += str(j-1)
                    n -= pow(10, i-1)*(j-1)
                    break
    sum = 0
    for i in range (0, len(output)):
        sum += int(output[i])
    return sum


n = int(input('Re-input an integer: '))
print(f'Sum of all digits of N is: {sum_digit(n)}')

# 4.4
def reverse(n):
    output = ''
    while n != 0 :
        output += str(n % 10)
        n = int((n - n % 10) / 10)
    return output

print(f'Reverse of N is: {reverse(n)}')
