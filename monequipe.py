from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from outils import ComposeStrategy,FonceurStrategy,Defenseur
#from outils import 

team1=SoccerTeam("Poireau")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))


team2=SoccerTeam("Patate")
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",FonceurStrategy()))

team3=SoccerTeam("Aubergine")
team3.add_player(SoccerPlayer("t3j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t3j2",Defenseur()))
team3.add_player(SoccerPlayer("t3j3",Defenseur()))
team3.add_player(SoccerPlayer("t3j4",FonceurStrategy()))

team4=SoccerTeam("Carotte")
team4.add_player(SoccerPlayer("t4j2",FonceurStrategy()))
team4.add_player(SoccerPlayer("t4j1",FonceurStrategy()))
team4.add_player(SoccerPlayer("t4j3",Defenseur()))
team4.add_player(SoccerPlayer("t4j4",FonceurStrategy()))

teams = [team1, team2, team3, team4]
#if __name__== "__main__":
#	battle=SoccerBattle(team1,team1.copy())
	#obs=PygletObserver()
	#obs.set_soccer_battle(battle)
	#pyglet.app.run()

