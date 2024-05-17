from numpy import random

choices = ['rock', 'paper', 'scissors'] 
beats= {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}

p1 = random.choice(choices)
p2 = random.choice(choices)  
print(f'Player 1: {p1}\nPlayer 2: {p2}')    

if beats[p1] == p2:
    print('Player 1 wins!')
elif beats[p2] == p1:
    print('Player 2 wins!')
else:
    print('Tie.')    
    

def find_winner(p1, p2):
    if beats[p1] == p2:
        return 'Player 1 wins!'
    elif beats[p2] == p1:
        return 'Player 2 wins!'
    else:
        return 'Tie.'
    
def readysetgo():
    return random.choice(choices)

def play_once():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'Player 1: {p1}\nPlayer 2: {p2}')
    
    winner = find_winner(p1,p2)
    print(f'The winner is: {winner}')
    
class Player():
    def __init__(self, name, strategy = 'random'):
        self.name = name
        self.wins = 0
        self.choices = ['rock', 'paper', 'scissors']
        self.strategy = strategy
        
    def readysetgo(self):
        if self.strategy == 'random':
            return random.choice(self.choices)
        elif self.strategy == 'always_rock':
            return 'rock'

class Game():
    def __init__(self, num_players = 2):
        self.beats = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
        self.num_players = num_players
        self.players = [Player(str(n+1)) for n in range(num_players)]
        
    def find_winner(self, p1, p2):
        if self.beats[p1] == p2:
            return 'Player 1'
        elif self.beats[p2] == p1:
            return 'Player 2'
        else:
            return 'Tie'
        
    def play_once(self):
        hands = [p.readysetgo() for p in self.players]
        print('Everyone plays:', hands)
        
        for player, hand in zip(self.players, hands):
            wins = sum([r == 'Player 1' for r in results])
            losses = sum([r == 'Player 2' for r in results])
            ties = sum([r == 'Tie' for r in results]) - 1
            print(f'Player {player.name}: {wins} wins, {Losses} Losses,')
            player.wins += wins
    
