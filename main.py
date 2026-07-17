from cave import Cave
from character import Character, Enemy
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

PRIMARY_BULLETS = 0
SECONDARY_BULLETS = 0

# ============================================================
#  SCALABLE ENEMY SYSTEM
# ============================================================

class EnemyFactory:
    def __init__(self):
        self.templates = {}

    def register(self, name, description, damage, speed, health, dialogue):
        self.templates[name] = {
            "description": description,
            "damage": damage,
            "speed": speed,
            "health": health,
            "dialogue": dialogue
        }

    def create(self, name):
        t = self.templates[name]
        e = Enemy(name, t["description"], t["damage"], t["speed"])
        e.set_health(t["health"])
        e.set_dialogue(t["dialogue"])
        return e

enemy_factory = EnemyFactory()

# Register enemy types
enemy_factory.register(
    "Stalker",
    "*You feel something watching you.*",
    damage=15,
    speed=0,
    health=100,
    dialogue="..."
)

enemy_factory.register(
    "Zombie",
    "A pale, groaning creature.",
    damage=10,
    speed=1,
    health=50,
    dialogue="Kill..."
)

enemy_factory.register(
    "Destroyer",
    "A humanoid musclebound figure looms over you. There is bloodlust in the way it moves.",
    damage=100,
    speed=2,
    health=10000,
    dialogue="KILL!!"
)

# ============================================================
#  ROOMS AND INTERACTABILITY
# ============================================================

entrance = Cave("Entrance")
entrance.set_interactability(True)
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

# ============================================================
#  PLAYER STATS
# ============================================================

player_health = 100
weapon_primary = "AR-15"
PRIMARY_BULLETS = 20
primary_damage = 50
weapon_secondary = "Glock-17"
SECONDARY_BULLETS = 100
secondary_damage = 20
player_evading = False

def reload():
    global PRIMARY_BULLETS, SECONDARY_BULLETS
    PRIMARY_BULLETS = 20
    SECONDARY_BULLETS = 100
    
# Keys
serum_keys = False
armory_keys = False
generator_keys = False
holding_keys = False

# Player attributes
poison_immunity = False
shock_blaster = False
shock_charged = False
shock_avail = False
stim = False

# ============================================================
#  DESCRIPTIONS
# ============================================================

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

# ============================================================
#  ROOM LINKS
# ============================================================

entrance.set_link_caves(hallway_1, "south")
south_laboratory.set_link_caves(hallway_1, "east")
south_laboratory_2.set_link_caves(staircase_2, "south")
lounge.set_link_caves(hallway_floor_2, "west")
infirmary.set_link_caves(hallway_2, "north")
armory.set_link_caves(hallway_2, "west")
armory.set_link_caves(training_room, "east")
training_room.set_link_caves(armory, "west")
garage_basement.set_link_caves(hallway_basement, "north")
holding_cells.set_link_caves(staircase_basement, "south")
generators.set_link_caves(hallway_basement, "west")

hallway_1.set_link_caves(hallway_2, "south")
hallway_2.set_link_caves(staircase_1, "west")
hallway_2.set_link_caves(armory, "east")
hallway_2.set_link_caves(infirmary, "south")
hallway_2.set_link_caves(hallway_1, "north")
hallway_1.set_link_caves(south_laboratory, "west")
hallway_1.set_link_caves(entrance, "north")
staircase_1.set_link_caves(staircase_2, "up")
staircase_1.set_link_caves(hallway_2, "east")
staircase_1.set_link_caves(staircase_basement, "down")
staircase_2.set_link_caves(staircase_1, "down")
staircase_2.set_link_caves(south_laboratory_2, "north")
staircase_2.set_link_caves(hallway_floor_2, "east")
staircase_basement.set_link_caves(staircase_1, "up")
staircase_basement.set_link_caves(holding_cells, "north")
staircase_basement.set_link_caves(hallway_basement, "east")
hallway_basement.set_link_caves(generators, "east")
hallway_basement.set_link_caves(staircase_basement, "west")
hallway_basement.set_link_caves(garage_basement, "south")
hallway_floor_2.set_link_caves(staircase_2, "west")
hallway_floor_2.set_link_caves(lounge, "east")

