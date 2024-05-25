import prompt
import random


def parity(name):
   print('Answer "yes" if the number is even, otherwise answer "no".')
   for i in range(3):
         rand=random.randint(1, 1000000)
         print('Question:', rand)
         answer = prompt.string('Your answer: ')
         k='yes' if rand % 2 == 0 else 'no'
         if k==answer:
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
         else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again,",name,"!")
            break
