from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PLAYER_RADIUS, BALL_RADIUS

def get(id):
        if(id == 1):
            return 2
        else:
            return 1

def g(id, state):
    return state.get_goal_center(self.get(teamid))

def b(id, state):
    return state.ball.position

def p (id, state):
    return player.position

def gp (id, state):
    return state.get_goal_center(self.get(teamid)) - player.position
  
def gb(id, state):  
    return state.get_goal_center(self.get(teamid)) - state.ball.position

def bp (id, state):
    return state.ball.position - player.position

# a developper, pour savoir quel joueur a le ballon  
# un joueur -> si choix 0 cherche si quelqu'un de son equipe a le ballon / 
#si choix 1 cherche si quelqu'un de l'equipe adverse a le ballon 

def aBallon(id,state,player,choix):   
    if (id==1 and choix == 0 ):
        for p in state.team1.players:
            if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                return p.position
    elif (id == 1 and choix == 1):
        for p in state.team2.players:
            if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                return p.position
    if (id ==2 and choix == 0  ):
        for p in state.team2.players:
            if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                return p.position
    else:
        for p in state.team1.players:
            if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                return p.position


def posPlayeradv(id,state,player): 
    pos = Vector2D()
    if (id==1):
        for p in state.team2.players:
            if (p.position.distance(player.position) < 30) :
                pos = p.position
        return pos
    else :
        for p in state.team1.players:
            if (p.position.distance(player.position) < 30 ) :
                pos = p.position
        return pos
        

def Playeradv(id,state,player): 
    if (id==1):
        for p in state.team2.players:
            if (p.position.distance(player.position) < 50) :
                return True
    else :
        for p in state.team1.players:
            if (p.position.distance(player.position) < 50 ) :
                return True