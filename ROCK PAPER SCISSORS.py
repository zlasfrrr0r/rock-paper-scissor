#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randint
def computer_turn():
    threechoices = ['Rock', 'Paper', 'Scissors']
    themove = threechoices[randint(0,2)]
    return(themove)


# In[2]:


# ASSOCIATE A VALUE FOR THE INPUT
usermove = ''
def user_turn(usermove):
    while usermove not in ['rock', 'paper', 'scissors', 'Rock', 'Paper', 'Scissors']:
        usermove = input("Rock, paper or scissors? DON'T TYPE SPACES: "   )
        newusermove = usermove.capitalize()
    return newusermove


# In[3]:


def the_game(computer,user):
    if computer == user:
        print(f'The {computer} met against {user} and none shall win.')
    elif computer == 'Rock' and user == 'Paper':
        print('You engulfed the rock!')
    elif computer == 'Rock' and user == 'Scissors':
        print('The rock broke you :( ')
    elif computer == 'Paper' and user == 'Rock':
        print('The paper engulfed you  :( ')
    elif computer == 'Paper' and user == 'Scissor':
        print('You tore the paper!')
    elif computer == 'Scissors' and user == 'Paper':
        print('The scissors tore you up :(')
    else:
        print('You broke the scissors!')


# In[4]:


def play():
    
    gameon = True
    
    while gameon:
        
        thecomputer = computer_turn()

        theuser = user_turn(usermove)

        the_game(thecomputer,theuser)

        play_again = input('Another round? (yes/no):  '.lower())
        
        if play_again == 'yes':
            gameon
        if play_again == 'no':
            gameon = False
            
play()

