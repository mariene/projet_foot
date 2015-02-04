# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:58:05 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam


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

       
class Tirer (SoccerStrategy):
    def __init__(self):
        self.point
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


class TirerVersBut (Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.point= state.get_goal_center(self.get(teamid)) - player.position        
        return Tirer.compute_strategy(self,state,player,teamid)
    def copy(self):
        return TirerVersBut() 
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1
