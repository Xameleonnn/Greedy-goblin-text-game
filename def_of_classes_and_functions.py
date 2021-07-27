# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 16:28:42 2021

@author: Михаил
"""

class Item:
    
    def __init__(self, item_name, value, weight, level):
        self.item_name = item_name
        self.value = value
        self.weight = weight
        self.level = level
        
    def get_value(self):
        return self.value
    
    def get_weight(self):
        return self.weight
    
    def get_item_name(self):
        return self.item_name
    
    def get_level(self):
        return self.level
    
class CollectionItem(Item):
    
    def __init__(self, item_name, value, weight, level, collection):
        Item.__init__(self, item_name, value, weight, level)
        self.collection = collection
        
    def get_collection(self):
        return self.collection
    
class Location:
    
    def __init__(self, level):
        self.level = level
        self.items = get_list_of_items_lvl(level)
        
    def get_level(self):
        return self.level
    
    def get_items(self):
        return self.items

def get_list_of_items_lvl(level):
    '''
    For putting items with right item_level
    into location with it's initialization
    
    Parameters: level - integer
    
    Returns: list - list of objects which type is Item
    '''
    list_of_items_req_level = []
    for element in list_all_items:
        if element.get_level() == level:
            list_of_items_req_level.append(element)
            
    return list_of_items_req_level

# Items

# Items for lvl 1 locations
glass_bottle = Item('A botte', 2, 1, 1)
brick = CollectionItem('A brick', 5, 3, 1, 'bars')
blank_scroll = CollectionItem('A blank scroll', 1, 0, 1, 'scholar junk')

# Items for lvl 2 locations
inkwell = CollectionItem('An inkwell', 6, 1, 2, 'scholar junk')
metal_goblet = CollectionItem('A metal goblet', 8, 2, 2, 'tableware')
copper_bar = CollectionItem('Copper bar', 12, 5, 2, 'bars')

# Items for lvl 3 locations
silver_fork = CollectionItem('A silver fork', 8, 1, 3, 'tableware')
strange_shroom = CollectionItem('A strange glowing mushroom', 0, 0, 3, 'strange')
bat_man_wing = CollectionItem('Wing of a bat man', 20, 10, 3, 'trophy')

# Items for lvl 4 locations
pearl = Item('A perl', 10, 1, 4)
encrusted_silver_bracelet = Item('A silver bracelet with encrusted gems', 15, 2, 4)
siedge_crossbow = CollectionItem('A siedge crossbow', 30, 10, 4, 'weaponry')

# Items for lvl 5 locations
emerald = Item('Cut emerald', 15, 1, 5)
astrology_book = CollectionItem('A book about astrology', 20, 2, 5, 'scholar junk')
giant_strange_shroom = CollectionItem('A strange giant glowing mushroom', 0, 20, 5, 'strange')

# Items for lvl 6 locations
telescope = CollectionItem('A telescope', 40, 3, 6, 'scholar junk')
unicorn_horn = CollectionItem('A horn of a unicorn', 50, 3, 6, 'trophy')
crate_with_steel = Item('A wooden crate with a lot of steel bars in it', 250, 50, 6)

# Items for lvl 7 locations
golden_spoon = CollectionItem('A golden spoon', 35, 1, 7, 'tableware')
strange_staff = CollectionItem('A strange glowing staff', 0, 5, 7, 'strange')
steel_longsword = CollectionItem('A stell longsword', 120, 10, 7, 'weaponry')

# Items for lvl 8 locations
black_pearl = Item('A black pearl', 100, 1, 8)
gold_bar = CollectionItem('A gold bar', 250, 5, 8, 'bars')
giant_silver_plate = CollectionItem('A giant silver dish with encrusted gems', 400, 10, 8, 'tableware')

# Items for lvl 9 locations
platinum_ring = Item('A platinum ring with ruby', 150, 1, 9)
strange_glowing_stone = CollectionItem('A strange glowing stone', 0, 15, 9, 'strange')
massive_irridium_cube = CollectionItem('A massive cube made of metal irridium', 650, 50, 9, 'bars')

# Items for lvl 10 locations
titan_alloy_dagger = CollectionItem('A dagger made of unknown alloy', 500, 3, 10, 'weaponry')
minotaur_head = CollectionItem('A head of minotaur', 1000, 25, 10, 'trophy')
treasure_chest = Item('A golden chest filled with coins', 2500, 80, 10)

list_all_items = [glass_bottle, brick,blank_scroll, inkwell, metal_goblet, copper_bar, silver_fork, bat_man_wing, pearl,
                  encrusted_silver_bracelet, siedge_crossbow, emerald, astrology_book, giant_strange_shroom, telescope, 
                  unicorn_horn, crate_with_steel, golden_spoon, strange_staff, steel_longsword, black_pearl, gold_bar, 
                  giant_silver_plate, platinum_ring, strange_glowing_stone, massive_irridium_cube, titan_alloy_dagger, 
                  minotaur_head, treasure_chest]

# Locations
    
# Locations lvl 1
cave_l1 = Location(1)
basement_l1 = Location(1)

# Locations lvl 2
flooded_cave_l2 = Location(2)
cave_l2 = Location(2)
basement_l2 = Location(2)

# Location lvl 3
flooded_cave_l3 = Location(3)
antient_tomb_l3 = Location(3)
maze_l3 = Location(3)

# Location lvl 4
ravine_l4 = Location(4)
undeground_swamp_l4 = Location(4)
antient_tomb_l4 = Location(4)

# Location lvl 5
undeground_suburbs_l5 = Location(5)

# Location lvl 6
barracks_l6 = Location(6)
inn_l6 = Location(6)
temple_l6 = Location(6)

# Location lvl 7
prison_l7 = Location(7)
square_l7 = Location(7)
graveyard_l7 = Location(7)

# Location lvl 8
catacombs_l8 = Location(8)
minotaur_labyrinth_l8 = Location(8)
spyder_caves_l8 = Location(8)

# Location lvl 9
escape_tunned_l9 = Location(9)
escape_elevator_l9 = Location(9)

# Location lvl 10
dragon_test_l10 = Location(10)










