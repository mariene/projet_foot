# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015

@author: 3202002
"""


from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from outils import AllerVers, AllerVersBalle,AllerVersBalleBis,Tirer,TirerVersBut, AllerVersBut,TirerVersP,PasBouger
from outils import ComposeStrategy,FonceurStrategy,Defenseur,RandomStrategy,TirerRd

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")

team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j2",Defenseur()))
team1.add_player(SoccerPlayer("t1j3",FonceurStrategy()))
team1.add_player(SoccerPlayer("t1j4",Defenseur()))

comp=ComposeStrategy(AllerVersBut(),TirerVersBut())

team2.add_player(SoccerPlayer("t2j2",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j3",Defenseur()))
team2.add_player(SoccerPlayer("t2j4",FonceurStrategy()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 