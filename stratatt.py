# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:20:27 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
from need import *
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
        need = Need(state, teamid, player)
        b = state.ball.position
        p = player.position
        pos = b-p
        shoot=Vector2D()
        if ((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
            shoot = state.get_goal_center(need.get()) - p
        return SoccerAction(pos,shoot)
    def create_strategy(self):
        return FonceurStrategy()
 
#STRAT 
#attaque

#tire aleatoirement mais plus genre dribble mais plus loin (shoot loin)
class Aleatoire(SoccerStrategy):
    def __init__(self):
        self.name="Aleatoire"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.get())
        b = state.ball.position
        dist= b - player.position
        if not need.CanIshoot():
            return SoccerAction(dist,Vector2D())
        gb = state.get_goal_center(need.get()) - player.position
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
        self.name="Attaquant"        
        self.bal= DegageTer()
        self.fonce = FonceurStrategy()
        self.ale = ComposeStrategy(AllerVersBalle(),Aleatoire())
    def compute_strategy(self,state,player,teamid):
        need = Need(state,teamid, player)
        g = state.get_goal_center(need.getad())
        gadv = state.get_goal_center(need.get())
        b = state.ball.position
        gadvb = gadv - b
        p = player.position
        gb = g - b 
        
        if (gadvb.norm < GAME_WIDTH/6.0): 
            return self.bal.compute_strategy(state,player,teamid)
        elif (b.x==GAME_WIDTH/2.0 and b.y==GAME_HEIGHT/2.0) or gb.norm < GAME_WIDTH/8.0:
            return self.ale.compute_strategy(state,player,teamid)
        else:
            return self.fonce.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  


class Degage(SoccerStrategy):
    def __init__(self):        
        self.name="Degage"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        if need.CanIshoot():
            shoot = state.get_goal_center(need.get()) - p
            return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

class DegageBis(SoccerStrategy):
    def __init__(self):        
        self.name="DegageBis"
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
        self.name="DegageTer"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        b = state.ball.position
        shoot = state.get_goal_center(need.get()) - p
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        p2 = (GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2) - 0.25
        p1 = (GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2) + 0.25
        if not need.CanIshoot():
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
    
# compose Strat
class Rd(SoccerStrategy):
    def __init__(self):        
        self.name="Rd"
        self.strat=ComposeStrategy(AllerVersBalle(),AleatoireBis())
    def compute_strategy(self,state,player,teamid):
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class Haut(SoccerStrategy):
    def __init__(self):        
        self.name="Haut"
        self.strat=ComposeStrategy(AllerVersBalle(),TirerVersLeHaut())
    def compute_strategy(self,state,player,teamid):
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class Bas(SoccerStrategy):
    def __init__(self):        
        self.name="Bas"
        self.strat=ComposeStrategy(AllerVersBalle(),TirerVersLeBas())
    def compute_strategy(self,state,player,teamid):
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 