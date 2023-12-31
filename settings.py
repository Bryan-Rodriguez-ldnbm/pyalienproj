
class Settings:

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed = 3
        self.bullet_speed = 3.8
        self.alien_speed = 0.37

        self.fleet_direction = 1
        self.alien_points = 50
    
    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    
