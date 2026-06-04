'''cave class'''
class Cave:
    '''defines cave class'''
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

    '''sets cave descriptions'''
    def set_description(self, cave_description):
        self.description = cave_description
    
    '''returns cave descriptions'''
    def get_description(self):
        return self.description
    
    '''sets cave name'''
    def set_name(self, cave_name):
        self.name = cave_name
    
    '''returns cave name'''
    def get_name(self):
        return self.name
    
    '''sets caves linked to current cave'''
    def set_link_caves(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    
    '''returns linked caves'''
    def get_link_caves(self):
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)
    
    def set_character(self, new_character):
        '''sets character in cave darou'''
        self.character = new_character 

    def get_character(self):
        '''get character '''
        return self.character

    '''organises main loop outputs'''
    def describe(self):
        print(self.description)
        self.get_link_caves()
    
    '''main movement method'''
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")