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
          '4 - No backtracking. '
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
    counter = 0
    for element in loot:
        counter += 1
        item_name = element.get_item_name()
        item_value = element.get_value()
        item_weight = element.get_weight()
        print(counter,')', item_name + ', ', 
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

def get_next_move():
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
              '5 - check game rules.')
        
        decision = 0
        while decision not in range(1,6):
            try:
                decision = int(input('Make your choise! '))
                if decision not in range(1,6):
                    print("You were not the smartest kid in the family, right? Type the correct number! (from 1 to 5): ")
            
            except ValueError:
                print('A NUMBER!!! ЦИФРА!!! 数字!!!')
            
                
        print('===================================================')
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
            
        # else:
        #     print('Unexpected outcome, lets try again.')

def play_location(location):
    '''
    Function plays the location for player.
    
    Parameters: location - objects of type Location
    
    Returns: None
    '''
    if location != start_l0:  
        print(location.get_text_before_loot())
        loot = location.get_items()
        display_item_props(loot)
        player_item_pick = 0
        while player_item_pick not in range(1,4):
            try:
                player_item_pick = int(input('Which item do you choose? (1, 2, 3): '))
                if player_item_pick not in range(1,4):
                    print("Type the goddamn NUMBER! (from 1 to 3): ")
            
            except ValueError:
                print('A NUMBER!!! ЦИФРА!!! 数字!!!')
                
        put_in_bag(loot.pop(player_item_pick-1))
        print('===================================================')
        print(location.get_text_after_loot())
    
    else:
        print('You see an entrance to the cave on your left and a small dilapidated '
              'cabin on your right.')
    
def go_next_location(location, player_pick):
    '''
    Function takes player pick ('r'/'l') and current location,
    then it navigate player correctly to the next location.
    
    Parameters: location - object of type Location
                player pick - string
    
    Returns: object - type Location
    '''
    next_location_level = location.get_level() + 1
    current_position = location.get_position()
   
    
    
    if current_position == 'l' and player_pick == 'l':
        adjusted_player_pick = 'l'
    elif current_position == 'm' and player_pick == 'l':
        adjusted_player_pick = 'l'
    elif current_position == 'r' and player_pick == 'l':
        adjusted_player_pick = 'm'
    elif current_position == 'l' and player_pick == 'r':
        adjusted_player_pick = 'm'
    elif current_position == 'm' and player_pick == 'r':
        adjusted_player_pick = 'r'
    else:
        adjusted_player_pick = 'r'
    
    if location.get_level() == 4: # level 5 is only middle, so NoneType errors will occur if we step in direction other then 'm'
        adjusted_player_pick = 'm'
    
    if location.get_level() == 8: # same as above
        if location == catacombs_l8:
            adjusted_player_pick = 'l'
            
        if location == spyder_caves_l8:
            adjusted_player_pick = 'r'
    
    if location.get_level() == 9: # same as above
        adjusted_player_pick = 'm'
    
    for element in list_all_locations:
        if element.get_level() == next_location_level:
            if element.get_position() == adjusted_player_pick:
                return element

def get_score(bag):
    '''
    Function calculates overall score of items in your bag
    
    Parameters: bag - list
    
    Returns: integer
    '''
    overall_score = 0
    obtained_collection_items = {'bars':0, 'scholar junk':0, 'tableware':0, 
                                 'strange':0, 'trophy':0, 'weaponry':0}
    for item in bag:
        if type(item) == CollectionItem:
            obtained_collection_items[item.get_collection()] = obtained_collection_items.get(item.get_collection()) + 1
            
    for item in bag:
        item_value = item.get_value()
        if type(item) == CollectionItem:
            if item.get_collection() == 'bars':
                value_multiplier_per_item = 2
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('bars')
            elif item.get_collection() == 'scholar junk':
                value_multiplier_per_item = 4
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('scholar junk')
            elif item.get_collection() == 'tableware':
                value_multiplier_per_item = 2
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('tableware')
            elif item.get_collection() == 'trophy':
                value_multiplier_per_item = 3
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('trophy')
            elif item.get_collection() == 'weaponry':
                value_multiplier_per_item = 2
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('weaponry')
            
            if item.get_collection() == 'strange': # all strange items have 0 value
                item_value = 800
                value_multiplier_per_item = 2
                score_for_item = item_value * value_multiplier_per_item * obtained_collection_items.get('strange')
                
        else:
             score_for_item = item_value
            
        overall_score += score_for_item
    
    return overall_score
    
# Start of the game

print('I greet you, little greedy creature. '
      'You have come with nothing but an empty '
      'bag and a desire to become rich. Let us begin!')

input_name = input('What is your name? ')
while input_name == '':
    input_name = input('Lets try again. What is your name? ')
    
nickname = ['The Filthy', "The Greedy one", 
            'The Little mouse', 'The Doomed one', 
            'The Lost', 'The Unpleasant']

random_int = random.randint(0, 5)
randomised_nickname = nickname.pop(random_int)
name = input_name + ' ' + randomised_nickname
print('From now on, you are', name + '.') # + is for dot to appear without space

location = start_l0
level = location.get_level()
game_over = False

while game_over != True:
    play_location(location)
    level += 1
    if level == 11: # Number of locations is 10
        print(get_score(bag))
        game_over = True
        break
    
    player_pick = get_next_move()
    location = go_next_location(location, player_pick)
    if location.get_level() == 6:
        player_pick = input("On the half way you started to smell a little bit of "
                            "alcohol in the air. Do you want to check the origins "
                            "of that smell? (y/n): " )
        
        if player_pick == 'y':
            print('===================================================')
            print('You picked', player_pick)
            location = inn_l6
    
    
    
















    