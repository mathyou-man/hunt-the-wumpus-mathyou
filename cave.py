class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    def set_description(self, cave_description):
        self.description = cave_description

    #def get_description(self, cave_description):
        #return self.description
    
    def set_name(self, cave_name):
        self.name = cave_name

    def describe(self):
        print(self.description)

    def set_link_caves(self, cave_to_link, cave_direction):
        self.linked_caves[direction] = cave_to_link

    def get_link_caves(self):
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)