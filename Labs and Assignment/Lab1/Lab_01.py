import math
# Q1
# 1.1
print('Input two numbers')
number1 = int(input())
number2 = int(input())
print('The result is', number1 * number2)
print()

print('Input two numbers')
number1 = int(input())
number2 = int(input())
print('The result is', number1 + number2)
print()

# 1.2
print('Printing current and previous number sum in a range (10)')
Sum = 1
for i in range(0, 10):
    if i == 0:
        print('Current Number 0 Previous Number  0  Sum:  0')
    else:
        print('Current Number', i, 'Previous Number ', i - 1, ' Sum: ', Sum)
        Sum += 2
print()

# 1.3
print("{}**{}**{}".format('Name', 'Is', 'James'))
print()

#Q2
# 2.1
#Q2
# 2.1
print('Input three integer numbers')
a = int(input())
b = int(input())
c = int(input())

octA = oct(a)
octB = oct(b)
octC = oct(c)

print('The octal number of decimal number {} is {}'.format(a, octA[2:]))
print('The octal number of decimal number {} is {}'.format(b, octB[2:]))
print('The octal number of decimal number {} is {}'.format(c, octC[2:]))
print()

#2.2
print('Input three floating-point numbers')
a = float(input())
b = float(input())
c = float(input())

print(f'{a:.2f}')
print(f'{b:.2f}')
print(f'{c:.2f}')

# Q3
# 3.4
print('Input four real numbers a,b,c and x')
a = float(input())
b = float(input())
c = float(input())
x = float(input())
print()

# 3.5
S1 = a * pow(x, 2) + b * x + c
print('S1 = {}'.format(S1))
print()

# 3.6
delta = pow(b, 2) - 4 * a * c
if delta > 0:
    S2 = math.sqrt(delta)
else:
    S2 = 0
print('S2 = {}'.format(S2))
print()

# 3.7 + 3.8
def checkTriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


print('Re-input four numbers a,b,c:')
a = float(input())
b = float(input())
c = float(input())
print()
if checkTriangle(a, b, c) == 0:
    print('a, b, c are not side of a triangle')
    print()
else:
    p = (a + b + c) / 2
    Area = pow(p * (p - a) * (p - b) * (p - c), 0.5)
    print("""
Area = {}
Perimeter = {}
""".format(Area, p * 2))
    print()

# Q4
# 4.3 + 4.4
print('Input three real numbers')
a = float(input())
b = float(input())
c = float(input())

if a > b and a > c:
    if b > c:
        print(f"""
Max is {a}
Min is {c}
Ascending order is {c} {b} {a}
""")
    else:
        print(f"""
Max is {a}
Min is {b}
Ascending order is {b} {c} {a}
""")
elif b > c and b > a:
    if a > c:
        print(f"""
Max is {b}
Min is {c}
Ascending order is {c} {a} {b}
""")
    else:
        print(f"""
Max is {b}
Min is {a}
Ascending order is {a} {c} {b}
""")
else:
    if b > a:
        print(f"""
Max is {c}
Min is {a}
Ascending order is {a} {b} {c}
""")
    else:
        print(f"""
Max is {c}
Min is {b}
Ascending order is {b} {a} {c}
""")
