'''character class'''

class Character():
    '''defines character super class'''
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.dialogue = None
    
    def set_dialogue(self, dialogue):
        '''character dialogue'''
        self.dialogue = dialogue

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
        print(self.name + " doesn't want to engage in dangerous and life threatening combat both based in close and long range. Please find the exit doors on each side of the cinema. If the exit doors have disappeared you've landed in the Backrooms. Nino Nakano the goat.")

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with the " + combat_item)
            return True
        else:
            print(self.name + " made you lose 20 yararara jannah points")