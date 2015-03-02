# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015
@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from outils import *

team5=SoccerTeam("team1")
team3=SoccerTeam("team2")
#team1=SoccerTeam("team1")
#team2=SoccerTeam("team2")

#team1.add_player(SoccerPlayer("t1j1",Attaquant()))
#team1.add_player(SoccerPlayer("t1j2",Degage()))
#team1.add_player(SoccerPlayer("t1j3",PasBouger()))
#team1.add_player(SoccerPlayer("t1j4",PasBouger()))


comp=ComposeStrategy(AllerVersAdv(),TirerRd())
compo=ComposeStrategy(AllerVersBalle(),PasTirerVersAdv())

#team2.add_player(SoccerPlayer("t2j2",Def()))
#team2.add_player(SoccerPlayer("t2j1",Degage()))
#team2.add_player(SoccerPlayer("t2j3",Attaquant()))
#team2.add_player(SoccerPlayer("t2j4",DefCyclique()))

#team3.add_player(SoccerPlayer("t3j1",DefCyclique()))
team3.add_player(SoccerPlayer("t3j2",Defenseur()))
team3.add_player(SoccerPlayer("t3j3",MixSimple()))
#team3.add_player(SoccerPlayer("t3j4",FonceurStrategy()))

#team5.add_player(SoccerPlayer("t5j2",Degage()))
#team5.add_player(SoccerPlayer("t5j1",Def()))
team5.add_player(SoccerPlayer("t5j3",comp))
team5.add_player(SoccerPlayer("t5j4",compo))

battle=SoccerBattle(team3,team5)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 
