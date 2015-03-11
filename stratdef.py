# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:20:04 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
import need
from math import pi 

###############################################################################     
#STRAT
#Defense

# defenseur a ameliorer car qd distance bg trop proche, plus le temps de choper balle
# enfin, de le rattrapper         
class Defenseur(SoccerStrategy):
    def __init__(self):
        #self.shooter=ComposeStrategy(PasBouger(),TirerRd())
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(self.getad(teamid)) - p
        gp = g-p
        bp = state.ball.position - player.position
        #pm = Vector2D(p.x*2,p.y*2) quand on veut modifier des coordonnées
        #shoot1 = g + b - pm
        #shoot = Vector2D.create_polar(player.angle + 3.25, 100)
        #shoot = Vector2D.create_polar(gb.angle + 2.25, 150)
        dist = b + g
        d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        dirt = d - p
        shoot = Vector2D.create_polar(gp.angle + 2.505, 15)
        dirt.product(10)
        if (b.y < GAME_HEIGHT*0.5) or (gb.norm <= 20.0): #or b.y > GAME_HEIGHT/2.0:
            #shoot2 = dist - p - p
            shoot2=Vector2D.create_polar(gp.angle - 2.505, 15)
            return SoccerAction(dirt,shoot2)
        elif((p.distance(b)<=(PLAYER_RADIUS+BALL_RADIUS)))or(bp.norm <= GAME_WIDTH-(GAME_WIDTH*0.90)):
            # or  b.y < 90.0/2.0:
            #return self.shooter.compute_strategy(state,player,teamid)
            return SoccerAction (dirt,shoot)
        shoot1 = Vector2D(-10,10)
        return SoccerAction(dirt,shoot1)
        #shoot = Vector2D.create_polar(gb.angle + 2.5, 150)
        #return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Defenseur()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2
        
# Defenseur pour nouvelle configuration, meme chose que le defenseur du haut 
class DefenseurBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(self.getad(teamid)) - p
        gp = g-p
        bp = state.ball.position - player.position

        dist = b + g
        d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        dirt = d - p
        dirt.product(10)
        
        if need.CanIshoot(state,player) : 
            if b.y < GAME_HEIGHT/2.0:
                shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                return SoccerAction(dirt,shoot2)
            else :
                shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                return SoccerAction (dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DefenseurBis()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2    

# defenseur, situe a un peu près 3/4 de la distance but-ballon, cad plus proche du ballon 
#marche pour attaquant mais moins pr Fonceur
class Def(SoccerStrategy):
    def __init__(self):
        #self.shooter=ComposeStrategy(AllerVersBalle(),TirerRd())
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        #gb = state.get_goal_center(self.getad(teamid)) - b
        #dist = b + g
#        d = Vector2D((dist.x/2.00)-(0.25*gb.norm), b.y)
        d = Vector2D(0.75*(b.x - GAME_WIDTH)+GAME_WIDTH, 0.75*(b.y-0.5*GAME_HEIGHT)+0.5*GAME_HEIGHT)
        if(teamid==1):
            d.x=0.75*b.x
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle+2.25,g.norm)
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Def()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

class DefBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gp= g-p
        d = Vector2D(0.75*(b.x - GAME_WIDTH)+GAME_WIDTH, 0.75*(b.y-0.5*GAME_HEIGHT)+0.5*GAME_HEIGHT)
        shoot = Vector2D.create_polar(player.angle+2.25,g.norm)
        dirt = d - p    
        
        if(teamid==1):
            d.x = 0.75*b.x
            dirt = d - p
            if need.CanIshoot(state,player):  
                if b.y < GAME_HEIGHT/2.0:
                    shoot2=Vector2D.create_polar(gp.angle + 2.505, 15)
                    return SoccerAction(dirt,shoot2)
                else :
                    shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                    return SoccerAction (dirt,shoot)
            else:
                return SoccerAction(dirt,Vector2D())
        else :
            if need.CanIshoot(state,player):  
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
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

# defenseur qui defend et qui "tourne" avec le ballon
class DefCyclique(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(self.getad(teamid)) - p
        dist = b + g
        d = Vector2D((dist.x/2.00)-(0.25*gb.norm), b.y)
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle + 2.25,g.norm)
        #if need.CanIshoot(state,player) == False:
         #   return SoccerAction(dirt,Vector2D())
        #else:
        if teamid == 1 :
            d =  Vector2D((dist.x/2.00)+(0.25*gb.norm), b.y)
            dirt = d - p
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Defenseur()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2


class DefCycliqueBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        b = state.ball.position
        p = player.position
        gb = state.get_goal_center(self.getad(teamid)) - p
        dist = b + g
        d = Vector2D((dist.x/2.00)-(0.25*gb.norm), b.y)
        dirt = d - p
        shoot = Vector2D.create_polar(player.angle + 2.25,g.norm)
        #if need.CanIshoot(state,player) == False:
         #   return SoccerAction(dirt,Vector2D())
        #else:
        if teamid == 1 :
            d =  Vector2D((dist.x/2.00)+(0.25*gb.norm), b.y)
            dirt = d - p
            if need.CanIshoot(state,player):  
                return SoccerAction(dirt,shoot)
            else :
                return SoccerAction(dirt,Vecteur2D())
        else:
            if need.CanIshoot(state,player):  
                return SoccerAction(dirt,shoot)
            else :
                return SoccerAction(dirt,Vecteur2D())     
    def create_strategy(self):
        return DefCycliqueBis()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

