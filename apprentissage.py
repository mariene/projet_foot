from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pickle
import os

from soccersimulator import SoccerStrategy
from strats import *


#list_fun_features=[distance_ball,distance_mon_but,distance_autre_but,distance_ball_mon_but,distance_ball_autre_but]

def gen_feature_simple(state,teamid,playerid):
    n = Need(state,teamid,state.get_player(teamid,playerid))
    l = [n.gadvp_norm(),n.gadvb_norm(),n.gp_norm,n.bp_norm(),n.gpad_norm(),gb_norm]
    return np.array(l)
#    return np.array([f(state,teamid,playerid) for f in list_fun_features])
