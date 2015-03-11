# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:20:27 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
import need
from outils import *
from math import pi

###############################################################################
#STRAT DE BASE
#joueur random
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
    def create_strategy(self):
        return RandomStrategy()
    
#joueur fonceur
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
            shoot = state.get_goal_center(need.get(teamid)) - p
        return SoccerAction(pos,shoot)
    def create_strategy(self):
        return FonceurStrategy()
 
#STRAT 
#attaque

#tire aleatoirement mais plus genre dribble mais plus loin (shoot loin)
class Aleatoire(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(need.get(teamid))
        b = state.ball.position
        dist= b - player.position
        if not need.CanIshoot(state,player):
            return SoccerAction(dist,Vector2D())
        gb = state.get_goal_center(need.get(teamid)) - player.position
        shoot = Vector2D.create_polar(gb.angle + random.uniform(-1,1),g.norm)
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
 

# un compose de plrs type de shoot
# mode fonceur si a le ballon 
# dans la partie du terrain adverse ou au moment du lancement-> shoot dans le ballon vers une direction rd pour peut etre atteindre des endroits 
# inaccesible pour le goal cad sur les coins des cages !
# qd proche des cages, cad, dans sa partie de terrain, tente de dribbler pour aller dans terrain adverse ...
# g.norm peut etre trop gde -> a voir !

class Attaquant(SoccerStrategy):
    def __init__(self):        
        self.bal= ComposeStrategy(AllerVersBalle(),TirerRd())
        self.fonce = FonceurStrategy()
        self.ale = ComposeStrategy(AllerVersBalle(),Aleatoire())
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        gadv = state.get_goal_center(need.get(teamid))
        b = state.ball.position
        gadvb = gadv - b
        p = player.position
        #dist= b - player.position
        gb = g - b 
        if ((b.x==GAME_WIDTH/2.0 and b.y==GAME_HEIGHT/2.0) or (gadvb.norm < GAME_WIDTH/6.0)): 
            return self.bal.compute_strategy(state,player,teamid)
        elif gb.norm < GAME_WIDTH/8.0:
            return self.ale.compute_strategy(state,player,teamid)
        else:
            return self.fonce.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

class Degage(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        if ((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
            shoot = state.get_goal_center(need.get(teamid)) - p
            return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

class DegageBis(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        if ((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
            gadvp = state.get_goal_center(need.get(teamid)) - p
            shoot = Vector2D().create_polar(gadvp.angle + random.uniform(-1,1), 10)
            return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  


class DegageTer(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        b = state.ball.position
        shoot = state.get_goal_center(need.get(teamid)) - p
        
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        p2 = (GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2) - 0.25
        p1 = (GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2) + 0.25
       # if p.distance(state.ball.position)>=PLAYER_RADIUS+BALL_RADIUS:
        if not need.CanIshoot(state,player):
            return SoccerAction(direct,Vector2D())
        if shoot.norm < 30:
            if (teamid == 2):
                if b.y < GAME_HEIGHT*0.5 :
                    v1 = Vector2D(0,p1)
                    shoot = v1 - p
                    return  SoccerAction(direct,shoot)
                else :
                    v2 = Vector2D(0,p2)
                    shoot = v2 - p
                    return SoccerAction(direct,shoot)
            else :
                if b.y < GAME_HEIGHT*0.5 :
                    v1 = Vector2D(GAME_WIDTH,p1)
                    shoot = v1 - p
                    return  SoccerAction(direct,shoot)
                else :
                    v2 = Vector2D(GAME_WIDTH,p2)
                    shoot = v2 - p
                    return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 