import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    valid_moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.type = 'basic'

    def move(self):
        return valid_moves[0]

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'rocker'

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'random'

    def move(self):
        return random.choice(Player.valid_moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'human'

    def move(self):
        player_move = None
        while True:
            player_move = input('\tWhats your move: ')
            if player_move in Player.valid_moves:
                break
            else:
                print('\tInvalid input! Enter "rock", "paper" or "scissors".')

        return player_move


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'reflect'
        self.opponents_last_move = None

    def move(self):
        if self.opponents_last_move is None:
            return random.choice(Player.valid_moves)
        else:
            return self.opponents_last_move

    def learn(self, my_move, their_move):
        self.opponents_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'cycle'
        self.my_last_move = None

    # def move(self):
    #     if self.my_last_move == 'rock':
    #         return 'paper'
    #     elif self.my_last_move == 'paper':
    #         return 'scissors'
    #     elif self.my_last_move == 'scissors':
    #         return 'rock'
    #     else:
    #         return random.choice(Player.valid_moves)

    def move(self):
        if self.my_last_move is None:
            return random.choice(Player.valid_moves)
        else:
            last_move_index = Player.valid_moves.index(self.my_last_move)
            next_move_index = last_move_index + 1
            if next_move_index >= len(Player.valid_moves):
                return Player.valid_moves[0]
            else:
                return Player.valid_moves[next_move_index]

    def learn(self, my_move, their_move):
        self.my_last_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def show_scores(score, final_scores=False):
    if final_scores:
        print("The final scores are: ")
        print(f"\tPlayer1: {score['p1']}")
        print(f"\tPlayer2: {score['p2']}")
    else:
        print("\tThe scores so far: ")
        print(f"\t\tPlayer1: {score['p1']}")
        print(f"\t\tPlayer2: {score['p2']}")


class Game:

    def __init__(self, p1, p2, round_amount=3):
        self.p1 = p1
        self.p2 = p2
        self.round_amount = round_amount
        self.score = {'p1': 0, 'p2': 0}

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\tPlayer 1: {move1}  Player 2: {move2}")

        p1_win = beats(move1, move2)
        if move1 == move2:
            pass
        elif p1_win:
            self.score['p1'] += 1
        else:
            self.score['p2'] += 1

        show_scores(self.score)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(self.round_amount):
            print(f"Round {round+1}:")
            self.play_round()

        print("Game over!")
        show_scores(self.score, True)
        if self.score['p1'] > self.score['p2']:
            print("Player1 wins!")
        elif self.score['p2'] > self.score['p1']:
            print("Player2 wins!")
        else:
            print("It's a draw!")


def get_random_bot():
    bot_players = ['rocker', 'randomPlayer', 'reflectPlayer', 'cyclePlayer']
    random_bot = random.choice(bot_players)
    if random_bot == 'rocker':
        return RockPlayer()
    elif random_bot == 'randomPlayer':
        return RandomPlayer()
    elif random_bot == 'reflectPlayer':
        return ReflectPlayer()
    elif random_bot == 'cyclePlayer':
        return CyclePlayer()


if __name__ == '__main__':
    # Player classes:
    #   Player - basic player class;
    #   RockPlayer - only plays rock;
    #   RandomPlayer - each round picks random move;
    #   HumanPlayer - users gets to input move;
    #   ReflectPlayer - plays opponents last move; random on first round;
    #   CyclePlayer - cycles through valid moves; random on first round;

    game = Game(HumanPlayer(), RockPlayer(), 5)

    # game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
