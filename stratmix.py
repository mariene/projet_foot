# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:25:04 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
from need import *
from math import pi 
from stratatt import *
from stratdef import *
from outils import *
###############################################################################
# un mix de defense et d'attaque  
# tentative -> a ameliorer !
class Mix(SoccerStrategy):
    def __init__(self):
        self.att= Attaquant()
        self.att2 = ComposeStrategy(AllerVersBalle(),FonceurStrategy())
        self.defe = DefenGoal()
        self.compo = ComposeStrategy(AllerVersBalle(),TirerRd())
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        b = state.ball.position
        p = player.position
        bp = b - p
        g = state.get_goal_center(need.getad())
        gb= g - b
        if gb.norm < (0.50 * GAME_WIDTH ) : 
            return self.defe.compute_strategy(state,player,teamid)
            if (p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS)) or bp.norm < 15:
                return self.att2.compute_strategy(state,player,teamid)
        if gb.norm == (0.20 * GAME_WIDTH ):
            return self.compo.compute_strategy(state,player,teamid)
        else: 
            return self.att.compute_strategy(state,player,teamid)                                    
    def create_strategy(self):
        return Mix()


# marche ! def au debut puis attaque quand a le ballon 
# trouver moyens -> fonce d'abord pour voir si peut choper le ballon 
# si oui attaque sinon defenseur et qd a le ballon va vers camp adverse 
class MixSimple(SoccerStrategy):
    def __init__(self):
        self.att= Attaquant()
        self.defe = DefenseurBis()
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position
        p = player.position
        bp= b - p
        if bp.norm < 30:
            return self.att.compute_strategy(state,player,teamid)
        return self.defe.compute_strategy(state,player,teamid)                  
    def create_strategy(self):
        return MixSimple()
