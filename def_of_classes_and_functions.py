# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:28:42 2021

@author: Михаил
"""

class Item:
    
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def get_value(self):
        return self.get_value
    
    def get_weight(self):
        return self.weight
    
class CollectionItem(Item):
    
    def __init__(self, value, weight, collection):
        Item.__init__(self, value, weight)
        self.collection = collection
        
    def get_collection(self):
        return self.collection
    
class Location:
    
    def __init__(self, level):
        self.level = level
        
    def get_level(self):
        return self.level
    
bag = []
weight_counter = 0
value_counter = 0
max_weight = 100
list_of_items = []

# Items for lvl 1 locations
glass_bottle = Item(2,1)
brick = CollectionItemItem(5, 3, 'bars')
blank_scroll = CollectionItem(1, 0, 'scholar junk')

# Items for lvl 2 locations
inkwell = CollectionItem(6, 1, 'scholar junk')
metal_goblet = CollectionItem(8, 2, 'tableware')
copper_bar = CollectionItem( , , 'bars')

# Items for lvl 3 locations
silver_fork = CollectionItem(8, 2, 'tableware')
strange_shroom = CollectionItem(, , 'strange')
bat_man_wing = CollectionItem(, , 'trophy')

# Items for lvl 4 locations
pearl = Item( , )
encrusted_silver_bracelet = Item( , )
siedge_crossbow = CollectionItem(, , 'weaponry')

# Items for lvl 5 locations
emerald = Item( , )
astrology_book = CollectionItem(, , 'scholar junk')
giant_strange_helmet = CollectionItem(, , 'strange')

# Items for lvl 6 locations
telescope = CollectionItem(, , 'scholar junk')
unicorn_horn = CollectionItem(, , 'trophy')
small_steel_anvil = Item( , )

# Items for lvl 7 locations
golden_spoon = CollectionItem(, , 'tableware')
strange_staff = CollectionItem(, , 'strange')
steel_zweihander = CollectionItem(, , 'weaponry')

# Items for lvl 8 locations
black_pearl = Item( , )
gold_bar = CollectionItemItem(, , 'bars')
giant_silver_plate = CollectionItem(, , 'tableware')

# Items for lvl 9 locations
platinum_ring = Item( , )
strange_glowing_stone = CollectionItem(, , 'strange')
irridium_bar = 

# Items for lvl 10 locations
super_alloy_dagger = CollectionItem(, , 'weaponry')
minotaur_head = CollectionItem(, , 'trophy')
golden_chest = Item( , )

def put_in_bag(item):
    item_value = item.get_value()
    item_weight = item.get_weight()
    suggested_weight = weight_counter + item_weight
    if suggested_weight < max_weight:
        value_counter += value
        weight_counter += weight
        bag.append(item)
        print('You put item in your precious bag successfully.')
    else:
        print("You can't put item in your damn bag, it's too much weight!")
