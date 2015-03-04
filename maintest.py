# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 17:04:17 2015
@author: 3202002
"""
from soccersimulator import Vector2D,SoccerState,SoccerAction,SoccerStrategy,SoccerBattle,SoccerPlayer,SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener, pyglet
from outils import *

team5=SoccerTeam("team1")
#team3=SoccerTeam("team2")
#team1=SoccerTeam("team1")
team2=SoccerTeam("team2")

#team1.add_player(SoccerPlayer("t1j1",Attaquant()))
#team1.add_player(SoccerPlayer("t1j2",Degage()))
#team1.add_player(SoccerPlayer("t1j3",PasBouger()))
#team1.add_player(SoccerPlayer("t1j4",PasBouger()))


comp=ComposeStrategy(AllerVersAdv(),TirerRd())
compo=ComposeStrategy(AllerVersBalle(),PasTirerVersAdv())

team2.add_player(SoccerPlayer("t2j2",DegageTer()))
#team2.add_player(SoccerPlayer("t2j1",compo))
#team2.add_player(SoccerPlayer("attaq",Attaquant()))
team2.add_player(SoccerPlayer("t2j4",Defenseur()))

#team3.add_player(SoccerPlayer("DefC",DefCyclique()))
#team3.add_player(SoccerPlayer("Def1",Defenseur()))
#team3.add_player(SoccerPlayer("MixS",MixSimple()))
#team3.add_player(SoccerPlayer("Deg",Degage()))

#team5.add_player(SoccerPlayer("DeG",TirLucarne()))
team5.add_player(SoccerPlayer("DefenG",DeGoal()))
team5.add_player(SoccerPlayer("Def",MixSimple()))
#team5.add_player(SoccerPlayer("comp",DefGoalP()))

battle=SoccerBattle(team2,team5)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run() 
