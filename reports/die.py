import random


class Die():
    '''Get possibile numbers from rolling a dice of n sides.'''

    def __init__(self, num_sides=6):
        '''By defaut, this is D6 dice, but can be altered when 
        calling an instance of the class.'''
        self.num_sides = num_sides
        self.sides = range(1, self.num_sides+1)
        

    def roll(self):
        '''Generate the random possibilies of numbers within the range of sides.'''
        rollz = random.randint(1, self.num_sides)
        return rollz