#Question 1
# 1.1
import os
import datetime as dt

f = open('sales.txt','x')
f.close()
os.remove('sales.txt')

# 1.2
year = dt.datetime.now().strftime('%d-%m-%Y.txt')
year_time = dt.datetime.now().strftime('%d-%m-%Y-%H-%M-%S.txt')
dir = os.getcwd()

file_name_1 = year
file_name_2 = year_time

f1 = open(file_name_1, 'x')
f2 = open(file_name_2, 'x')

print(f'created {os.path.basename(file_name_1)}')
print(f'created {os.path.basename(file_name_2)}')
print(f'created {dir}/{file_name_2}')

f1.close()
f2.close()

os.remove(file_name_1)
os.remove(file_name_2)

# 1.3
f = open('sample.txt', 'x')
os.chmod('sample.txt', mode = 777)
os.remove('sample.txt')

# Question 2
# 2.1
import os
f = open('q2.txt','w')
f.write('Done writing\nThis is new content')
f.close()

# 2.2
f = open('q2.txt','w')
f.write('This is new content\nOpening file again...\nThis is overwritten content')
f.close()

# 2.3
list = ['Name: Emma\n','Address: 221 Baker Street\n','City: London\n']
f = open('q2.txt','w')
f.writelines(list)
f.close()

os.remove('q2.txt')

#Question 3
# 3.1
f = open('test.txt','w')
f.write('My First Line\nMy Second  Line\n')
f.close()

# 3.2
f = open('test.txt','a')
f.write("This content is added to the end of the file\n")
f.close()

# 3.3
f = open('test.txt','r')

#print 'First'
pos = f.seek(3)
print(f.read(5))

#print 'Second'
pos = f.seek(17)
print(f.read(6))
f.close()
print()

# 3.4
f = open('test.txt','rb')
f.seek(-75,2)
print(f.read(9).decode())

f.seek(-72,2)
print(f.read(10).decode())
f.close()
print()

# 3.5
f = open('test.txt','rb+')
f.seek(75)
print(f'file handle at: {f.tell()}')

f.seek(0,2)
f.write('Demonstrating tell \n'.encode('UTF-8'))
print(f'file handle at: {f.tell()}')

f.seek(0)
print(f'file handle at: {f.tell()}')

print()
print('***Printing file content***')
line = f.readlines()
for i in line:
    print(i.decode().strip())
print('***Done***')
print(f'file handle at: {f.tell()}')
f.close()

os.remove('test.txt')

#Question 4
# 4.1
print()
import os
import datetime as dt

old_name = 'detail.txt'
open('detail.txt','x') # file creation

new_name = 'new_detail.txt'
open('new_detail.txt','x') # file creation

#check file existence
if os.path.isfile(new_name):
    print('File has already existed')
else:
    os.rename(old_name, new_name)

os.remove(old_name)
os.remove(new_name)

# 4.2
print()
open('sales1.txt','x')
open('sales2.txt','x')

files = os.listdir() # enumerate all files in current dir
for i in range(3,len(files)):
    new_name = '_'.join([files[i][:5],files[i][-5:]]) # sales1.txt -> sales_1.txt
    os.rename(files[i], new_name)
print('All Files Renamed\nNew Names are')
print(os.listdir()[3:])

# 4.3
print()
files = os.listdir()
new_name = '_new'.join([files[3][:7], files[3][-4:]])
os.rename(files[3], new_name)
print(os.listdir()[3:])

# 4.4
print()
year_time = dt.datetime.now().strftime("%d-%b-%Y.txt")
file_name = ''.join(['sales',year_time])
open (file_name,'x')
print(os.listdir()[3:])
print()

# 4.5
for i in os.listdir()[3:]:
    tmp = i.split('.')
    new_ext = '.'.join([tmp[0], tmp[1].replace('txt','pdf')])
    os.rename(i, new_ext )
    
print(os.listdir())
os.remove('sales04-Mar-2022.pdf')
os.remove('sales_1_new.pdf')
os.remove('sales_2.pdf')


