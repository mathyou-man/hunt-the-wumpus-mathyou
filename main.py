from cave import Cave
from character import Character, Enemy
import os

def clear_screen():
    '''Clears the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

entrance = Cave("Entrance")
hallway_1 = Cave("Hallway")
south_laboratory = Cave("East Laboratory")

clear_screen()

#sets player stats
player_health = 100
weapon_primary = "AR-15"
primary_damage = 50
weapon_secondary = "Glock-17"
secondary_damage = 20

#set descriptions
entrance.set_description("A white, sterile lobby. The empty rows of chairs and reception desk unnerve you.")
hallway_1.set_description("A simple white hallway. There is an open door on the west side of the it.")
south_laboratory.set_description("A large room with a high ceiling. There is a grated floor above.")

#sets linked caves
entrance.set_link_caves(hallway_1, "south")
hallway_1.set_link_caves(south_laboratory, "west")
hallway_1.set_link_caves(entrance, "north")
south_laboratory.set_link_caves(hallway_1, "east")


#sets characters
current_cave = entrance
stalker = Enemy("Stalker", "*You feel something watching you.*")
stalker.set_dialogue("...")
stalker.set_health(100)
south_laboratory.set_character(stalker)

dead = False
while dead == False:
    current_cave.describe()
    #checks whether cave has a character
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
        if inhabitant = 
    command = input("> ")
    
    
    #does certain things when certain commands are put
    if command in ["north", "east", "south", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            input()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            weapon = input("What will you fight with? " + weapon_primary + " or " + weapon_secondary + " ?")
            if weapon == weapon_primary:
                weapon_damage = primary_damage
            elif weapon == weapon_secondary:
                weapon_damage = secondary_damage
            else:
                print("You were too slow with getting a weapon out. It killed you.")
                dead = True

            inhabitant.health -= weapon_damage
            if inhabitant.health >= 75:
                print("It seems uninjured")
            elif 75 > inhabitant.health >= 50:
                print("It is injured.")
            elif 50 > inhabitant.health > 0:
                print("It seems gravely injured.")
            elif inhabitant.health <= 0:
                print("It's dead.")
                current_cave.set_character(None)

            print(f"The {inhabitant_name} attacks.")
            player_health -= 15
            if player_health >= 75:
                print("You are relatively uninjured")
            elif 75 > player_health >= 50:
                print("You are injured.")
            elif 50 > player_health > 0:
                print("You are gravely injured.")
            elif player_health <= 0:
                print("You succumb to your injuries.")
                dead = True

            input()
        else:
            print("There's nothing here.")
        
    clear_screen()