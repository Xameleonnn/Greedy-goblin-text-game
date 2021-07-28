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
    
    def __init__(self, level, position):
        self.level = level
        self.position = position
        self.items = get_list_of_items_lvl(level)
        self.text_before_loot = ''
        self.text_after_loot = ''
        
    
    def set_text_after_loot(self, text):
        self.text_after_loot = text
    
    def set_text_before_loot(self, text):
        self.text_before_loot = text
    
    def get_text_after_loot(self):
        return self.text_after_loot
    
    def get_text_before_loot(self):
        return self.text_before_loot
    
    def get_level(self):
        return self.level
    
    def get_items(self):
        return self.items
    
    def get_position(self):
        return self.position
    
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

list_all_items = [glass_bottle, brick,blank_scroll, inkwell, metal_goblet, copper_bar, silver_fork, strange_shroom, 
                  bat_man_wing, pearl, encrusted_silver_bracelet, siedge_crossbow, emerald, astrology_book, 
                  giant_strange_shroom, telescope, unicorn_horn, crate_with_steel, golden_spoon, strange_staff, 
                  steel_longsword, black_pearl, gold_bar, giant_silver_plate, platinum_ring, strange_glowing_stone, 
                  massive_irridium_cube, titan_alloy_dagger, minotaur_head, treasure_chest]


# Locations


# Location lvl 0
start_l0 = Location(0, 'm')

# Locations lvl 1
cave_l1 = Location(1, 'l')
basement_l1 = Location(1, 'r')

# Locations lvl 2
flooded_cave_l2 = Location(2, 'l')
cave_l2 = Location(2, 'm')
basement_l2 = Location(2, 'r')

# Location lvl 3
flooded_cave_l3 = Location(3, 'l')
antient_tomb_l3 = Location(3, 'm')
maze_l3 = Location(3, 'r')

# Locations lvl 4
ravine_l4 = Location(4, 'l')
undeground_swamp_l4 = Location(4, 'm')
antient_tomb_l4 = Location(4, 'r')

# Location lvl 5
undeground_suburbs_l5 = Location(5, 'm')

# Locations lvl 6
barracks_l6 = Location(6, 'l')
inn_l6 = Location(6, 'm')
temple_l6 = Location(6, 'r')

# Locations lvl 7
prison_l7 = Location(7, 'l')
square_l7 = Location(7, 'm')
graveyard_l7 = Location(7, 'r')

# Locations lvl 8
catacombs_l8 = Location(8, 'l')
minotaur_labyrinth_l8 = Location(8, 'm')
spyder_caves_l8 = Location(8, 'r')

# Locations lvl 9
escape_tunned_l9 = Location(9, 'l')
escape_elevator_l9 = Location(9, 'r')

# Location lvl 10
dragon_test_l10 = Location(10, 'm')

list_all_locations = [start_l0, cave_l1, basement_l1, flooded_cave_l2, cave_l2, basement_l2, flooded_cave_l3, antient_tomb_l3,
                      maze_l3, ravine_l4, undeground_swamp_l4, antient_tomb_l4, undeground_suburbs_l5, barracks_l6, inn_l6,
                      temple_l6, prison_l7, square_l7, graveyard_l7, catacombs_l8, minotaur_labyrinth_l8, spyder_caves_l8,
                      escape_tunned_l9, escape_elevator_l9, dragon_test_l10]

# Texts for locations

# blueprint for setters
# .set_text_before_loot(_text_before_loot) 
# .set_text_after_loot(_text_after_loot)

# Locations lvl 1
cave_l1_text_before_loot = ("You enter a massive cave. An underground river block your way. "
                            "There are some items lying just past the entrance.")

cave_l1_text_after_loot = ("You can cross the river to ford on the left, where it's not so "
                           "deep or you can try to cross a wooden rotten bridge on the right")

basement_l1_text_before_loot = ("You enter a cabin. It is dark and empty here but you notice "
                                "a ladder, which leads into cabin's basement. You are going "
                                "down the ladder and found yourself in a mossy dump basement. "
                                "There are some items lying around. "
                                "Those are not yours, but you cannot resist your kleptomania.")

