from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerAction, SoccerStrategy
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS


class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
	return SoccerAction(Vector2D.create_random(-0.1,0.1),Vector2D.create_random(-0.1,0.1))
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()

class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position 
        p = player.position
        pos = b-p
        shoot=Vector2D()
        if (p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS)):
           shoot = state.get_goal_center(self.get(teamid)) - p
        return SoccerAction(pos,shoot)
    def copy(self):
        return FonceurStrategy()
    def create_strategy(self):
        return FonceurStrategy()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

class PStrategy(SoccerStrategy):
    def __init__(self):
        self.name="P"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position 
        p = player.position
        g = state.get_goal_center(teamid)
        pos = g - p
        shoot=Vector2D()
        if (p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS)):
           shoot = state.get_goal_center(self.get(teamid)) - p
        return SoccerAction(pos,shoot)
    def copy(self):
        return PStrategy()
    def create_strategy(self):
        return PStrategy()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1


