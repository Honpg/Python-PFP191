# Ex_01
def check_input(inp):
    try:
        inp = int(inp)
    except:
        print('Error, please enter numeric input')
        flag = False
    else:
        flag = True
    return flag


def computepay(H, R):
    if H > 40:
        output = (H - 40) * R * 1.5 + 40  * R
    else:
        output = H * R
    return output


Hour = input("Input hours:")
while check_input(Hour) == False:
    Hour = input('Input hours:')
    

Rate = input("Input rate:")
while check_input(Rate) == False:
    Rate = input('Input rate:')
   
print(f'Pay: {computepay(int(Hour), int(Rate))}')

#Ex_02
def compute_grade(score):
    if score <= 0.6:
        print("F")
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    elif score <= 1:
        print('A')
    else:
       print('Bad score')
    
    
score = float(input("Input your grade:"))
compute_grade(score)

# Ex_03
def checkInput(inp):
    while inp != 'done':
        try:
            inp = int(inp)
        except:
            print('Invalid input')
            inp = input('Input a number:')
        else:
            inp = input('Input a number:')
        

inp = input("Input a number:")
checkInput(inp) 
 
