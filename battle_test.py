from dice import dice
from dice import boss_dice

class battle():
    '''
    Executes a dice battle.
    '''

    def __init__(self):
        #creates the initial point count.
        self.player_points = 100
        self.advesary_points = 100
        self.player_dice = dice()
        self.enemy_dice = boss_dice()


    def run_battle(self):
        self.game_stat = True
        while self.game_stat == True:
            self.display_points()
            self.player_action()
            if self.game_stat:
                self.player_dice.roll()
                self.enemy_dice.roll()
                self._player = self.player_dice.send_dice()
                self._enemy = self.enemy_dice.send_dice()
                self.display_rolls()
                self.round_results()
            self.game_results()
            


    def display_points(self):
        #When called will display the current points

        print(f'\nYour points: {self.player_points}')
        print(f'You enemies points: {self.advesary_points}\n')


    def player_action(self):
        #asks if the player wants to keep playing

        while True:
            _decision = input('Do you wish to continue playing or cut you losses?\nY or N: ').upper()
            if _decision == 'Y' or _decision == 'YES':
                break
            elif _decision == 'N' or _decision == 'NO':
                self.game_stat = False
                break
            else:
                print('Enter valid input...')


    def display_rolls(self):
        #Displays the dice results.

        print('\nYour dice:')
        for res in self._player:
            print(f'[{res}]')

        print('\nEnemies dice:')
        for res in self._enemy:
            print(f'[{res}]')


    def round_results(self):
        #Calculates who won the round
        _player_total = 0
        _enemy_total = 0

        for _die in self._player:
            _player_total += _die

        for _die in self._enemy:
            _enemy_total += _die

        if _player_total > _enemy_total:
            print('\nYou won this round!\n')
            self.player_points += 10
            self.advesary_points -= 25
        elif _player_total < _enemy_total:
            print('\nYou have lost this round!\n')
            self.advesary_points += 10
            self.player_points -= 25

    
    def game_results(self):
        #Checks if the game is over and gives the results.
        if self.player_points <= 0:
            print('\nYou have lost the game!\nMaybe you need to collect more dice?')
            self.game_stat = False
        elif self.advesary_points <= 0:
            print(f'\nYou have won the game with {self.player_points} points!')
            self.game_stat = False
        else:
            pass
            


def self_test():
    example = battle()
    example.run_battle()

if __name__ == "__main__":
    self_test()  