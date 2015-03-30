# -*- coding: utf-8 -*-
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS

class Need(SoccerState):   
    def __init__(self,state,teamid,player):
        self.teamid=teamid
        self.state=state
        self.player=player
        
    def get(self):
        if(self.teamid == 1):
            return 2
        else:
            return 1    
    def getad(self):
        if(self.teamid == 1):
            return 1
        else:
            return 2
    def g(self):
        return self.state.get_goal_center(get())
    def b(self):
        return self.state.ball.position
    def p(self):
        return self.player.position
     #but adverse-joueur   
    def gadvp(self):
        return self.state.get_goal_center(self.get()) - self.player.position     
    def gadvp_norm(self):
        return (self.state.get_goal_center(self.get()) - self.player.position).norm
    #but adverse - ballon    
    def gadvb(self):  
        return self.state.get_goal_center(self.get()) - self.state.ball.position
    def gadvb_norm(self):  
        return (self.state.get_goal_center(self.get()) - self.state.ball.position).norm
    #cage-joueur
    def gp(self):
        return self.state.get_goal_center(self.getad()) - self.player.position        
    def gp_norm(self):
        return (self.state.get_goal_center(self.getad()) - self.player.position).norm
#cage-ballon
    def gb(self):  
        return self.state.get_goal_center(self.getad()) - self.state.ball.position   
    def gb_norm(self):  
        return (self.state.get_goal_center(self.getad()) - self.state.ball.position).norm
#ballon-joueur
    def bp(self):
        return self.state.ball.position - self.player.position   
    def bp_norm(self):
        return (self.state.ball.position - self.player.position).norm        
#ballon-adversaire
    def bpadv(self):
        return self.state.ball.position - self.posPlayeradv()    
    def bpadv_norm(self):
        return (self.state.ball.position - self.posPlayeradv()).norm        
#but adverse - adversaire
    def gpadv_norm(self):
        return (self.state.get_goal_center(self.get()) - self.posPlayeradv()).norm    
    def posp (self): 
        #gpad_norm = (self.state.get_goal_center(self.get()) - self.posPlayeradv()).norm
        #gp_norm = (self.state.get_goal_center(self.getad()) - self.state.ball.position).norm
        if (self.gpadv_norm() > self.gp_norm()):
            return True
        else :
            return False
        
# a developper, pour savoir quel joueur a le ballon  
# un joueur -> si choix 0 cherche si quelqu'un de son equipe a le ballon / 
#si choix 1 cherche si quelqu'un de l'equipe adverse a le ballon 

    def aBallon(self,choix):  
        pos = Vector2D()
        
        if self.teamid==1 :
            if choix == 0 :
                for p in self.state.team1.players:
                    if (self.state.ball.position - p.position).norm <=(PLAYER_RADIUS+BALL_RADIUS):
                        pos =  p.position
                return pos
            else :
                for p in self.state.team2.players :
                    if (self.state.ball.position - p.position).norm <=(PLAYER_RADIUS+BALL_RADIUS):
                        pos = p.position
                return pos
        else : 
            if choix == 0:
                for p in self.state.team2.players:
                    if (self.state.ball.position - p.position).norm<=(PLAYER_RADIUS+BALL_RADIUS):
                        pos = p.position
                return pos
            else:
                for p in self.state.team1.players:
                    if (self.state.ball.position - p.position).norm <=(PLAYER_RADIUS+BALL_RADIUS):
                        pos= p.position
                return pos

#si adversaire a le ballon
    def posPlayeradvBall(self): 
        pos = Vector2D()
        if (self.teamid==1):
            for p in self.state.team2.players:
                if (self.state.ball.position - p.position).norm <=(PLAYER_RADIUS+BALL_RADIUS) :
                    pos = p.position
            return pos
        else :
            for p in self.state.team1.players:
                if (self.state.ball.position - p.position).norm <=(PLAYER_RADIUS+BALL_RADIUS):
                    pos = p.position
            return pos 

# position des joueurs adverse
    def posPlayeradv(self): 
        pos = Vector2D()
        #sp =0.0
        if (self.teamid==1):
            for p in self.state.team2.players:
                if (p.position.distance(self.player.position) < 30) :
                    pos = p.position
                    #sp = p.speed
            return pos#,sp
        else :
            for p in self.state.team1.players:
                if (p.position.distance(self.player.position) < 30 ) :
                    pos = p.position
                    #sp = p.speed
            return pos #,sp
        
# position des joueurs de mon equipe        
    def posPlayerEq(self): 
        pos = Vector2D()
        if (self.teamid==1):
            for p in self.state.team1.players:
                if (p.position.distance(self.player.position) < 30) :
                    pos = p.position
                #sp = p.speed
            return pos
        else :
            for p in self.state.team2.players:
                if (p.position.distance(self.player.position) < 30 ) :
                    pos = p.position
               # sp = p.speed
            return pos

    def Playeradv(self): 
        if (self.teamid==1):
            for p in self.state.team2.players:
                if (p.position.distance(self.player.position) < 50) :
                    return True
        else :
            for p in self.state.team1.players:
                if (p.position.distance(self.player.position) < 50 ) :
                    return True

    def CanIshoot (self):
        p = self.player.position
        if (p.distance(self.state.ball.position)<=(PLAYER_RADIUS+BALL_RADIUS)):
            return True
        else :
            return False
    