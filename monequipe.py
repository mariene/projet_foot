from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from outils import *

team1=SoccerTeam("Poireaux")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))


team2=SoccerTeam("Patates")
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",Defenseur()))

#team6=SoccerTeam("Artichauts")
#team6.add_player(SoccerPlayer("t6j1",Mix()))
#team6.add_player(SoccerPlayer("t6j2",FonceurStrategy()))

team3=SoccerTeam("Aubergines")
team3.add_player(SoccerPlayer("t3j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t3j2",Defenseur()))
team3.add_player(SoccerPlayer("t3j3",Defenseur()))
team3.add_player(SoccerPlayer("t3j4",FonceurStrategy()))

#team4=SoccerTeam("Carottes")
#team4.add_player(SoccerPlayer("t4j2",FonceurStrategy()))
#team4.add_player(SoccerPlayer("t4j1",Aleatoire()))
#team4.add_player(SoccerPlayer("t4j3",Defenseur()))
#team4.add_player(SoccerPlayer("t4j4",FonceurStrategy()))

team5=SoccerTeam("Tomates")
team5.add_player(SoccerPlayer("t5j2",FonceurStrategy()))
team5.add_player(SoccerPlayer("t5j1",Mix()))
team5.add_player(SoccerPlayer("t5j3",Defenseur()))
team5.add_player(SoccerPlayer("t5j4",FonceurStrategy()))

teams = [team1, team2, team3,team5]
#if __name__== "__main__":
#	battle=SoccerBattle(team1,team1.copy())
	#obs=PygletObserver()
	#obs.set_soccer_battle(battle)
	#pyglet.app.run()

