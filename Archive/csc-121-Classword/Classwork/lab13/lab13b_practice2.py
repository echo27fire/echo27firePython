'''
Name: Taylor Goodspeed
Date: Nov 18, 2023
Assignment:  Lab09b - OOP Practice Exercise #2 - Code Completion
'''

'''
--pre config doc string--
Complete the following code so that the class includes a method named updateAttacks, which takes
a string argument representing a single attack in the game.  The updateAttacks method shold append
the value of the attack parameter to the list of attacks.

When completed, the program should display:
Pokemon name is Bulbasaur and type is Grass. Attacks include: ['Vine Whip', 'Tackle']
Pokemon name is Yzma and type is Rock.  Attacks include: ['Smash']

For full credit, also write comments and complete the docstring in this code!
'''

class Pokemon:
    """
    Represents a Pokemon with a name, type, and a list of attacks.
    """

    def __init__(self, name, kind):
        self.name = name  # Initialize the name
        self.type = kind  # Initialize the type
        self.attacks = []  # Initialize the list of attacks

    def updateAttacks(self, attack):
        """
        Adds a new attack to the list of attacks.

        Parameters:
        - attack (str): The name of the attack to be added.
        """
        self.attacks.append(attack)  # Append the new attack to the attacks list

    def __str__(self):
        return f"Pokemon name is {self.name} and type is {self.type}. Attacks include: {str(self.attacks)}"

# Create Pokemon instances and update their attacks
bulbasaur = Pokemon('Bulbasaur', 'Grass')
bulbasaur.updateAttacks('Vine Whip')
bulbasaur.updateAttacks('Tackle')

yzma = Pokemon('Yzma', 'Rock')
yzma.updateAttacks('Smash')


# DO NOT CHANGE ANYTHING BELOW THIS
print(bulbasaur)   # DO NOT CHANGE THIS
print(yzma)   #DO NOT CHANGE THIS
