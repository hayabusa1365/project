import random
import time

comp_score = 0
your_score = 0

while comp_score < 3 and your_score < 3:
    # Human
    your_answ = input('Rock, paper or scissors?')
    your_answ = your_answ.lower()
    
    # Robot
    guess_num = random.randint(1, 3)
    guess = ''
    if guess_num == 1:
        guess = 'rock'
    elif guess_num == 2:
        guess = 'paper'
    else:
        guess = 'scissors'
    
    if guess == your_answ:
        comp_score += 0
        your_score += 0
    elif your_answ == 'scissors' and guess == 'paper':
        your_score += 1
    elif your_answ == 'rock' and guess == 'scissors':
        your_score += 1
    elif your_answ == 'paper' and guess == 'rock':
        your_score += 1
    else:
        comp_score += 1
    
    print('Computer: '+guess, 'You: '+your_answ)
    print('Computer score: '+str(comp_score), 'Your score: '+str(your_score))
