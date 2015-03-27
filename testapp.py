# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:47:14 2015

@author: 3202002
"""


from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet, InteractStrategy, TreeStrategy
from stratatt import *
from stratdef import *
from stratmix import *
from outils import *
from apprentissage import *

team3=SoccerTeam("team1")
team5=SoccerTeam("team2")

team_tree = SoccerTeam("Team Tree")
treeia=TreeIA(gen_feature_simple,dict({"DefenseurBis":DefenseurBis(),"CoinHaut":CoinHaut(),"CoinBas":CoinBas(),"Haut":Haut(),"Bas":Bas(),"Rd":Rd()}))

fn=os.path.join(os.path.dirname(os.path.realpath(__file__)),"defenseurcoin.pkl")
treeia.load(fn)
TreeST=TreeStrategy("tree1",treeia)

#team5.add_player(SoccerPlayer("DC",TreeST))
#team5.add_player(SoccerPlayer("FS",comp))
#team5.add_player(SoccerPlayer("DT",comp))
#team5.add_player(SoccerPlayer("Def",MixSimple()))
team5.add_player(SoccerPlayer("MS",DegageTer()))

###############################################################################
# apprentissage
list_key_player1=['s','z','x','d','q']
list_strat_player1=[DefenseurBis(),CoinHaut(),CoinBas(),Haut(),Bas()]
inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"Def_DegTer1")

team3 = SoccerTeam("Interactive")
team3.add_player(SoccerPlayer("Inter 1",inter_strat_player1))
#team3.add_player(SoccerPlayer("DT",Degage()))


battle=SoccerBattle(team3,team5)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 