# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:37:30 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from soccersimulator import*
from stratatt import *
from stratdef import *
from stratmix import *
from outils import *

# 1 Nouvelle Stratégie 
class NDef(SoccerStrategy):
    def __init__(self,player):
        self.name="NDef"
        self.allerversJ= AllerVersJoueur()
        self.defenseur = DefenseurBis()
        self.player = player
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        if  (need.CanHeshoot(player)):
            return self.allerversJ.compute_strategy(state,player,teamid)
        else :
            return self.defenseur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return NDef()


        