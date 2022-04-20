# Exercise 1
f = open('Ex_03.txt','w')
inp = input("Enter data\n")

while inp != 'Done':
    if inp != 'Done':
        f.write(inp+'\n')
    inp = input()

print('''The file has been created successfully.
------------------------
This is file's content:''')
f.close()

f = open('Ex_03.txt','r')
print(f.read())
f.close()

# Exercise 2
f = open('Romeo.txt')
line = f.readline().strip()
output = []
while line !='':
    word = line.split(' ')
    for i in word:
        if i not in output:
            output.append(i)
    line = f.readline().strip()
print(sorted(output))
f.close()