basement_l1_text_after_loot = ("After picking the item up, you notice a hole in a wall to the "
                               "left and a ladder deeper down to the right.")

cave_l1.set_text_before_loot(cave_l1_text_before_loot)
cave_l1.set_text_after_loot(cave_l1_text_after_loot)
basement_l1.set_text_before_loot(basement_l1_text_before_loot)
basement_l1.set_text_after_loot(basement_l1_text_after_loot)
    
# Locations lvl 2
flooded_cave_l2_text_before_loot = ("After crossing a river, you feel a little bit wet. Cold "
                                    "air and screeching noizes are your only company on the "
                                    "way down in deeper caves. Finily after some time, you "
                                    "find yourself in big open space. It seems like the lower "
                                    "levels of caves were flooded, it's water all over the floor!"
                                    "You can spot some items in the shallow water! Grab them quick!")

flooded_cave_l2_text_after_loot = ("You spot a little entrance in a deeper levels of the cave on "
                                   "your right. A lot of sculls and images of dead are masterfully "
                                   "engraved on the wall next to entrance. On the other hand, you can "
                                   "go to the left to explore shallow waters of lower caves. ")

cave_l2_text_before_loot = ("Although the bridge was screaming udred your weight, you successfully "
                            "got on the other side. That cave is indeed a huge one! You quickly "
                            "spotted a couple of items next to a skeleton of a human. It seems "
                            "like poor soul fell from height and was impaled by a stalagmite. "
                            "Or someone helped him be impaled...")

cave_l2_text_after_loot = ("After grabbing an item, you carefully plan where to go next. You can turn "
                           "to the left and dive deep in lover caves. But on your right there is an "
                           "entrance with a bull head above it. You wonder what it has to do with "
                           "that place?")

basement_l2_text_before_loot = ("The ladder was surprisingly long. You lost feel of time while heading "
                                "lower and lower down. But, finally, you touched the ground by your feet. "
                                "There is a chest in the room, lets see what is inside!")

basement_l2_text_after_loot = ("It is great time for planning the next move! And you definitly need planning "
                               "because you found yourself between 2 hallways. You feel an eternum grief when "
                               "looking in the hallway on the left, and a painful fear, when looking in the "
                               "hallway on the right.")

flooded_cave_l2.set_text_before_loot(flooded_cave_l2_text_before_loot) 
flooded_cave_l2.set_text_after_loot(flooded_cave_l2_text_after_loot)
cave_l2.set_text_before_loot(cave_l2_text_before_loot) 
cave_l2.set_text_after_loot(cave_l2_text_after_loot)
basement_l2.set_text_before_loot(basement_l2_text_before_loot) 
basement_l2.set_text_after_loot(basement_l2_text_after_loot)

# Location lvl 3
flooded_cave_l3_text_before_loot = ("It was 3 or maybe more hours of constant descending lower. Little stream at the "
                                    "start of a tunnel became a full underground river. Finally, you found yourself "
                                    "in a huge open space. Just before you is a lake... no, a whole underground sea! "
                                    "The water here is extremely transparent. You came closer to the shore and found "
                                    "a couple items here!")

flooded_cave_l3_text_after_loot = ("While grabbing an item, you spotted a boat! You quickly jumped inside and started "
                                   "to sail throung the deep water. With every motion of your paddles, the echo spread "
                                   "for miles around. After some time, you reached the shore. You can head to the right "
                                   "or to the left.")

antient_tomb_l3_text_before_loot = ("Thousends upon thousends of tombstones fill this giant room. You walk through "
                                    "them and feel like somebody is watching. With every second you feel that more "
                                    "and more eyes are wathching you. Sweating cold, you start running fast, untill you "
                                    "stumble over something and hit a gravestone with you head. You passed out. Gods "
                                    "know how much time you've been here unconscious. When you came to your senses, "
                                    "you found yourself in a shallow deepening filled with graves. There are some "
                                    "items next to them!")

