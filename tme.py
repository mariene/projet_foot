# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
Ce script temporaire est sauvegardé ici :
/users/Etu2/3202002/.spyder2/.temp.py
"""
#PLAYER_RADIUS=1.
#BALL_RADIUS=0.65
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet, PLAYER_RADIUS, BALL_RADIUS
v = Vector2D()
v1 = Vector2D(1,2)
v2 = Vector2D(2,3)
v3 = v1 + v2
v3+=v3
v4=v3-v1
v5 = Vector2D.create_random(0,1)
v5.x
v5.norm
action = SoccerAction(v1,v5)
action.shoot
action.acceleration
action.acceleration.norm

class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos = Vector2D.create_random(-1,1)
        shoot = Vector2D.create_random(-1,1)
        return SoccerAction(pos,shoot)
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
        if ((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
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
            
#goal qui ressort le ballon, a mettre avec CStratégie pour contrer 2 joueurs fonceurs
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
        dist_gp = g - p 
        #dist_pp= p - state.team.player.position
        #shoot = state.get_goal_center(self.get(teamid)) - p
        shoot=Vector2D()
        if (state.is_y_inside_goal(p.y)):
            if (b-p < 10):
                shoot = b + g - 2*p
            if (p.distance(b)< PLAYER_RADIUS + BALL_RADIUS):
                shoot = state.get_goal_center(self.get(teamid)) - p
                #if (dist_pp < 5):
                #shoot = dist_pp - p
        else:
            shoot = state.get_goal_center(self.get(teamid)) - p
        return SoccerAction(dist_gp,shoot)     
    def copy(self):
        return PStrategy()
    def create_strategy(self):
        return PStrategy()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1
            
#essaye de reprendre le ballon quand le goal le ressort
class CStrategy(SoccerStrategy):
    def __init__(self):
        self.name="C"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position
        p = player.position
        dist_bp = b - p
        #dist_pp= p - state.SoccerTeam.player.position
        if (p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS)) :
            shoot = state.get_goal_center(self.get(teamid)) - p
            return SoccerAction(dist_bp,shoot)
    def copy(self):
        return CStrategy()
    def create_strategy(self):
        return CStrategy()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",PStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",RandomStrategy()))
team2.add_player(SoccerPlayer("t2j1",RandomStrategy()))
team1.add_player(SoccerPlayer("t1j2",RandomStrategy()))
team2.add_player(SoccerPlayer("t2j2",RandomStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 