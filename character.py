'''character class'''

class Character():
    '''defines character super class'''
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.dialogue = None
        self.health = 0
    
    def set_dialogue(self, dialogue):
        '''character dialogue'''
        self.dialogue = dialogue

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name

    def describe(self):
        '''prints description'''
        print("A " + self.name + " is here.")
        print(self.description)

    def talk(self):
        '''manages talking to the character'''
        if self.dialogue is not None:
            print("[" + self.name + " says]: " + self.dialogue)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self):
        '''manages fighting with the character'''
        print(self.name + " doesn't seem to want to fight.")

class Enemy(Character):
    def __init__(self, char_name, char_description, damage, attack_speed):
        super().__init__(char_name, char_description)
        self.enemy_damage = damage
        self.enemy_attack_speed = attack_speed
        
    def fight(self, weapon_damage):
        self.health -= weapon_damage
        if self.health <= 0:
            print("The " + self.name + " succumbs to its injuries.")
    
    def set_damage(self, damage):
        self.enemy_damage = damage

    def get_damage(self):
        return self.enemy_damage
    
    def set_speed(self, attack_speed):
        self.enemy_attack_speed = attack_speed

    def get_speed(self):
        return self.enemy_attack_speed