# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:20:04 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
from need import *
from math import pi 
from outils import *
###############################################################################     
#STRAT
#Defense

# defenseur a ameliorer car qd distance bg trop proche, plus le temps de choper balle
# enfin, de le rattrapper         
class Defenseur(SoccerStrategy):
    def __init__(self):
        self.name="Defenseur"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(need.getad()) - p
        gp = g-p
        bp = state.ball.position - player.position
        dist = b + g
        d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        dirt = d - p
        shoot = Vector2D.create_polar(gp.angle + 2.505, 15)
        dirt.product(10)
        if (b.y < GAME_HEIGHT*0.5) or (gb.norm <= 20.0): 
            shoot2=Vector2D.create_polar(gp.angle - 2.505, 15)
            return SoccerAction(dirt,shoot2)
        elif((p.distance(b)<=(PLAYER_RADIUS+BALL_RADIUS)))or(bp.norm <= GAME_WIDTH-(GAME_WIDTH*0.90)):
            return SoccerAction (dirt,shoot)
        shoot1 = Vector2D(-10,10)
        return SoccerAction(dirt,shoot1)
    def create_strategy(self):
        return Defenseur()

        
# Defenseur pour nouvelle configuration, meme chose que le defenseur du haut 
class DefenseurBis(SoccerStrategy):
    def __init__(self):
        self.name="DefenseurBis"
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
        dirt.product(10)
        if need.CanIshoot() : 
            if b.y < GAME_HEIGHT/2.0:
                shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                return SoccerAction(dirt,shoot2)
            else :
                shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                return SoccerAction (dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DefenseurBis() 

# defenseur, situe a un peu près 3/4 de la distance but-ballon, cad plus proche du ballon 
#marche pour attaquant mais moins pr Fonceur
class Def(SoccerStrategy):
    def __init__(self):
        self.name="Def"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad())
        b = state.ball.position
        p = player.position
        d = Vector2D(0.75*(b.x - GAME_WIDTH)+GAME_WIDTH, 0.75*(b.y-0.5*GAME_HEIGHT)+0.5*GAME_HEIGHT)
        if(teamid==1):
            d.x=0.75*b.x
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle+2.25,g.norm)
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Def()


class DefBis(SoccerStrategy):
    def __init__(self):
        self.name="DefBis"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad())
        b = state.ball.position
        p = player.position
        gp= g-p
        d = Vector2D(0.75*(b.x - GAME_WIDTH)+GAME_WIDTH, 0.75*(b.y-0.5*GAME_HEIGHT)+0.5*GAME_HEIGHT)
        shoot = Vector2D.create_polar(player.angle+2.25,g.norm)
        dirt = d - p           
        if(teamid==1):
            d.x = 0.75*b.x
            dirt = d - p
            if need.CanIshoot():  
                if b.y < GAME_HEIGHT/2.0:
                    shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                    return SoccerAction(dirt,shoot2)
                else :
                    shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                    return SoccerAction (dirt,shoot)
            else:
                return SoccerAction(dirt,Vector2D())
        else :
            if need.CanIshoot():  
                if b.y < GAME_HEIGHT/2.0:
                    shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                    return SoccerAction(dirt,shoot2)
                else :
                    shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                    return SoccerAction (dirt,shoot)
            else:
                return SoccerAction(dirt,Vector2D())         
    def create_strategy(self):
        return DefBis()


# defenseur qui defend et qui "tourne" avec le ballon
class DefCyclique(SoccerStrategy):
    def __init__(self):
        self.name="DefCyclique"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad())
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(need.getad()) - p
        dist = b + g
        d = Vector2D((dist.x/2.00)-(0.25*gb.norm), b.y)
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle + 2.25,g.norm)
        if teamid == 1 :
            d =  Vector2D((dist.x/2.00)+(0.25*gb.norm), b.y)
            dirt = d - p
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return DefCyclique()



