# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:57:15 2021

@author: Михаил
"""
import random
# from def_of_classes_and_functions import * 

print('I greet you, little greedy creature. '
      'You have come with nothing but an empty '
      'bag and desire to become rich. Let us begin!')

input_name = input('What is your name? ')
nickname = ['The filthy', "The greedy one", 
            'The little mouse', 'The doomed one', 
            'The lost', 'The unpleasant'
            ]

random_int = random.randint(0, 5)
randomised_nickname = nickname.pop(random_int)
name = input_name + ' ' + randomised_nickname
print('From now on, you are', name + '.') # + is for dot to appear without space
decision = input('Go ahead and pick your way, right or left. (r/l) ')
print(decision)
















    