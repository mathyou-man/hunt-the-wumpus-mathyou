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

current_cave = cavern

#sets characters
harry = Enemy("Harry", "A hairy, smelly wumpus")
harry.describe()
harry.set_dialogue("Come closer. I can't see you")
harry.set_weakness("gurpreet aura")
harry.talk()

fight_with = input("What will you fight with? ")
harry.fight(fight_with)

while True:
    #print("\n")
    current_cave.describe()
    command = input("> ")
    current_cave = current_cave.move(command)