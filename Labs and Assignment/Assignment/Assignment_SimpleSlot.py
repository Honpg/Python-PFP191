import random as rd

def play(balance):
    a = rd.randrange(0,10)
    b = rd.randrange(0,10)
    c = rd.randrange(0,10)
    if a == b == c:
        balance += 10.0
        sum = str(a) + str(b) + str(c)            
        print(f'The slot machine show {sum}.')
        print(f'You win the big prize, $10!')
        print(f'You have ${balance}.')
    elif a == b or a == c or b ==c:
        balance += 0.5
        sum = str(a) + str(b) + str(c)
        print(f'The slot machine show {sum}.')
        print('You win 50 cents!')
        print(f'You have ${balance}.')
    else:
        balance -= 0.25
        sum = str(a) + str(b)+ str(c)
        print(f'The slot machine show {sum}.')
        print("Sorry you don't win anything.")
        print(f'You have ${balance}.')
    return balance

def save():
    print('Your money have saved')
    
def end(balance):
    print(f'Thank you for your playing! You end with ${balance}!')

if __name__ == "__main__":
    balance = 10.00
    print(f'You have ${balance}')
    choice = input("""Choose one of the following menu options:
1) Play the slot machine
2) Save Game
3) Cash out
""")

    while int(choice) in range(1,4):
        if choice == '1':
            if balance == 0.0:
                print('You have no money left')
                break
            else:       
                balance = play(balance)
        elif choice == '2':
            save()
        else:
            end(balance)
            break   
        choice = input("""Choose one of the following menu options:
1) Play the slot machine
2) Save Game
3) Cash out
""")



