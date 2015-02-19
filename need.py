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
def aBallon(id,state):   
    if (id==1):
        for p in state.team1.player:
             if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                 return p.position
             else:
                  for p in state.team2.player:
                      if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                          return p.position
    else : 
        for p in state.team2.player:
             if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                 return p.position
             else:
                 for p in state.team2.player:
                      if ((p.distance(need.b)<(PLAYER_RADIUS+BALL_RADIUS))):
                          return p.position