# ============================================================
#  SCALABLE ENEMY SPAWN TABLE
# ============================================================

enemy_spawns = {
    "South Laboratory First Floor": "Stalker",
    "South Laboratory Second Floor": "Stalker",
    "Hallway 2nd Floor": "Zombie",
    "South Hallway": "Zombie",
    "Basement Hallway": "Zombie",
    "Holding Cells": "Zombie",
    "Generators": "Zombie",
    "Armory": "Stalker",
    "Training Room": "Zombie",
    "Garage": "Destroyer"
}

boss_dead = False

# Apply spawns
all_caves = [
    entrance, hallway_1, hallway_2, south_laboratory, south_laboratory_2,
    staircase_1, staircase_2, staircase_basement, armory, infirmary,
    hallway_floor_2, lounge, hallway_basement, garage_basement,
    holding_cells, generators, training_room
]

for cave in all_caves:
    name = cave.get_name()
    if name in enemy_spawns:
        cave.set_character(enemy_factory.create(enemy_spawns[name]))

# ============================================================
#  GAME LOOP
# ============================================================

print("Commands: Fight (Only works if there is an enemy in the room with you, evading negates damage as a whole), Interact (Allows you to investigate parts of the room), Move (By entering direction to move in), Rest (Only works in infirmary), Inventory (Tells you your weapons, buffs and objects of interest.)\n")

current_cave = entrance
enemy_cooldown = 0
dead = False

