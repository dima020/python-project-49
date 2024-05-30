import random
import prompt

def nod(a, b):
    min_ = min(a, b)
    for i in range(min_, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        

def game_nod(name):
    print('What is the result of the expression?')
    for i in range(3):
        a=random.randint(1, 100)
        b=random.randint(1, 100)
        rez=nod(a,b)
        print("Question:", a, b)
        answer = int(prompt.string('Your answer: '))
        print('Your answer,', answer)          
        if rez==answer:
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was'{rez}'.")
            print("Let's try again,",name,"!")
            break


 
