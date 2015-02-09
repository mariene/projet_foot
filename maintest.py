# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015

@author: 3202002
"""


from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from outils import AllerVers, AllerVersBalle,AllerVersBalleBis,Tirer,TirerVersBut, AllerVersBut,TirerVersP,PasBouger
from outils import ComposeStrategy

team1=SoccerTeam("team1")
team2=SoccerTeam("team2")
team1.add_player(SoccerPlayer("t1j1",AllerVersBalle()))
team2.add_player(SoccerPlayer("t2j1", AllerVers()))
team1.add_player(SoccerPlayer("t1j2",))
team2.add_player(SoccerPlayer("t2j2",AllerVersBut()))
battle=SoccerBattle(team1,team2)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 