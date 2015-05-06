# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:58:05 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT,GAME_GOAL_HEIGHT
import random
from need import *
from math import pi 

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

###############################################################################   
#ALLER VERS / DEPLACEMENT
# Aller vers un point
class AllerVers (SoccerStrategy):
    def __init__(self):
        self.point=Vector2D()
    def compute_strategy(self,state,player,teamid):
        shoot=Vector2D()
        dist = self.point - player.position
        dist.product(10)
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

class AllerVersBalleFut (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        self.strat.point= state.ball.position + state.ball.speed       
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

#Aller vers but 
class AllerVersBut (SoccerStrategy):
    def __init__(self):
        self.strat= AllerVers()
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        self.strat.point= state.get_goal_center(need.get())
        return self.strat.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  


# joueur va vers le joueur adverse     
# a developper -> se positionner a l'endroit où il va etre si possible       
class AllerVersAdv(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        #p = player.position
        need = Need(state, teamid, player)
        shoot = Vector2D()
        padv= need.posPlayeradv()
        #padv =  Vector2D(padv.x+1.0, padv.y+1.0)
        direct= padv - player.position
        #direct = Vector2D((padvp.x/2.0),(padvp.y/2.0))
        if padv == Vector2D() :
            direct = Vector2D()
            return SoccerAction(direct,shoot)
        return SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

# PB /!\ sachant que maintenant avec la nouvelle config la balle va loin donc n'est pas sur que c'est 
# l'adversaire qui a la balle car il peut l'avoir shooter loin mais le recup apres, ce qui fait que le 
#joueur ne peut pas totalement le suivre 
class AllerVersAdvBis(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        #p = player.position
        need = Need(state, teamid, player)
        shoot = Vector2D()
        padv = need.posPlayeradvBall()
        direct = padv - player.position
        if padv == Vector2D() :
            direct = state.ball.position - player.position
            return SoccerAction(direct,shoot)
        else :       
            return SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass

class AllerVersJoueur(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        shoot = Vector2D()
        pos = need.posPlayerEq()
        direct= pos - p
        #direct = Vector2D(padv.x + spadv + p.x, p.y+padv.y)
        return SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class AllerVersJoueurBis(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        shoot = Vector2D()
        pos = need.aBallon(0)
        direct= pos - p
        #direct = Vector2D(padv.x + spadv + p.x, p.y+padv.y)
        if pos == Vector2D() :
            direct = state.ball.position - player.position
            return SoccerAction(direct,shoot)
        else :       
            return SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
        
        
class AllerVersCoinBas(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = (GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2) + 0.5 
        if teamid == 1:
            direct = Vector2D(0.75,p)-player.position
        else :
            direct = Vector2D(GAME_WIDTH-1.0,p)-player.position
        return SoccerAction(direct,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class AllerVersCoinHaut(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = (GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2) - 0.5
        if teamid == 1:
            direct = Vector2D(0.75,p)-player.position
        else :
            direct = Vector2D(GAME_WIDTH-1.0,p)-player.position
        return SoccerAction(direct,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class SurMemeLigne(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position 
        l = (GAME_WIDTH*0.05)+GAME_WIDTH*0.5
        pos = Vector2D(l,b.y)-player.position
        if teamid == 1:
            l = GAME_WIDTH*0.05
            pos = Vector2D(l,b.y)-player.position
            return SoccerAction(pos,Vector2D())
        else :
            return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class SurMemeLigneBis(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position + state.ball.speed
        l = -(GAME_WIDTH*0.015)+GAME_WIDTH
        pos = Vector2D(l,b.y)-player.position
        if teamid == 1:
            l = GAME_WIDTH*0.015
            pos = Vector2D(l,b.y)-player.position
            return SoccerAction(pos,Vector2D())
        else :
            return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class SurMemeLigneHorizHaut(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position + state.ball.speed
        l = GAME_HEIGHT/2.0 - 5
        pos = Vector2D(b.x,l)-player.position
        return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class SurMemeLigneHorizBas(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position + state.ball.speed
        l = GAME_HEIGHT/2.0 + 5
        pos = Vector2D(b.x,l)-player.position
        return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass


class Avancer(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        pos = Vector2D(p.x+5.0,p.y)-p
        return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass      

class Reculer(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        pos = Vector2D(p.x-5.0,p.y)-p
        return SoccerAction(pos,Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass    

###############################################################################
#TIRER VERS
#tirer vers un point       
class Tirer (SoccerStrategy):
    def __init__(self):
        self.point = Vector2D()
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        shoot = self.point - player.position
        dist = Vector2D()
        if need.CanIshoot():
            return SoccerAction(dist,shoot)
        else :
            return SoccerAction(dist,dist)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        
    
         
class TirerVersBut(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        self.point = state.get_goal_center(need.get())       
        return Tirer.compute_strategy(self,state,player,teamid) 
    

class TirerVersButBis(SoccerStrategy):
    def __init__(self):
        self.strat = Tirer()
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        self.strat.point = state.get_goal_center(need.get())
        return self.strat.compute_strategy(state,player,teamid)
    
    
#tire n'importe ou
class TirerRd(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        g = state.get_goal_center(self.get(teamid))
        #b = state.ball.position
        ##gb = state.get_goal_center(self.get(teamid)) - player.position
        #de=Vector2D.create_polar(player.angle, g.norm)
        dr= Vector2D.create_polar(player.angle+random.random(),g.norm)
        direc = Vector2D()   
        if need.CanIshoot():
            return SoccerAction(direc,dr)
        else:
            return SoccerAction(direc,direc)
    def create_strategy(self):
        return TirerRd()
    def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1 


#tirer vers un joueur -> a developper
class TirerVersP(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        #self.point= state.get_player(self.teamid) 
        need = Need(state, teamid, player)
        pos = need.posPlayerEq()
        #pos = Vector2D(pos.x,pos.y)
        shoot = pos - player.position 
        if need.CanIshoot():
            return SoccerAction(Vector2D(),shoot)
        return SoccerAction(Vector2D(),Vector2D())

        
        
# a peu près le meme genre que Aleatoire sauf qu'il n'y a pas de direction
# tirerRd mais plus "orienter"
class AleatoireBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        gb = state.get_goal_center(need.get()) - player.position
        shoot = Vector2D.create_polar(gb.angle + random.uniform(-1,1),3)
        if need.CanIshoot():
            return SoccerAction(Vector2D(),shoot)
        else :
            return SoccerAction(Vector2D(),Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class Dribbler(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        gb = state.get_goal_center(need.get()) - state.ball.position
        shoot = Vector2D.create_polar(gb.angle + random.random()*2-1,1.25)
        if need.CanIshoot():
            return SoccerAction(Vector2D(),shoot)
        else :
            return SoccerAction(Vector2D(),Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class PasTirerVersAdv(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state,teamid, player)
        gp = state.get_goal_center(need.get()) - player.position
        padv = need.posPlayeradv()
        gpadv = state.get_goal_center(need.get()) - padv
        if need.CanIshoot():
            if need.Playeradv():
                if (gp.norm < gpadv.norm):
                    shoot = Vector2D(3,3)
                    return SoccerAction(Vector2D(),shoot)
                else :
                    return SoccerAction(Vector2D(),gp)
            else :
            #shoot = state.get_goal_center(need.get(teamid))
                return SoccerAction(Vector2D(),gp)
        return SoccerAction(Vector2D(),Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class PasVersToi(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        b = state.ball.position 
        gp = state.get_goal_center(need.get() )- player.position
        #gb = state.get_goal_center(need.get(teamid)) - b
        padv= need.posPlayeradv()
        gpadv = state.get_goal_center(need.get()) - padv
        direct = Vector2D(0,0)
        b = state.ball.position 
        padvp = padv - player.position 
        if need.CanIshoot():
            if need.posp():      
                shoot = Vector2D.create_polar(gp.angle - pi/4.0, 40.0)
                return SoccerAction(direct,shoot)
            else :
                shoot = Vector2D.create_polar(gp.angle + pi/4.0, 40.0)
                return SoccerAction(direct,shoot)
        else:
            return SoccerAction(direct,direct)
        #else :
            #shoot = state.get_goal_center(need.get(teamid))
        #return SoccerAction(Vector2D(),gp)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

class TirerVersLeBas(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        gb = state.get_goal_center(need.get()) - player.position
        shoot = Vector2D.create_polar(gb.angle -pi/4.0,5)
        if need.CanIshoot():
            return SoccerAction(Vector2D(),shoot)
        else :
            return SoccerAction(Vector2D(),Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
    
class TirerVersLeHaut(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        gb = state.get_goal_center(need.get()) - player.position
        shoot = Vector2D.create_polar(gb.angle + pi/4.0,5)
        if need.CanIshoot():
            return SoccerAction(Vector2D(),shoot)
        else :
            return SoccerAction(Vector2D(),Vector2D())
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 


class TirerSurCH(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = Vector2D()
        p1 = (GAME_HEIGHT/2-GAME_GOAL_HEIGHT/2) + 0.25
        if need.CanIshoot():
            if (teamid == 2):
                v1 = Vector2D(0,p1)
                shoot = v1 - p
                return  SoccerAction(direct,shoot)                
            else :
                v1 = Vector2D(GAME_WIDTH,p1)
                shoot = v1 - p
                return  SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass     
    
    
    
class TirerSurCB(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        need = Need(state, teamid, player)
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = Vector2D()
        p2 = (GAME_HEIGHT/2+GAME_GOAL_HEIGHT/2) - 0.25
        if need.CanIshoot():
            if (teamid == 2):
                    v2 = Vector2D(0,p2)
                    shoot = v2 - p
                    return SoccerAction(direct,shoot)
            else :
                    v2 = Vector2D(GAME_WIDTH,p2)
                    shoot = v2 - p
                    return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 
###############################################################################            
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
    
###############################################################################    
#CHOSES UTILES
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

#class SelectorStrat(SoccerStrategy):
 #    def __init__(self):
  #      self.liststrat=[]
   #  def selector(self,state,player,teamid):
    #     if() return 
     #     ....
    #def compute_strategy(self,state,player,teamid):
     #   idx=selector()
      #  return self.liststrat[idx].(computestratstate,player,teamid) 
###############################################################################     

class SurMemeLigneBas(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position + state.ball.speed
        l = GAME_HEIGHT - 2
        pos =  state.ball.position - Vector2D(b.x,l)
        return SoccerAction(Vector2D(),pos)


class SurMemeLigneHaut(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position + state.ball.speed
        l = 2
        pos = state.ball.position - Vector2D(b.x,l)
        return SoccerAction(Vector2D(),pos)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass

###############################################################################
