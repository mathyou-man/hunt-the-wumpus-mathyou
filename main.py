from cave import Cave
from character import Character, Enemy
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Rooms and interactability
entrance = Cave("Entrance")
hallway_1 = Cave("Central Hallway")
hallway_2 = Cave("South Hallway")
hallway_2.set_interactability(True)
south_laboratory = Cave("South Laboratory First Floor")
south_laboratory.set_interactability(True)
south_laboratory_2 = Cave("South Laboratory Second Floor")
south_laboratory_2.set_interactability(True)
staircase_1 = Cave("1st Floor Staircase")
staircase_2 = Cave("2nd Floor Staircase")
staircase_basement = Cave("Basement Staircase")
armory = Cave("Armory")
armory.set_interactability(True)
infirmary = Cave("Infirmary")
hallway_floor_2 = Cave("Hallway 2nd Floor")
lounge = Cave("Lounge")
lounge.set_interactability(True)
hallway_basement = Cave("Basement Hallway")
garage_basement = Cave("Garage")
holding_cells = Cave("Holding Cells")
holding_cells.set_interactability(True)
generators = Cave("Generators")
generators.set_interactability(True)
training_room = Cave("Training Room")
training_room.set_interactability(True)

clear_screen()

# Player stats
player_health = 100
weapon_primary = "AR-15"
primary_damage = 50
weapon_secondary = "Glock-17"
secondary_damage = 20

# Descriptions
entrance.set_description("A white, sterile lobby. The desolate rows of chairs and the empty reception desk unnerve you.\n")
hallway_1.set_description("A simple white hallway. There is an open door on the west side of it.\n")
south_laboratory.set_description("A large room with a high ceiling. There is a grated floor above. There are vials of liquid in a locked glass box.\n")
south_laboratory_2.set_description("A large room with a grated floor. A faint smell of blood lingers in the air.\n")
hallway_2.set_description("A simple white hallway. A metal cart full of various items lies on the ground. A staircase leads upward and downward.\n")
armory.set_description("Guns everywhere. The weapon you need is locked behind a glass case.\n")
staircase_1.set_description("Stairs leading to the basement and to the second floor.\n")
staircase_2.set_description("Stairs leading to the first floor.\n")
staircase_basement.set_description("Stairs leading to the first floor.\n")
infirmary.set_description("White, neatly made beds entice you to rest.\n")
hallway_floor_2.set_description("A simple white hallway. To the east is a lounge room.\n")
lounge.set_description("A quiet lounge with soft chairs and dim lights.\n")
hallway_basement.set_description("A dark and musty hallway. There's a crowbar on the ground. The garage is nearby, and you can sense immense danger from the door leading to it. You best ensure you are prepared.")
garage_basement.set_description("Cars have been thrown about and the massive metal door leading to the outside has been pounded so hard there are dents in it.")
generators.set_description("A set of emergency generators. You can charge something big in here.")
holding_cells.set_description("Containment units that clearly were breached. There is a locked locker lying dented on the ground.")
training_room.set_description("Targets set some distance across the room are full of bullet holes. There's a set of keys on a wall hook.")

#room links
entrance.set_link_caves(hallway_1, "south")
south_laboratory.set_link_caves(hallway_1, "east")
south_laboratory_2.set_link_caves(staircase_2, "south")
lounge.set_link_caves(hallway_floor_2, "west")
infirmary.set_link_caves(hallway_2, "north")
armory.set_link_caves(hallway_2, "west")
armory.set_link_caves(training_room, "east")
training_room.set_link_caves(armory, "west")

#hallways and staircases links
hallway_1.set_link_caves(hallway_2, "south")
hallway_2.set_link_caves(staircase_1, "west")
hallway_2.set_link_caves(armory, "east")
hallway_2.set_link_caves(infirmary, "south")
hallway_2.set_link_caves(hallway_1, "north")
hallway_1.set_link_caves(south_laboratory, "west")
hallway_1.set_link_caves(entrance, "north")
staircase_1.set_link_caves(staircase_2, "up")
staircase_1.set_link_caves(hallway_2, "east")
staircase_2.set_link_caves(staircase_1, "down")
staircase_2.set_link_caves(south_laboratory_2, "north")
staircase_2.set_link_caves(hallway_floor_2, "east")
hallway_floor_2.set_link_caves(staircase_2, "west")
hallway_floor_2.set_link_caves(lounge, "east")

#keys
serum_keys = False
armory_keys = False
generator_keys = False
holding_keys = False

#player attributes
poison_immunity = False
shock_blaster = False
shock_charged = False
shock_avail = False
stim = False

# Enemies
current_cave = entrance
enemy_cooldown = 0

#stalker
stalker = Enemy("Stalker", "*You feel something watching you.*", 15, 0)
stalker.set_dialogue("...")
stalker.set_health(100)

#zombie
zombie = Enemy("Zombie", "A pale, groaning creature.", 10, 1)
zombie.set_dialogue("Kill...")
zombie.set_health(50)

#ultimate weapon
destroyer = Enemy("Destroyer", "A humanoid musclebound figure looms over you. There is bloodlust in the way it moves.", 100, 2)
destroyer.set_dialogue("KILL!!")
destroyer.set_health(10000)

south_laboratory.set_character(stalker)
south_laboratory_2.set_character(stalker)
hallway_floor_2.set_character(zombie)
hallway_2.set_character(zombie)
hallway_basement.set_character(zombie)
holding_cells.set_character(zombie)
generators.set_character(zombie)
armory.set_character(stalker)
training_room.set_character(zombie)
garage_basement.set_character(destroyer)

