# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:58:05 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS

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


class AllerVers (SoccerStrategy):
    def __init__(self):
        self.point=Vector2D()
    def compute_strategy(self,state,player,teamid):
        shoot=Vector2D()
        dist = self.point - player.position
        return SoccerAction(dist,shoot)
    def copy(self):
        s= AllerVers()
        s.point = self.point.copy()
        return s
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        
  

class AllerVersBalle (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        self.strat.point= state.ball.position        
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return AllerVersBalle()
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        
  

class AllerVersBalleBis (AllerVers):
    def __init__(self):
        AllerVers.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.point= state.ball.position        
        return AllerVers.compute_strategy(self,state,player,teamid)
    def copy(self):
        return AllerVersBalleBis()   


class AllerVersBut (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        self.strat.point= state.get_goal_center(self.get(teamid))
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return AllerVersBut()
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

       
class Tirer (SoccerStrategy):
    def __init__(self):
        self.point = Vector2D()
    def compute_strategy(self,state,player,teamid):
        shoot = self.point - player.position
        dist = Vector2D()
        return SoccerAction(dist,shoot)
    def copy(self):
        s = Tirer()
        s.point = self.point.copy()
        return s
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        



class TirerVersP(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.point= state.get_player(self.teamid)    
        return Tirer.compute_strategy(self,state,player,teamid)
    def copy(self):
        return TirerVersP()  

        
class TirerVersBut(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.p = state.get_goal_center(self.get(teamid)) - player.position        
        return Tirer.compute_strategy(self,state,player,teamid)
    def copy(self):
        return TirerVersBut() 
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

class PasBouger(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        shoot = Vector2D()
        dist = Vector2D()
        return SoccerAction(dist,shoot)
    def copy(self):
        return PasBouger()
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

# mastrat = ComposeStrategy(PasBouger(),TirVersBut())

class ComposeStrategy(SoccerStrategy):
    def __init__(self,dep,tir):
        self.dep = dep
        self.tir = tir
    def compute_strategy(self,state,player,teamid):
        dep= self.dep.compute_strategy(state,player,teamid)
        tir=self.tir.compute_strategy(state,player,teamid)
        return SoccerAction(dep,tir)
    def copy(self):
        return ComposeStrategy()
    def create_strategy(self):
        return ComposeStrategy()

class D(Soccer)


        