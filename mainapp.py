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

treeia1=TreeIA(gen_feature_simple,dict({"DefBis":DefenseurBis(),"Haut":Haut(),"Bas":Bas()}))
fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"def_plusproche.pkl")
treeia1.load(fn)
TreeST1=TreeStrategy("tree2",treeia1)

treeia2=TreeIA(gen_feature_simple,dict({"DefBis":DefenseurBis(),"Degage":Degage(),"TirerCoinHaut":TirerCoinHaut(),"TirerCoinBas":TirerCoinBas(),"Haut":Haut(),"Bas":Bas()}))
fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"att2.pkl")
treeia2.load(fn)
TreeST2=TreeStrategy("tree3",treeia2)



compo=ComposeStrategy(SurMemeLigneBis(),Rd())
team5.add_player(SoccerPlayer("tree1",TreeST))
team5.add_player(SoccerPlayer("Att2",TreeST2))
team5.add_player(SoccerPlayer("Goal",compo))
team5.add_player(SoccerPlayer("Tree 2",TreeST1))


team_tree.add_player(SoccerPlayer("Tree 1",TreeST))
team_tree.add_player(SoccerPlayer("G",compo))
team_tree.add_player(SoccerPlayer("DT",DegageTer()))
team_tree.add_player(SoccerPlayer("Def",DefBis()))

battle=SoccerBattle(team_tree,team5)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 