print("Commands: Fight (Only works if there is an enemy in the room with you, evading negates damage as a whole), Interact (Allows you to investigate parts of the room), Move (By entering direction to move in), Rest (Only works in infirmary), Inventory (Tells you your weapons, buffs and objects of interest.)")
print("I don't make plot holes which is why YOU CANT SHOOT ANYTHING OPEN THEY'RE ALL BULLETPROOF\n")

dead = False

while not dead:
    current_cave.describe()
    print("")

    if current_cave.get_name() == "Garage":
        dead = True
        print("The poison in the air emitted by the Destroyer immediately takes over your body and kills you.")
        break

    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant_name = inhabitant.name   # FIXED

    command = input("> ")

    # movement
    if command in ["north", "east", "south", "west", "up", "down"]:
        if inhabitant is not None:
            print(f"The {inhabitant_name} will kill you if you try to run away.")
            input()
        else:
            current_cave = current_cave.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            input()

    elif command == "inventory":
        print(f"You possess a {weapon_primary} and a {weapon_secondary}.")
        if shock_blaster:
            print("You have the Shock Blaster.")
        if stim:
            print("The stim you injected allows you to shoot two bullets in one action. You aren't fast enough to use it on the stimulant.")
        if poison_immunity:
            print("The serums you injected give you immunity to all poisons.")
        print("Your objects of interest are:")
        if holding_keys:
            print("Keys for something in the basement")
        if armory_keys:
            print("Keys for something in the armory")
        if serum_keys:
            print("Keys for something in the south lab first floor")
        if generator_keys:
            print("A keycard")
        input()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):

            # weapon selection
            if shock_blaster and shock_charged:
                shock_avail = True
                weapon = input(f"What will you fight with? Shock Blaster, {weapon_primary} or {weapon_secondary}? (ultimate/primary/secondary/evading) ")
            else:
                weapon = input(f"What will you fight with? {weapon_primary} or {weapon_secondary}? (primary/secondary/evading) ")

            if weapon == "primary":
                weapon_damage = primary_damage
            elif weapon == "ultimate":
                if shock_avail:
                    weapon_damage = 1000
                else:
                    print("You were too slow with getting a weapon out. It killed you.")
                    dead = True
                    continue
            elif weapon == "secondary":
                weapon_damage = secondary_damage
            else:
                print("You were too slow with getting a weapon out. It killed you.")
                dead = True
                continue

            inhabitant.health -= weapon_damage

            # enemy health feedback
            if inhabitant.health >= 75:
                print("It seems uninjured.")
            elif inhabitant.health >= 50:
                print("It is injured.")
            elif inhabitant.health > 0:
                print("It seems gravely injured.")
            else:
                print("It's dead.")
                current_cave.set_character(None)

            # enemy attack logic (FIXED)
            if inhabitant.health > 0:
                if enemy_cooldown == 0:
                    print(f"The {inhabitant_name} attacks.")
                    player_health -= inhabitant.get_damage()
                    enemy_cooldown = inhabitant.attack_speed   # FIXED: cooldown only set here
                else:
                    enemy_cooldown -= 1
                    print(f"The {inhabitant_name} prepares to attack.")

            # player health feedback
            if player_health == 100:
                print("You are perfectly uninjured.")
            elif player_health >= 75:
                print("You are relatively uninjured.")
            elif player_health >= 50:
                print("You are injured.")
            elif player_health > 0:
                print("You are gravely injured.")
            else:
                print("You succumb to your injuries.")
                dead = True

            input()

        else:
            print("There's nothing here.")

    elif command == "interact":
        if current_cave.interactability:

            if current_cave.get_name() == "South Hallway":
                serum_keys = True
                print("These keys might be of use.")
                current_cave.interactability = False

            elif current_cave.get_name() == "South Laboratory First Floor":
                if serum_keys:
                    poison_immunity = True
                    print("You inject the poison immunity serums. It will help when you eliminate your target.")
                    current_cave.interactability = False
                else:
                    print("You need keys to access the serums.")

            elif current_cave.get_name() == "Lounge":
                generator_keys = True
                print("A keycard.")
                current_cave.interactability = False

            elif current_cave.get_name() == "Generator":
                if generator_keys:
                    print("The keycard activates the Generators. You use it to charge the shock blaster and so it is now available for use.")
                    shock_charged = True
                    current_cave.interactability = False
                else:
                    print("You need a keycard to activate the generators.")

            elif current_cave.get_name() == "Training Room":
                holding_keys = True
                print("You collect a key meant for somewhere in the basement")
                current_cave.interactability = False

            elif current_cave.get_name() == "Holding Cells":
                if holding_keys:
                    print("You unlock the locker and collect a key labelled for the armory.")
                    armory_keys = True
                    current_cave.interactability = False
                else:
                    print("You need a key.")

            elif current_cave.get_name() == "Armory":
                if armory_keys and generator_keys and serum_keys:
                    print("You use the two keys and the keycard, opening the weapon's case. The shock blaster, a rifle with a tesla coil barrel capable of firing thousands of volts enters your possession.")
                    shock_blaster = True
                    current_cave.interactability = False
                else:
                    print("You're missing something.")

            elif current_cave.get_name() == "South Laboratory Second Floor":
                stim = True
                primary_damage = 100
                secondary_damage = 40
                print("You find a stimulant injector and use it. You can shoot faster now.")
                current_cave.interactability = False

        else:
            print("There's nothing to do here.")
        input()

    elif command == "rest":
        if current_cave.get_name() == "Infirmary":
            player_health = 100
            print("You rest and recover your strength.")
        else:
            print("You can't rest here.")
        input()

    clear_screen()
