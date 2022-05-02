import random
import sys


class RockPaperScissors:
    def __init__(self):
        self.winning_responses = {
          # 'move': [moves that lose to that move],
            'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
            'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
            'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
            'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
            'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
            'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
            'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
            'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
            'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
            'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
            'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
            'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
            'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
        }
        self.player_scores = {
            # 'player': int(score)
        }
        self.player_name = ''
        self.commands = ['!exit', '!rating']
        self.valid_options = []
        self.player_move = ''
        self.computer_move = ''
        self.result = ''

    def rps_game(self):
        self._startup_steps()

        while True:
            self._set_player_move()
            self._check_for_exit()
            self._check_for_rating()

            if not self._move_is_valid() or (self.player_move in self.commands):
                continue
            else:
                pass

            self._set_computer_move()
            self._set_round_result()
            self._update_player_score()
            self._print_result()

    def _startup_steps(self):
        """The steps required to set up the game."""
        self._set_player_name()
        print(f'Hello, {self.player_name}')
        self._set_player_scores()
        self._add_current_player()
        self._set_valid_options()
        print("Okay, let's start\n")
        return

    def _set_player_name(self):
        """Sets the player_name attribute with the player name."""
        self.player_name = input("Enter your name: ")
        return

    def _set_player_scores(self):
        """Reads the ratings file into the player_scores attribute"""
        with open('rating.txt', 'r') as ratings:
            for line in ratings.readlines():
                entry = line.split(' ')
                player = entry[0]
                score = int(entry[1])
                self.player_scores[player] = score

        return

    def _set_player_move(self):
        """Sets the player_move attribute from input."""
        self.player_move = input()
        return

    def _add_current_player(self):
        """Adds the current player to the _player_scores attribute if it's not already there."""
        if self.player_name not in self.player_scores.keys():
            self.player_scores[self.player_name] = 0

        return

    def _set_valid_options(self):
        """Sets the valid_options attribute via user input."""
        options = input("Enter the options you would like to play with, separated by a comma")
        if options:
            self.valid_options += options.split(',')
            return
        if not options:
            self.valid_options += ['rock', 'paper', 'scissors']
            return

    def _check_for_exit(self):
        """Exits the program if an exit command is given."""
        if self.player_move == '!exit':
            print("Bye!")
            sys.exit()

    def _check_for_rating(self):
        """Prints the player's score if requested."""
        if self.player_move == '!rating':
            print(f'Your rating: {self.player_scores[self.player_name]}')

        return

    def _move_is_valid(self):  # Boolean
        """Checks that the player move is valid."""
        if self.player_move in self.valid_options + self.commands:
            return True
        else:
            print("Invalid input\n")
            return False

    def _set_computer_move(self):
        """Randomly sets the computer_move attribute."""
        self.computer_move = random.choice(self.valid_options)
        return

    def _set_round_result(self):
        """Sets the result attribute."""
        if self.computer_move in self.winning_responses[self.player_move]:
            self.result = 'win'
            return
        if self.computer_move == self.player_move:
            self.result = 'draw'
            return
        if self.player_move in self.winning_responses[self.computer_move]:
            self.result = 'lose'
            return

    def _update_player_score(self):
        """Updates the player's score based on the result of the round."""
        if self.result == 'draw':
            self.player_scores[self.player_name] += 50
            return
        if self.result == 'win':
            self.player_scores[self.player_name] += 100
            return

        return

    def _print_result(self):
        """Prints the result of the round"""
        if self.result == 'lose':
            print(f'Sorry, but the computer chose {self.computer_move}\n')
            return
        if self.result == 'draw':
            print(f'There is a draw ({self.player_move})\n')
            return
        if self.result == 'win':
            print(f'Well done. The computer chose {self.computer_move} and failed\n')
            return


rps = RockPaperScissors()
rps.rps_game()
