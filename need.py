from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam

def get(self,teamid):
        if(teamid == 1):
            return 2
        else:
            return 1

def g(self, teamid):
    return state.get_goal_center(self.get(teamid))

def b(self):
    return state.ball.position

def p (self):
    return player position

def gb (self):
    return state.get_goal_center(self.get(teamid)) - player.position

def bp (self):
    return state.ball.position - player.position
