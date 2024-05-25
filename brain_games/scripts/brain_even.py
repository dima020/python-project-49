import prompt
from brain_games.cli import welcome_user,name

name=None

def parity():
   print('Answer "yes" if the number is even, otherwise answer "no".')
   for i in range(3):
         number = int(prompt.string('Question: '))
         print('Question:', number, )
         answer = prompt.string('Your answer: ')
         k='yes' if number % 2 == 0 else 'no'
         if k==answer:
            print("Correct!")
            if i==2:
                print('Congratulations,', name, '!')
         else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again,",name,"!")
            break

       
   #print('Your answer: yes' if number % 2 == 1 else 'Your answer: no')
