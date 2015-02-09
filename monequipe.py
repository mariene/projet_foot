from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from strats import RandomStrategy,PStrategy,FonceurStrategy
#from outils import 

team1=SoccerTeam("team1")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))


team2=SoccerTeam("team2")
team2.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t2j2",FonceurStrategy()))

team3=SoccerTeam("team3")
team3.add_player(SoccerPlayer("t3j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t3j2",PStrategy()))
team3.add_player(SoccerPlayer("t3j3",FonceurStrategy()))
team3.add_player(SoccerPlayer("t3j4",PStrategy()))


teams = [team1, team2, team3]
#if __name__== "__main__":
#	battle=SoccerBattle(team1,team1.copy())
	#obs=PygletObserver()
	#obs.set_soccer_battle(battle)
	#pyglet.app.run()