while not dead:
    current_cave.describe()
    print("")
    player_evading = False

    if current_cave.get_name() == "Garage" and poison_immunity == False:
        dead = True
        print("The poison in the air emitted by the Destroyer immediately takes over your body and kills you.")
        break
    else:
        pass

    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant_name = inhabitant.name

    command = input("> ")

    # MOVEMENT
    if command in ["north", "east", "south", "west", "up", "down"]:
        if inhabitant is not None:
            print(f"The {inhabitant_name} will kill you if you try to run away.")
            input()
        else:
            current_cave = current_cave.move(command)

    # TALK
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            input()

    # INVENTORY
    elif command == "inventory":
        print(f"You possess a {weapon_primary} and a {weapon_secondary}.")
        print(f"You only have {PRIMARY_BULLETS} rounds left in your {weapon_primary} and {SECONDARY_BULLETS} bullets left in your {weapon_secondary}")
        if shock_blaster:
            print("You have the Shock Blaster.")
        if stim:
            print("The stim you injected allows you to shoot more precisely, dealing more damage. Doesn't work with shock blaster.")
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

    # FIGHT
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):

            # weapon selection
            if shock_blaster and shock_charged:
                shock_avail = True
                weapon = input(f"What will you fight with? Shock Blaster, {weapon_primary} or {weapon_secondary}? (ultimate/primary/secondary/evading) ")
            else:
                weapon = input(f"What will you fight with? {weapon_primary} or {weapon_secondary}? (primary/secondary/evading) ")

            # PRIMARY WEAPON (instant death if not enough ammo)
            if weapon == "primary":
                if PRIMARY_BULLETS >= 5:
                    weapon_damage = primary_damage
                    PRIMARY_BULLETS -= 5
                else:
                    print("Your primary weapon was empty. It killed you before you could use a weapon with bullets.")
                    dead = True
                    continue

            # ULTIMATE WEAPON
            elif weapon == "ultimate":
                if shock_avail:
                    weapon_damage = 2000
                    print(f"The shock blaster sends a bolt of immense energy at the {inhabitant_name}.")
                else:
                    print("You were too slow with getting a weapon out. It killed you.")
                    dead = True
                    continue

            # SECONDARY WEAPON (instant death if not enough ammo)
            elif weapon == "secondary":
                if SECONDARY_BULLETS >= 5:
                    weapon_damage = secondary_damage
                    SECONDARY_BULLETS -= 5
                else:
                    print("Your secondary weapon was empty. It killed you before you could use a weapon with bullets.")
                    dead = True
                    continue

            # EVADING
            elif weapon == "evading":
                player_evading = True
                weapon_damage = 0
                print("You prepare to evade.")

            # INVALID INPUT (instant death)
            else:
                print("You were too slow with getting a weapon out. It killed you.")
                dead = True
                continue
            
            if not player_evading:
                inhabitant.health -= weapon_damage

            # enemy health feedback
            if inhabitant_name == "Stalker":
                if inhabitant.health >= 75:
                    print("It seems uninjured.")
                elif inhabitant.health >= 50:
                    print("It is injured.")
                elif inhabitant.health > 0:
                    print("It seems gravely injured.")
                else:
                    print("It's dead.")
                    current_cave.set_character(None)
            
            elif inhabitant_name == "Zombie":
                if inhabitant.health >= 40:
                    print("It seems uninjured.")
                elif inhabitant.health >= 20:
                    print("It is injured.")
                elif inhabitant.health > 0:
                    print("It seems gravely injured.")
                else:
                    print("It's dead.")
                    current_cave.set_character(None)
            
            elif inhabitant_name == "Destroyer":
                if inhabitant.health >= 8000:
                    print("It moves without struggle. You have to hit it harder.")
                elif inhabitant.health >= 5000:
                    print("It's heaving now.")
                elif inhabitant.health >= 2000:
                    print("Just a little more...")
                elif inhabitant.health >= 0:
                    print("It's almost dead.")
                else:
                    print("It crashed down with a thud. It's finally dead.")
                    boss_dead = True
                    current_cave.set_character(None)

            # enemy attack logic
            if inhabitant.health > 0 and not player_evading:
                if enemy_cooldown == 0:
                    print(f"The {inhabitant_name} attacks.")
                    player_health -= inhabitant.get_damage()
                    enemy_cooldown = inhabitant.get_speed()
                else:
                    print(f"The {inhabitant_name} prepares to attack.")
            else:
                if player_evading:
                    print(f"\nYou evade the {inhabitant_name}'s attack.")
                    enemy_cooldown = inhabitant.get_speed()
                elif enemy_cooldown != 0:
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
            
            print(f"You only have {PRIMARY_BULLETS} rounds left in your {weapon_primary} and {SECONDARY_BULLETS} bullets left in your {weapon_secondary}")

            input()

        else:
            print("There's nothing here.")

    # INTERACT
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

            elif current_cave.get_name() == "Generators":
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
                if armory_keys and generator_keys and serum_keys and shock_blaster == False:
                    print("You use the two keys and the keycard, opening the weapon's case. The shock blaster, a rifle with a tesla coil barrel capable of firing thousands of volts enters your possession.")
                    print("You restock on ammo.")
                    shock_blaster = True
                    reload()

                elif shock_blaster:
                    print("You restock on ammo.")
                    reload()

                else:
                    print("You're missing something that can unlock the shock blaster.")
                    print("You restock on ammo.")
                    reload()

            elif current_cave.get_name() == "South Laboratory Second Floor":
                stim = True
                primary_damage = 100
                secondary_damage = 40
                print("You find a stimulant injector and use it. You can shoot faster now.")
                current_cave.interactability = False
            
            elif current_cave.get_name() == "Entrance":
                if boss_dead:
                    print("You leave. The job is finished. The company that hired you to kill their experiment gives you the shock blaster as a gift. You eat dinner, wondering when you'll get a girlfriend.")
                    dead = True
                else:
                    print("You aren't done yet. Finish the job.")



        else:
            print("There's nothing to do here.")
        input()

    # REST
    elif command == "rest":
        if current_cave.get_name() == "Infirmary":
            player_health = 100
            print("You rest and recover your strength.")
        else:
            print("You can't rest here.")
        input()

    clear_screen()
