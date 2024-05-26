import random
import prompt

def generate_expression(num1,num2):
    operators = ['+', '-', '*']
    operator = random.choice(operators) 
    question = f'{num1} {operator} {num2}'
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2

    return question, answer


def expression(name):
    print('What is the result of the expression?')
    for i in range(3):
        a=random.randint(1, 100)
        b=random.randint(1, 100)
        ge=generate_expression(a,b)
        print("Question:",ge[0])
        answer = int(prompt.string('Your answer: '))
        print('Your answer,', answer)          
        if ge[1]==answer:
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
        else:
            print(f"'{ge[1]}' is wrong answer ;(. Correct answer was'{ge[0]}'.")
            print("Let's try again,",name,"!")
            break


 



