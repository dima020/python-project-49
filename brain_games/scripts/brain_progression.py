import random
import prompt


def progression():
    len_=random.randint(5, 14)
    index_=random.randint(1, len_-1)
    x1=random.randint(1, 20)
    step=random.randint(1, 5)
    progression = [x1 + step * i for i in range(len_-1)] 
    hidden_value =progression[index_]
    progression[index_] = ".."
    return progression,hidden_value 


def brainprogression(name):
    print('What number is missing in the progression?')
    for i in range(3):
        progression1,rez=progression()
        print("Question:", progression1)
        answer = int(prompt.string('Your answer: '))   
        if rez==answer:
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was'{rez}'.")
            print("Let's try again,", name,"!")
            break
