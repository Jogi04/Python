import random


class RockPaperScissors:
    def __init__(self, throw_pc, throw_user):
        self.throw_pc = throw_pc
        self.throw_user = throw_user

    def compare_throws(self):
        if self.throw_user == self.throw_pc:
            return 'draw'
        elif self.throw_user == 'scissors' and self.throw_pc != 'rock':
            return 'user wins'
        elif self.throw_user == 'rock' and self.throw_pc != 'paper':
            return 'user wins'
        elif self.throw_user == 'paper' and self.throw_pc != 'scissors':
            return 'user wins'
        elif self.throw_user != 'paper' and self.throw_pc == 'rock':
            return 'pc wins'
        elif self.throw_user != 'rock' and self.throw_pc == 'scissors':
            return 'pc wins'
        elif self.throw_user != 'scissors' and self.throw_pc == 'paper':
            return 'pc wins'


valid_throws = ['rock', 'paper', 'scissors']
draws = 0
wins = 0
loses = 0

while True:
    wish = str(input('Do you want to play Rock, Paper, Scissors [y/n]? '))
    if wish == 'n':
        break

    throw = str(input('rock, paper, scissors? '))
    if throw not in valid_throws:
        continue
    throw_pc = random.choice(valid_throws)

    game = RockPaperScissors(throw_pc, throw)
    print('Computer choice: ' + throw_pc)
    if game.compare_throws() == 'draw':
        print(game.compare_throws())
        draws += 1
    elif game.compare_throws() == 'user wins':
        print(game.compare_throws())
        wins += 1
    elif game.compare_throws() == 'pc wins':
        print(game.compare_throws())
        loses += 1

    print('\nDraws: ' + str(draws))
    print('Wins: ' + str(wins))
    print('Loses: ' + str(loses))
