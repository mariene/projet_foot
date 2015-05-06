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
        self.j = player
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        if  (need.CanHeshoot(self.j)):
            return self.allerversJ.compute_strategy(state,player,teamid)
        else :
            return self.defenseur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return NDef()

#ne marche pas 

# 2
# Vu où se trouve les flaques de boue ou de glace, c'est a dire souvent centré au milieu du terrain, 
# par conséquent les bords du terrain ne sont pas atteint donc on peut faire une strategie autour de ça 
# on attend que le joueur adverse prend le ballon et va jusqu'au but (s'il y arrive) donc notre joueur est en 
# défense, quand le ballon est proche de lui il le prend et parcours les bords du terrain jusqu'au cage 
# adverse donc il faut qu'il tire tout droit 
class Bord(SoccerStrategy):
    def __init__(self):
        self.name="Bord"
        self.goal = DefenseurBis()
        self.bas = ComposeStrategy (FonceurStrategy(),SurMemeLigneBas())
        self.haut = ComposeStrategy(FonceurStrategy(),SurMemeLigneHaut())
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        b = state.ball.position
        p = player.position
        bp= b - p
        gp = state.get_goal_center(need.get()) - player.position
        gb = state.get_goal_center(need.get()) - b
        if bp.norm < 10 :#or gb.norm < 10:
            if b.y > GAME_HEIGHT*0.5 :
                return self.bas.compute_strategy(state,player,teamid)
            else :
                return self.haut.compute_strategy(state,player,teamid)
        return self.goal.compute_strategy(state,player,teamid)

#defenseur qui vise vers les zones
class DefenseurTer(SoccerStrategy):
    def __init__(self):
        self.name="DefenseurTer"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad())
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(need.getad()) - p
        gp = g-p
        bp = state.ball.position - player.position
        dist = b + g
        d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        dirt = d - p
        zone = state.danger_zones.bottom_left
        gzone= g - zone
        if need.CanIshoot() : 
            if b.y < GAME_HEIGHT/2.0:
                shoot2=Vector2D.create_polar(gzone.angle + 2.505, 15)
                return SoccerAction(dirt,shoot2)
            else :
                shoot = Vector2D.create_polar(gzone.angle - 2.505, 15)
                return SoccerAction (dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DefenseurTer()    
                    
                    
                
