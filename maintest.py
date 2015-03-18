# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015
@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from stratatt import *
from stratdef import *
from stratmix import *
from outils import *

team3=SoccerTeam("team1")
#team3=SoccerTeam("team2")
#team1=SoccerTeam("team1")
team5=SoccerTeam("team2")

#team1.add_player(SoccerPlayer("t1j1",Attaquant()))
#team1.add_player(SoccerPlayer("t1j2",Degage()))
#team1.add_player(SoccerPlayer("t1j3",PasBouger()))
#team1.add_player(SoccerPlayer("t1j4",PasBouger()))


comp=ComposeStrategy(AllerVersJoueurBis(),TirerRd())
compo=ComposeStrategy(AllerVersBalle(),PasVersToi())

# bonne equipe voir si je la change avec tomate ou aubergine 
#team2.add_player(SoccerPlayer(";)",DegageTer()))
#team2.add_player(SoccerPlayer("t2j1",DeGoal()))
#team2.add_player(SoccerPlayer("attaq",Def()))
#team2.add_player(SoccerPlayer("def",Defenseur()))


#team3.add_player(SoccerPlayer("Def2",DegageTer()))
#team3.add_player(SoccerPlayer("Def",DefenseurBis()))
team3.add_player(SoccerPlayer("Att",comp))
#team3.add_player(SoccerPlayer("Def1",DefBis()))
#team3.add_player(SoccerPlayer("MixS",MixSimple()))
team3.add_player(SoccerPlayer("Deg",FonceurStrategy()))

#team5.add_player(SoccerPlayer("FS",comp))
#team5.add_player(SoccerPlayer("DT",comp))
team5.add_player(SoccerPlayer("DC",DefenseurBis()))
team5.add_player(SoccerPlayer("MS",Attaquant()))

#list_key_player1=['a','z']
#list_key_player2=['q','s']
#list_strat_player1=[DefenseurBis(),FonceurStrategy(),DegageTer(),]
#list_strat_player2=[RandomStrategy(),FonceurStrategy()]

# arguemnts :  liste des touches, liste des strategies, nom du fichier, tout sauvegarder ou non, concatener dans un meme fichier a la suite ou non
#inter_strat_player1=InteractStrategy(list_key_player1,list_strat_player1,"test_interact.pkl")
#inter_strat_player2=InteractStrategy(list_key_player2,list_strat_player2,"test_interact.pkl",True)
#team3 = SoccerTeam("Interactive")
#team3.add_player(SoccerPlayer("Inter 1",inter_strat_player1))
#team3.add_player(SoccerPlayer("Inter 2",inter_strat_player2))

#team_tree = SoccerTeam("Team Tree")
#team_tree.add_player(SoccerPlayer("Tree 1",FirstTreeStrategy()))
#team_tree.add_player(SoccerPlayer("Tree 2",FirstTreeStrategy()))
#teams =[team1,team2,team3,team_tree]


battle=SoccerBattle(team5,team3)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 
