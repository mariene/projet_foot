from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam

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
