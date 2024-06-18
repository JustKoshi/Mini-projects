import random

class Player:
    
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        
    def increase_score(self, points):
        self.score += points
        
    def __str__(self):
        return f"Player {self.name}, Score: {self.score}"
    
class Game:
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    def roll_dice(self):
        return random.randint(1,6)
    
    def make_turn(self, player, target):
        print(f"It's your turn: {player.name}")
        roll1 = self.roll_dice()
        print(f"You rolled: {roll1}")
        if(roll1!=1):
            player.increase_score(roll1)
            print(f"{player.name} your score is {player.score}")
            answer = input("Do you want to roll again? (y/n) ")
            while(answer == 'y'):
                 roll1 = self.roll_dice()
                 print(f"You rolled: {roll1}")
                 if(roll1!=1):
                     player.increase_score(roll1)
                     print(f"{player.name} your score is {player.score}")
                     if(player.score>=target):
                         break
                     answer = input("Do you want to roll again? (y/n) ")
                 else:
                    player.score = 0
                    print(f"{player.name} your score is 0")
                    break
        else:
            player.score = 0
            print(f"{player.name} your score is 0")
        print(f"\n{player.name} total score is: {player.score}\n")
                
    def game_start(self):
        target_score = 21
        while self.player1.score < target_score and self.player2.score < target_score:
            
            self.make_turn(self.player1, target_score)
            if self.player1.score >= target_score:
                break
            
            self.make_turn(self.player2, target_score)
            if self.player2.score >= target_score:
                break
        if(self.player1.score>=target_score):
            print(f"Winner is {self.player1.name}!!\n")
        else:
            print(f"Winner is {self.player2.name}!!\n")    
            
player1 = Player("Kacper")
player2 = Player("Marcin")
game = Game(player1, player2)
game.game_start()
    