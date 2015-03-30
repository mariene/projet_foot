# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:35:35 2015

@author: 3202002
"""

from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from soccersimulator import TreeIA, TreeStrategy
from stratatt import *
from stratdef import *
from stratmix import *
from outils import *
from apprentissage import *

team3=SoccerTeam("team1")
team5=SoccerTeam("team2")

#team5.add_player(SoccerPlayer("FS",comp))
#team5.add_player(SoccerPlayer("DT",comp))
#team5.add_player(SoccerPlayer("DC",DefenseurBis()))
#team5.add_player(SoccerPlayer("MS",Attaquant()))

###############################################################################
# apprentissage
team_tree = SoccerTeam("Team Tree")
treeia=TreeIA(gen_feature_simple,dict({"DefenseurBis":DefenseurBis(),"CoinHaut":CoinHaut(),"CoinBas":CoinBas(),"Haut":Haut(),"Bas":Bas()}))

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"defenseurcoin2.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

team5.add_player(SoccerPlayer("DC",TreeST))
team5.add_player(SoccerPlayer("Att2",Attaquant()))
team5.add_player(SoccerPlayer("Att",Attaquant()))
team5.add_player(SoccerPlayer("Tree 2",Def()))

compo=ComposeStrategy(SurMemeLigneBis(),Rd())
team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("G",compo))
team_tree.add_player(SoccerPlayer("DT",DegageTer()))
team_tree.add_player(SoccerPlayer("Def",Def()))

battle=SoccerBattle(team_tree,team5)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 