antient_tomb_l3_text_after_loot = ("Stealing from the dead, what have you become? Anyway, after taking "
                                   "an item, you looked around for an exit from this horrible place. "
                                   "You see just ahead of you a crack in the wall on the left, which "
                                   "leads to a huge open space, but you can't quite see anything "
                                   "there. The room is turning to the right, and it seems like graveyard "
                                   "is not about to end there")

maze_l3_text_before_loot = ("'Brace yourself! You have entered the MAZE!' That is what was carved at the entrance. "
                            "After long hours of wakling, you almost feel like you are going to die here. Turn "
                            "after turn, madness starts to fill you. But then, suddenly, you see a room. Some "
                            "corpses lying here and there, but more importantly - some items! Dead will not need "
                            "them here anyway...")

maze_l3_text_after_loot = ("After grabbing an item, you see 2 paths that lead from a maze. One on the right "
                           "smells like antient corpse. One on the left is absolutely the same, but with a little "
                           "bit of rot. Unpleasant choice...")

flooded_cave_l3.set_text_before_loot(flooded_cave_l3_text_before_loot) 
flooded_cave_l3.set_text_after_loot(flooded_cave_l3_text_after_loot)
antient_tomb_l3.set_text_before_loot(antient_tomb_l3_text_before_loot) 
antient_tomb_l3.set_text_after_loot(antient_tomb_l3_text_after_loot)
maze_l3.set_text_before_loot(maze_l3_text_before_loot) 
maze_l3.set_text_after_loot(maze_l3_text_after_loot)

# Locations lvl 4
ravine_l4_text_before_loot = ("Finally, a fresh air! You put your head up and see a sky! It is so high up. What is "
                              "far more displeasing, however, is that the only way further is blocked by a huge "
                              "ravine. You search for a way through that and accidentally found a hidden stash. Lets "
                              "see what is inside!")

ravine_l4_text_after_loot = ("After grabbing an item, you continue your search and soon you see 2 paths down. "
                             "Which one you take?")

undeground_swamp_l4_text_before_loot = ("That smell. Smell of decay. It's definitely a swamp, but what is it doing "
                                        "down here? Navigating through that might be a challenge, but there is no "
                                        "other way. Wielding a long stick, you are trying to cross this gods-forgotten "
                                        "place. After long exhausting advance, you found a little island with a tent. "
                                        "There are some items in it! What a surprise!")

undeground_swamp_l4_text_after_loot = ("Nice and easy, after getting an item you continue your advance. Suddenly, ground "
                                       "become firm and dry. What a relief. You turn you head around in hope to find a way. "
                                       "Fortunately, you found 2! Which one you take, the left or the right?")

antient_tomb_l4_text_before_loot = ("A giant tombstones. It is surprising how they ended up there. Standing 15 meters tall, "
                                    "a single stone could weight probably 200 tons or more! And there are hundreds... "
                                    "No, thousands of them around! Being incredibly massive, they are fully covered in runes. "
                                    "You decided to quit staring and hurry through this strange place. After a while, you "
                                    "see a square made of stone and a pillar in center. Just under it there are some items. "
                                    "Quickly, grab them!")

antient_tomb_l4_text_after_loot = ("Right after you took an item, the pillar started to slide down into the ground with a lot "
                                   "of noise. You tried to run away, but your legs were paralyzed and they wouldn't move an inch. "
                                   "Suddenly a bright flash of light blinded you and you fell. After some time, the ability to "
                                   "see came back. You were standing in a closed room with 2 ways out - one to the right and "
                                   "one to the left. ")

ravine_l4.set_text_before_loot(ravine_l4_text_before_loot) 
ravine_l4.set_text_after_loot(ravine_l4_text_after_loot)
undeground_swamp_l4.set_text_before_loot(undeground_swamp_l4_text_before_loot) 
undeground_swamp_l4.set_text_after_loot(undeground_swamp_l4_text_after_loot)
antient_tomb_l4.set_text_before_loot(antient_tomb_l4_text_before_loot) 
antient_tomb_l4.set_text_after_loot(antient_tomb_l4_text_after_loot)

