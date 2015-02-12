# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:58:05 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT
import random

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
            shoot = state.get_goal_center(self.get(teamid)) - p
        return SoccerAction(pos,shoot)
    def create_strategy(self):
        return FonceurStrategy()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

# Aller vers un point
class AllerVers (SoccerStrategy):
    def __init__(self):
        self.point=Vector2D()
    def compute_strategy(self,state,player,teamid):
        shoot=Vector2D()
        dist = self.point - player.position
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        
  
#aller vers la balle en 2 versions
class AllerVersBalle (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        self.strat.point= state.ball.position        
        return self.strat.compute_strategy(state,player,teamid)
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
 
#Aller vers but 
class AllerVersBut (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        self.strat.point= state.get_goal_center(self.get(teamid))
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

#tirer vers un point       
class Tirer (SoccerStrategy):
    def __init__(self):
        self.point = Vector2D()
    def compute_strategy(self,state,player,teamid):
        shoot = self.point - player.position
        dist = Vector2D()
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        

#tirer vers un joueur -> a developper
class TirerVersP(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.point= state.get_player(self.teamid)    
        return Tirer.compute_strategy(self,state,player,teamid)
         
class TirerVersBut(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.p = state.get_goal_center(self.get(teamid)) - player.position        
        return Tirer.compute_strategy(self,state,player,teamid) 
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
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    
# mastrat = ComposeStrategy(PasBouger(),TirVersBut())
# pour faire composition de strat
class ComposeStrategy(SoccerStrategy):
    def __init__(self,dep,tir):
        self.dep = dep
        self.tir = tir
    def compute_strategy(self,state,player,teamid):
        dep= self.dep.compute_strategy(state,player,teamid)
        tir=self.tir.compute_strategy(state,player,teamid)
        return SoccerAction(dep.acceleration,tir.shoot)
 

#tire n'importe ou
class TirerRd(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        b = state.ball.position
        gb = state.get_goal_center(self.get(teamid)) - player.position
        #de=Vector2D.create_polar(player.angle, g.norm)
        dr= Vector2D.create_polar(player.angle+random.random(),g.norm)
        direc = Vector2D()    
        return SoccerAction(direc,dr)
    def create_strategy(self):
        return TirerRd()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1 
     
# defenseur a ameliorer car qd distance bg trop proche, plus le temps de choper balle
# enfin, de le rattrapper         
class Defenseur(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(self.get(teamid)) - p
        gp = g-p
        #pm = Vector2D(p.x*2,p.y*2) quand on veut modifier des coordonnées
        #shoot1 = g + b - pm
        #shoot = Vector2D.create_polar(player.angle + 3.25, 100)
        #shoot = Vector2D.create_polar(gb.angle + 2.25, 150)
        dist = b + g
        d = Vector2D((dist.x)/2,(dist.y)/2)   
        dirt = d - p
        shoot = Vector2D.create_polar(gp.angle + 2.5, 100)
        if (gb.norm < 15):
            dirt1 = dist- p - p
            return SoccerAction(dirt1,shoot)
        #shoot = Vector2D.create_polar(gb.angle + 2.5, 150)
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Defenseur()
    def get(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2


class Aleatoire(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        b = state.ball.position
        dist= b - player.position
        gb = state.get_goal_center(self.get(teamid)) - player.position
        shoot = Vector2D.create_polar(gb.angle + random.uniform(-1,1),15)
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1 

            
class Attaquant(SoccerStrategy):
    def __init__(self):        
        self.bal= ComposeStrategy(AllerVersBalle(),TirerRd())
        self.fonce = ComposeStrategy(FonceurStrategy(),TirerVersBut())
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        b = state.ball.position
        dist= b - player.position
        gb = g - b 
        if (gb.norm < GAME_WIDTH/5):
            return self.fonce.compute_strategy(state,player,teamid)
        return self.bal.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

            
class Mix(SoccerStrategy):
    def __init__(self):
        self.att= ComposeStrategy(AllerVersBalle(),FonceurStrategy())
        self.defe=Defenseur()
        self.compo = ComposeStrategy(AllerVersBalle(),TirerRd())
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position
        p = player.position
        bp = b - p
        g = state.get_goal_center(self.get(teamid))
        gb= g - b
        #bpd = Vector2D(bp.x - 1, bp.y)
        #shoot = Vector2D.create_polar(player.angle+random.random(),10)
        shoot = Vector2D.create_polar(player.angle + 2.5, 150)
        if b.x==GAME_WIDTH/2.0 and b.y==GAME_HEIGHT/2.0 : 
            return SoccerAction(bp,shoot)
        elif b.x < GAME_WIDTH/3: 
            if((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
                dist = Vector2D()
                return SoccerAction(dist,shoot)
            else :
                return self.defe.compute_strategy(state,player,teamid)
        if gb < ((1/10) * GAME_WIDTH ) : 
            return self.compo.compute_strategy(state,player,teamid)
        return self.att.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Mix()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1
