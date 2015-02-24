# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015
@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from outils import *

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")

team1.add_player(SoccerPlayer("t1j1",Def()))
#team1.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
#team1.add_player(SoccerPlayer("t1j3",Attaquant()))
team1.add_player(SoccerPlayer("t1j4",DeGoal()))


comp=ComposeStrategy(AllerVersBalle(),TirerRd())
compo=ComposeStrategy(AllerVersBalle(),AleatoireBis())



team2.add_player(SoccerPlayer("t2j2",Defenseur()))
#team2.add_player(SoccerPlayer("t2j1",Goal()))
#team2.add_player(SoccerPlayer("t2j3",compo))
team2.add_player(SoccerPlayer("t2j4",Def()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 
