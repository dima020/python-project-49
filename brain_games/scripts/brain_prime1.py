import random
import prompt


def prime():
    value=random.randint(1, 100)
    even='yes'
    for i in range(value-1, 2, -1): 
        if value%i==0:            
            even="no"
            break
    return value, even


def brainprime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        value, even=prime()
        print("Question:", value)
        answer = prompt.string('Your answer: ')
        if even==answer.lower():
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
        else:
            print(f"'{answer}'if given number is prime. Otherwise answer '{even}'.")
            print("Let's try again,", name, "!")
            break
