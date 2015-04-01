# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015
@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from soccersimulator import*
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


comp=ComposeStrategy(SurMemeLigneHorizHaut(),TirerVersP())
compo=ComposeStrategy(AllerVersBalle(),Dribbler())
comp1=ComposeStrategy(SurMemeLigneHorizBas(),TirerVersP())
comp2=ComposeStrategy(AllerVersBalle(),AleatoireBis())
# bonne equipe voir si je la change avec tomate ou aubergine 
#team2.add_player(SoccerPlayer(";)",DegageTer()))
#team2.add_player(SoccerPlayer("t2j1",DeGoal()))
#team2.add_player(SoccerPlayer("attaq",Def()))
#team2.add_player(SoccerPlayer("def",Defenseur()))

#goal = ComposeStrategy(SurMemeLigneBis(),Rd())

#team3.add_player(SoccerPlayer("Def2",DegageTer()))
#team3.add_player(SoccerPlayer("pDef",comp1))
#team3.add_player(SoccerPlayer("Rd",Rd()))
team3.add_player(SoccerPlayer("Def1",DefenseurBis()))
team3.add_player(SoccerPlayer("MixS",MixSimple()))
#team3.add_player(SoccerPlayer("Deg",FonceurStrategy()))

team5.add_player(SoccerPlayer("FS",Degage()))
team5.add_player(SoccerPlayer("DT",Goal()))
#team5.add_player(SoccerPlayer("DC",DefBis()))
#team5.add_player(SoccerPlayer("MS",DefenseurBis()))


battle=SoccerBattle(team5,team3)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 
