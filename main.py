from cave import Cave
from character import Character, Enemy
import os

def clear_screen():
    '''Clears the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

clear_screen()

#set descriptions
cavern.set_description("A dark and dirty cave")
grotto.set_description("A small cave with ancient markings.")
dungeon.set_description("A large cave with torture stuff (earphones playing BTS)")

cavern.set_link_caves(dungeon, "south")
dungeon.set_link_caves(cavern, "north")
dungeon.set_link_caves(grotto, "west")
grotto.set_link_caves(dungeon, "east")

#sets characters
current_cave = cavern
harry = Enemy("Harry", "A hairy, smelly wumpus")
harry.set_dialogue("Come closer. I can't see you")
harry.set_weakness("gurpreet aura")
dungeon.set_character(harry)

dead = False
while dead == False:
    current_cave.describe()
    #checks whether cave has a character
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
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
            fight_with = input("What will you fight with? >")
            if inhabitant.fight(fight_with) is True:
                clear_screen()
                print("Light work")
                current_cave.set_character(None)
                input()
            else:
                clear_screen()
                print("That was ineffective. You ran away with your flesh intact")
                print("Game over.")
                input()
                dead = True
        else:
            print("There is no one here to run the 1s with")
        
    clear_screen()