#permet de renvoyer le ballon a l'oppose de l'endroit où c'est envoye
class DefenGoal(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid)) 
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
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

class DefenGoalBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid)) 
        b = state.ball.position
        p = player.position
        gb = g - b
        dist = b + g
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.80*(b.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
        if need.CanIshoot(state,player):
            if (b.y > 0.5*GAME_HEIGHT):
                shoot = Vector2D.create_polar(gb.angle + (pi/2.0), 100)
                return SoccerAction(dirt,shoot)
            else :
                shoot = Vector2D.create_polar(gb.angle - (pi/2.0), 100)
                return SoccerAction(dirt,shoot)
        return SoccerAction(dirt,Vector2D())
    def create_strategy(self):
        return DefenGoalBis()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2
# essaye de prevoir ou le ballon va aller suivant le vecteur vitesse et pouvoir l'intercepter 
# marche pour fonceur / moins pour attaquant 
# derive de DefenGoal
class DeGoal(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid)) 
        b = state.ball.position
        p = player.position
        gb = g - b   
        dist = (b + state.ball.speed ) + g
        bi = b + state.ball.speed
        dist = bi + g
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.75*(bi.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        #gp = g-p
        shoot = Vector2D.create_polar(gb.angle + (pi/2.00), 100)
        #bp = state.ball.position - player.position
        #if bp.norm <= GAME_WIDTH-(GAME_WIDTH*0.90) or (p.distance(b)<=(PLAYER_RADIUS+BALL_RADIUS)) :
        if not need.CanIshoot(state,player):
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
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

class DeGoalBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        gad = state.get_goal_center(self.getad(teamid)) 
        g = state.get_goal_center(need.get(teamid)) 
        b = state.ball.position
        p = player.position
        gb = gad - b   
        dist = (b + state.ball.speed ) + gad
        bi = b + state.ball.speed
        #dist = b + gad
        #d = Vector2D((dist.x)/2.00,(dist.y)/2.00)   
        d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.70*(bi.y-(GAME_HEIGHT*0.5)))
        dirt = d - p
        
        if need.CanIshoot(state,player):
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
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2
            
            
# def proche test 
class DefGoalP(SoccerStrategy):
    def __init__(self):
        self.defe = Defenseur()
        self.deg=DeGoal()
        self.defe1 = Def()
    def compute_strategy(self,state,player,teamid):
        # variables
        g = state.get_goal_center(self.getad(teamid)) 
        b = state.ball.position
        p = player.position
        #direct  = (b + state.ball.speed ) + g
        bi = b + state.ball.speed
        x = 0.01 * GAME_WIDTH
        bp=b-p
        #dist = bi + g
        #d = Vector2D((dist.x)/2.0, (GAME_HEIGHT*0.5) + 0.75*(bi.y-(GAME_HEIGHT*0.5)))
        #dirt = d - p
       
        # cage 
        # les coins ou il vise
        p2 = (GAME_HEIGHT/2.0+GAME_GOAL_HEIGHT/2.0) + BALL_RADIUS
        p1 = (GAME_HEIGHT/2.0-GAME_GOAL_HEIGHT/2.0) - BALL_RADIUS
                
         #distances
        #gb = g - b   
        gp = g-p
        
        # ballon proche des cages
        if bp.norm < 15 and b.x < 20 and need.CanIshoot (state,player):
            shoot = Vector2D.create_polar(player.angle+2.0,g.norm)
            d = b - p
            return SoccerAction(d, shoot)
        # ballon au milieu, à peu pres
        if (bi.y > ((GAME_HEIGHT*0.5) - 2) and bi.y < ((GAME_HEIGHT*0.5) + 2) ):
            return self.defe1.compute_strategy(state,player,teamid)
        # ballon au dessus de la moitie de la largeur du terrain
        if (b.y <= (GAME_HEIGHT*0.5)+2):
            if b.y > p1 :
                if bi.y >= p1:
                    direct = Vector2D(x,p1)-p
                    shoot = Vector2D.create_polar(gp.angle + 2.505, 15)
                    return SoccerAction(direct,shoot)
                else :
                    return self.defe.compute_strategy(state,player,teamid)
            else :
                return self.deg.compute_strategy(state,player,teamid)
        # ballon en dessous de la moitie de la largeur du terrain
        else :
            if b.y < p2 and b.y >= (GAME_HEIGHT*0.5)-2:
                if bi.y <= p2:
                    direct = Vector2D(x,p2)- p
                    shoot = Vector2D.create_polar(gp.angle - 2.505, 15)
                    return SoccerAction(direct,shoot)
                else :
                    return self.defe.compute_strategy(state,player,teamid)
            else :
                return self.deg.compute_strategy(state,player,teamid)
        
        if not need.CanIshoot (state,player):
            dirt = b - p
            dirt.x = x
            return SoccerAction(dirt,Vector2D())
            
    def create_strategy(self):
        return DefGoalP()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2 