# Location lvl 5
undeground_suburbs_l5_text_before_loot = ("bt us5")
undeground_suburbs_l5_text_after_loot = ("at us5")

undeground_suburbs_l5.set_text_before_loot(undeground_suburbs_l5_text_before_loot) 
undeground_suburbs_l5.set_text_after_loot(undeground_suburbs_l5_text_after_loot)

# Locations lvl 6
barracks_l6_text_before_loot = ("bt6")
barracks_l6_text_after_loot = ("at6")
inn_l6_text_before_loot = ("bt6")
inn_l6_text_after_loot = ("at6")
temple_l6_text_before_loot = ("bt6")
temple_l6_text_after_loot = ("at6")

barracks_l6.set_text_before_loot(barracks_l6_text_before_loot) 
barracks_l6.set_text_after_loot(barracks_l6_text_after_loot)
inn_l6.set_text_before_loot(inn_l6_text_before_loot) 
inn_l6.set_text_after_loot(inn_l6_text_after_loot)
temple_l6.set_text_before_loot(temple_l6_text_before_loot) 
temple_l6.set_text_after_loot(temple_l6_text_after_loot)

# Locations lvl 7
prison_l7_text_before_loot = ("bt7")
prison_l7_text_after_loot = ("at7")
square_l7_text_before_loot = ("bt7")
square_l7_text_after_loot = ("at7")
graveyard_l7_text_before_loot = ("bt7")
graveyard_l7_text_after_loot = ("at7")

prison_l7.set_text_before_loot(prison_l7_text_before_loot) 
prison_l7.set_text_after_loot(prison_l7_text_after_loot)
square_l7.set_text_before_loot(square_l7_text_before_loot) 
square_l7.set_text_after_loot(square_l7_text_after_loot)
graveyard_l7.set_text_before_loot(graveyard_l7_text_before_loot) 
graveyard_l7.set_text_after_loot(graveyard_l7_text_after_loot)

# Locations lvl 8
catacombs_l8_text_before_loot = ("bt8")
catacombs_l8_text_after_loot = ("at8")
minotaur_labyrinth_l8_text_before_loot = ("bt8")
minotaur_labyrinth_l8_text_after_loot = ("at8")
spyder_caves_l8_text_before_loot = ("bt8")
spyder_caves_l8_text_after_loot = ("at8")

catacombs_l8.set_text_before_loot(catacombs_l8_text_before_loot) 
catacombs_l8.set_text_after_loot(catacombs_l8_text_after_loot)
minotaur_labyrinth_l8.set_text_before_loot(minotaur_labyrinth_l8_text_before_loot) 
minotaur_labyrinth_l8.set_text_after_loot(minotaur_labyrinth_l8_text_after_loot)
spyder_caves_l8.set_text_before_loot(spyder_caves_l8_text_before_loot) 
spyder_caves_l8.set_text_after_loot(spyder_caves_l8_text_after_loot)

# Locations lvl 9
escape_tunned_l9_text_before_loot = ("bt9")
escape_tunned_l9_text_after_loot = ("at9")
escape_elevator_l9_text_before_loot = ("bt9")
escape_elevator_l9_text_after_loot = ("at9")

escape_tunned_l9.set_text_before_loot(escape_tunned_l9_text_before_loot) 
escape_tunned_l9.set_text_after_loot(escape_tunned_l9_text_after_loot)
escape_elevator_l9.set_text_before_loot(escape_elevator_l9_text_before_loot) 
escape_elevator_l9.set_text_after_loot(escape_elevator_l9_text_after_loot)

# Location lvl 10
dragon_test_l10_text_before_loot = ("bt10")
dragon_test_l10_text_after_loot = ("at10")

dragon_test_l10.set_text_before_loot(dragon_test_l10_text_before_loot) 
dragon_test_l10.set_text_after_loot(dragon_test_l10_text_after_loot)