class DefCycliqueBis(SoccerStrategy):
    def __init__(self):
        self.name="DefCycliqueBis"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad())
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(need.getad()) - p
        dist = b + g
        d = Vector2D((dist.x/2.00)-(0.25*gb.norm), b.y)
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle + 2.25,g.norm)
        if teamid == 1 :
            d =  Vector2D((dist.x/2.00)+(0.25*gb.norm), b.y)
            dirt = d - p
            if need.CanIshoot():  
                return SoccerAction(dirt,shoot)
            else :
                return SoccerAction(dirt,Vecteur2D())
        else:
            if need.CanIshoot():  
                return SoccerAction(dirt,shoot)
            else :
                return SoccerAction(dirt,Vecteur2D())     
    def create_strategy(self):
        return DefCycliqueBis()

#permet de renvoyer le ballon a l'oppose de l'endroit où c'est envoye
class DefenGoal(SoccerStrategy):
    def __init__(self):
        self.name="DefenGoal"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad()) 
        b = state.ball.position
        p = player.position
        gb = g - p
        dist = b + g
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.70*(b.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
        bp = state.ball.position - player.position
        if((p.distance(b)<=(PLAYER_RADIUS+BALL_RADIUS))) or (bp.norm <= GAME_WIDTH-(GAME_WIDTH*0.90)):
            if (b.y > 0.5*GAME_HEIGHT):
                shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
                return SoccerAction(dirt,shoot)
            else :
                shoot = Vector2D.create_polar(gb.angle - (pi/2.0), 100)
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return DefenGoal()

class DefenGoalBis(SoccerStrategy):
    def __init__(self):
        self.name="DefenGoalBis"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad()) 
        b = state.ball.position
        p = player.position
        gb = g - b
        dist = b + g
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.80*(b.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
        if need.CanIshoot():
            if (b.y > 0.5*GAME_HEIGHT):
                shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
                return SoccerAction(dirt,shoot)
            else :
                shoot = Vector2D.create_polar(gb.angle - (pi/2.0), 100)
                return SoccerAction(dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DefenGoalBis()
    
# essaye de prevoir ou le ballon va aller suivant le vecteur vitesse et pouvoir l'intercepter 
# marche pour fonceur / moins pour attaquant 
# derive de DefenGoal
class DeGoal(SoccerStrategy):
    def __init__(self):
        self.name="DeGoal"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(need.getad()) 
        b = state.ball.position
        p = player.position
        gb = g - b   
        bi = b + state.ball.speed
        dist = bi + g
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.75*(bi.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        shoot = Vector2D.create_polar(gb.angle + (pi/2.00), 100)
        if not need.CanIshoot():
            return SoccerAction(dirt,Vector2D())
        if (b.y > 0.5*GAME_HEIGHT):
            shoot = Vector2D.create_polar(gb.angle - (pi/2.0), 100)
            return SoccerAction(dirt,shoot)
        else :
            shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
            return SoccerAction(dirt,shoot)
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return DeGoal()


class DeGoalBis(SoccerStrategy):
    def __init__(self):
        self.name="DeGoalBis"
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        gad = state.get_goal_center(need.getad()) 
        g = state.get_goal_center(need.get()) 
        b = state.ball.position
        p = player.position
        gb = gad - b   
        dist = (b + state.ball.speed ) + gad
        bi = b + state.ball.speed 
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.70*(bi.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        if need.CanIshoot():
            if (b.y > 0.5*GAME_HEIGHT):
                shoot = Vector2D.create_polar(gb.angle - (pi/2.0), 15)
                return SoccerAction(dirt,shoot)
            else :
                shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 15)
                return SoccerAction(dirt,shoot)
        else :        
            return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DeGoalBis()
           
class Goal(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
        self.stratbas = ComposeStrategy(SurMemeLigneBis(),TirerVersLeBas())
        self.strathaut = ComposeStrategy(SurMemeLigneBis(),TirerVersLeHaut())
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        b = state.ball.position
        if (b.y > 0.5*GAME_HEIGHT):
            return self.strathaut.compute_strategy(state,player,teamid)
        else :
            return self.stratbas.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Goal()            

# compose Strat
class CoinHaut(SoccerStrategy):
    def __init__(self):        
        self.name="CoinHaut"
        self.strat=ComposeStrategy(AllerVersCoinHaut(),TirerVersLeBas())
    def compute_strategy(self,state,player,teamid):
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class CoinBas(SoccerStrategy):
    def __init__(self):        
        self.name="CoinBas"
        self.strat=ComposeStrategy(AllerVersCoinBas(),TirerVersLeHaut())
    def compute_strategy(self,state,player,teamid):
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    


