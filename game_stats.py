
class GameStats:

    def __init__(self, ai_game):
        
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self.read_scores()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def read_scores(self):
        file = open('highscore.txt','r')
        score = file.read()
        return int(score)
    
    def save_scores(self):
        file = open('highscore.txt','w')
        file.write(str(self.high_score))