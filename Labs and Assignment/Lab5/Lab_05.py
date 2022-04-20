#Question 1
#Q1
list_1 = [1,2,3]
list_2 = [1,2,3]
list_3 = [1.0, 'Jessa', 3]
list_4 = []
list_5 = []
print(list_1, list_2, list_3, list_4, list_5)
#Q2
list_1 = ["M","na","i", "Ke"]
list_2 = ["y","me","s","lly"]
result = []
for i in range (len(list_1)):
    tmp = list_1[i] + list_2[i]
    result.append(tmp)
print(result)
print()

#Question 2
#Q1
list = []
for i in range(1,8):
    list.append(i)
for i in range(len(list)):
    list[i] = list[i]*list[i]
print(list)
#Q2 
list_1 = ['Hello','take']
list_2 = ['Dear','Sir']
result = []
for i in range (len(list_1)):
    for j in range (len(list_2)):
        tmp = ' '.join([list_1[i], list_2[j]])
        result.append(tmp)
print(result)
print()

# Question 3
#Q1
dict_1 = {'Ten':10, 'Twenty':20, 'Thirty':30,}
dict_2 = {'fourty':40, 'Fifty':50, 'Thirty':30}

print (dict_1 | dict_2)
#Q2
sample = {"class":
    {"student":
        {"name":
            "Mike",
            "marks":
                {"Physics":70,
                 "history":80}}}}

print(sample.get('class').get('student').get('marks').get('history'))    
#Q3
employees = ['Kelly', 'Emma']
defaults = {'designation':'Developer', 'salary':8000}
dict = {}
for i in range(len(employees)):
    dict[employees[i]] = defaults
print (dict)
print()

#Question 4
#Q1
tuple1 = ('Orange', [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#Q2
tuple1 = (10, 20, 30, 40)
a = tuple1[0]
b = tuple1[1]
c = tuple1[2]
d = tuple1[3]

print(a)
print(b)
print(c)
print(d)
#Q3
tuple1 = (11,22) 
tuple2 = (99,88)
tuple_tmp = tuple2
tuple2 = tuple1
tuple1 = tuple_tmp
print(tuple1, tuple2)
