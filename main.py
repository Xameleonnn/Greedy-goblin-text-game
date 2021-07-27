# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 10:57:15 2021

@author: Михаил
"""
import random
from def_of_classes_and_functions import * 
'''
Initializing some values for game to work properly and for balance 
purposes. If you want to shift game balance - change next objects:
    max_weight, Items_for_lvl_x_locations
'''
bag = []
weight_counter = 0
value_counter = 0
max_weight = 100
list_of_items = []

def get_game_rules():
    '''
    Just printing our the rules
    
    Returns: None
    '''
    print('Your main goal is to get as much value from the items as possible. '
          'But remember, you cannot take more then', max_weight, 'of weight. '
          'Rules are as follows: '
          '1 - You can pick only 1 item from suggested. '
          '2 - Once obtained, you cannot throw the item away from the bag '
          'because of extreme greed that you possess. '
          '3 - Some items can be part of a collection. Gather items from '
          'one collection to get more value points at final scoring. '
          )

def put_in_bag(item):
    '''
    Function for putting the item(object) in the bag(list)
    while checking for possible overweight.
    
    Parameters: item - object of a class Item
    
    Returns: None
    '''
    item_weight = item.get_weight()
    suggested_weight = weight_counter + item_weight
    if suggested_weight < max_weight:
        bag.append(item)
        print('You put the item in your precious bag successfully.')
    else:
        print("You can't put item in your damn bag, it's too much weight!")

def display_item_props(loot):
    '''
    Function for getting all relevant properties
    of the item(object) and printing them to a player
    
    Parameters: loot - list with objects of type Item
    
    Returns: None
    '''
    for element in loot:
        item_name = element.get_item_name()
        item_value = element.get_value()
        item_weight = element.get_weight()
        print("Item's name is", item_name + ', ', 
              "it's value is", item_value, ', ', 
              "it's weight is", item_weight, '.')
    
def get_current_weight(bag):
    '''
    Function for getting current weight load
    
    Parameters: bag - list with objects of type Item
    
    Returns: int
    '''
    resulting_weight = 0
    for item in bag:
        item_weight = item.get_weight()
        resulting_weight += item_weight
    
    return resulting_weight

def process_next_move():
    '''
    Function asks for the next move. A player can choose his path through input, check 
    his inventory (which is bag[items]), check for his load and learn about gamerules.
    
    Returns: str - 'r' or 'l'
    '''
    complition = False
    while complition != True:
        print('===================================================')
        print('So,', name + ', what would you like to do? '
              '1 - go right, '
              '2 - go left, '
              '3 - check bag for items, '
              '4 - check for current weight load, '
              '5 - check game rules.'
              )
        decision = int(input('Make your choise! '))
        print('===================================================')
        print('You picked', decision)
        possible_choices = [1, 2, 3, 4, 5]
        while decision not in possible_choices:
            decision = int(input("You were not the smartest kid in the family, right? "
                                 "Type the goddamn NUMBER! (from 1 to 5): ")) # Don't be shy to show some disrespect for a greedy goblin
            print('You picked', decision)
       
        if decision == 1:
            return 'r'
        elif decision == 2:
            return 'l'
        elif decision == 3:
            if len(bag) == 0:
                print('There is nothing in the bag.')
            else:
                print('Here are some precious items in your bag:')
                display_item_props(bag)
        elif decision == 4:
            print('Current weight is', get_current_weight(bag), '. ',
                  'You can take', max_weight - get_current_weight(bag),
                  'more points of weight')
            
        elif decision == 5:
            get_game_rules()
            
        else:
            print('Unexpected outcome, lets try again.')
    
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

# Here we start a jorney

print('You see an entrance in a cave on your left and a small dilapidated cabin on your right')
player_pick = process_next_move()
# level = 0

if player_pick == 'r': # basement_l1
    print('You enter a cabin. It is dark and empty here but you notice '
          "a ladder, which leads into cabin's basement. You are going "
          "down the ladder and found yourself in a mossy dump basement. "
          "There are some items lying around. "
          'Those are not yours, but you cannot resist your kleptomania.')
    
    loot = basement_l1.get_items()
    display_item_props(loot)
    player_item_pick = int(input('Which item do you choose? (1, 2, 3): '))
    put_in_bag(loot.pop(player_item_pick-1))
    
    print('After picking the item up, you notice a hole in a wall to the right '
          'and a ladder deeper down to the left.')
    player_pick = process_next_move()
    if player_pick == 'r': # cave_l2
        # something for cave_l2
        pass
else: # cave_l1
    print("You enter a massive cave. An underground river block your way. "
          "There are some items lying just past the entrance.")
    
    loot = cave_l1.get_items()
    display_item_props(loot)
    player_item_pick = int(input('Which item do you choose? (1, 2, 3): '))
    put_in_bag(loot.pop(player_item_pick-1))
    print("You can cross the river to ford on the left, where it's not "
          "so deep or you can try to cross a wooden rotten bridge on the right")
     
    if player_pick == 'r': # cave_l2
        # again something for cave_l2, i need to think how not to repeat myself
















    