import random
class dice():
    #you roll a 1d6
    
    def __init__(self):
        self._die = []
        self._dice_number = 1
        self._min_value = 1
        self._max_value = 6


    def roll(self):
        self._die = []
        for i in range(self._dice_number):
            _result = random.randint(self._min_value,self._max_value)
            self._die.append(_result)


    def send_dice(self):

        return self._die


    def add_another_dice(self,amount):

        self._dice_number + amount


    def remove_a_dice(self,amount):

        self._dice_number - amount
    

class enemy_dice(dice):
    #The enemy rolls 1d12

    def __init__(self):
        self._die = []
        self._dice_number = 1
        self._min_value = 1
        self._max_value = 12


