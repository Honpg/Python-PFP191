import math
# Exercise 1
name = input('Enter your name: ')
print(f'Hello {name}')

#Exercise 2
Hours = float(input('Enter Hours: '))
Rate = float(input('Enter Rate: '))
print(f'Pay: {Hours * Rate}')

#Exercise 3
temperature = float(input('Input current Celsius temperature: '))
temperature = (temperature * 9 / 5 ) +32
print(f'Fahrenheit is: {temperature}')

#Exercise 4
a = int(input('Input a integer: '))
output = 0
if a % 10 == 0:
    power = int(math.log10(a) + 1)
else:
    power = math.ceil(math.log10(a))
if pow(10, power) > a:
    power -= 1
for i in range(power + 1, 0, -1):
    # run factor from 0 to 9
    if a <= 10:
        output += a
    else:
        for j in range(11, 0, -1):
            if pow(10, i - 1) * (j - 1) <= a:
                output += j - 1
                a -= pow(10, i - 1) * (j - 1)
                break
print(f'S = {output}')
