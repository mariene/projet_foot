# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:58:05 2015

@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS,BALL_RADIUS,GAME_WIDTH,GAME_HEIGHT
import random
import need
from math import pi 

#STRAT' DE BASE
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
            shoot = state.get_goal_center(need.get(teamid)) - p
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
        self.strat.point= state.get_goal_center(self.need.get(teamid))
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
        p = player.position
        shoot = Vector2D()
        padv = need.posPlayeradv(teamid,state,player)
        direct= padv - p
        #direct = Vector2D(padv.x + spadv + p.x, p.y+padv.y)
        return SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  

class AllerVersJoueur(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        shoot = Vector2D()
        pos = need.posPlayerEq(teamid,state,player)
        direct= pos - p
        #direct = Vector2D(padv.x + spadv + p.x, p.y+padv.y)
        return SoccerAction(direct,shoot)
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
        shoot = self.point - player.position
        dist = Vector2D()
        return SoccerAction(dist,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass        
    
         
class TirerVersBut(Tirer):
    def __init__(self):
        Tirer.__init__(self)
    def compute_strategy(self,state,player,teamid):
        self.point = state.get_goal_center(need.get(teamid))       
        return Tirer.compute_strategy(self,state,player,teamid) 
    

class TirerVersButBis(SoccerStrategy):
    def __init__(self):
        self.strat = Tirer()
    def compute_strategy(self,state,player,teamid):
        self.strat.point = state.get_goal_center(need.get(teamid))
        return self.strat.compute_strategy(state,player,teamid)
    
    
#tire n'importe ou
class TirerRd(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.get(teamid))
        #b = state.ball.position
        ##gb = state.get_goal_center(self.get(teamid)) - player.position
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

#tirer vers un joueur -> a developper
class TirerVersP(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        #self.point= state.get_player(self.teamid) 
        pos = need.posPlayerEq(teamid,state,player)
        shoot = pos - player.position 
        return SoccerAction(Vector2D(),shoot)
        
        
# a peu près le meme genre que Aleatoire sauf qu'il n'y a pas de direction
# tirerRd mais plus "orienter"
class AleatoireBis(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        gb = state.get_goal_center(need.get(teamid)) - player.position
        shoot = Vector2D.create_polar(gb.angle + random.uniform(-1,1),5)
        return SoccerAction(Vector2D(),shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass 

def PasTirerVersAdv(Soccerstrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        #positions
        gp = state.get_goal_center(need.get(teamid)) - player.position
        padv = need.posPlayeradv(teamid,state,player)
        gpadv = state.get_goal_center(need.get(teamid)) - padv
        #shoot
        if (gp.norm < gpadv.norm):
            shoot = Vector2D.create_polar(gb.angle + 2,5)
            return SoccerAction(Vector2D(),shoot)
        else :
            shoot = state.get_goal_center(need.get(teamid))
            return SoccerAction(Vector2D(),shoot)
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
#STRAT'
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
        return SoccerAction(dirt,shoot)
    def create_strategy(self):
        return Defenseur()
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

###############################################################################
#STRAT 
#attaque

#tire aleatoirement mais plus genre dribble mais plus loin (shoot loin)
class Aleatoire(SoccerStrategy):
    def __init__(self):
        pass
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(need.get(teamid))
        b = state.ball.position
        dist= b - player.position
        gb = state.get_goal_center(need.get(teamid)) - player.position
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
        self.bal= ComposeStrategy(AllerVersBalle(),TirerRd())
        self.fonce = FonceurStrategy()
        self.ale = ComposeStrategy(AllerVersBalle(),Aleatoire())
    def compute_strategy(self,state,player,teamid):
        g = state.get_goal_center(self.getad(teamid))
        gadv = state.get_goal_center(need.get(teamid))
        b = state.ball.position
        gadvb = gadv - b
        #dist= b - player.position
        gb = g - b   
        if ((b.x==GAME_WIDTH/2.0 and b.y==GAME_HEIGHT/2.0) or (gadvb.norm < GAME_WIDTH/6.0)): 
            return self.bal.compute_strategy(state,player,teamid)
        elif gb.norm < GAME_WIDTH/8.0:
            return self.ale.compute_strategy(state,player,teamid)
        else:
            return self.fonce.compute_strategy(state,player,teamid)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

class Degage(SoccerStrategy):
    def __init__(self):        
        pass
    def compute_strategy(self,state,player,teamid):
        p = player.position
        b = state.ball.position
        shoot = Vector2D()
        direct = (state.ball.position + state.ball.speed) - p
        direct.product(10)
        if ((p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS))):
            shoot = state.get_goal_center(need.get(teamid)) - p
            return SoccerAction(direct,shoot)
        return  SoccerAction(direct,shoot)
    def start_battle(self,state):
        pass        
    def finish_battle(self,won):
        pass  



class DegageBis(SoccerStrategy):
    def __init__(self):        
        pass
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
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

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
        b = state.ball.position
        p = player.position
        bp = b - p
        g = state.get_goal_center(self.getad(teamid))
        gb= g - b
        if gb.norm < (0.50 * GAME_WIDTH ) : 
            return self.defe.compute_strategy(state,player,teamid)
            if (p.distance(b)<(PLAYER_RADIUS+BALL_RADIUS)) or bp.norm < 15:
                return self.att2.compute_strategy(state,player,teamid)
        if gb.norm == (0.20 * GAME_WIDTH ):
            return self.compo.compute_strategy(state,player,teamid)
            #return self.att.compute_strategy(state,player,teamid) 
        else: 
            return self.att.compute_strategy(state,player,teamid)                                    
    def create_strategy(self):
        return Mix()
    def getad(self,teamid):
        if(teamid == 1):
            return 1
        else:
            return 2

# marche ! def au debut puis attaque quand a le ballon 
# trouver moyens -> fonce d'abord pour voir si peut choper le ballon 
# si oui attaque sinon defenseur et qd a le ballon va vers camp adverse 
class MixSimple(SoccerStrategy):
    def __init__(self):
        self.att= Attaquant()
        self.defe = Defenseur()
    def compute_strategy(self,state,player,teamid):
        b = state.ball.position
        p = player.position
        bp= b - p
        if bp.norm < 10 :
            return self.att.compute_strategy(state,player,teamid)
        return self.defe.compute_strategy(state,player,teamid)                  
    def create_strategy(self):
        return MixSimple()

