from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from outils import *

team1=SoccerTeam("Poireaux")
team1.add_player(SoccerPlayer("t1j1",DegageTer()))

team4=SoccerTeam("Carottes")
team4.add_player(SoccerPlayer("t4j2",MixSimple()))

team2=SoccerTeam("Patates")
team2.add_player(SoccerPlayer("t2j1",Degage()))
team2.add_player(SoccerPlayer("t2j2",Defenseur()))

team6=SoccerTeam("Oignons")
team6.add_player(SoccerPlayer("t6j1",Defenseur()))
team6.add_player(SoccerPlayer("t6j2",DegageTer()))

team3=SoccerTeam("Aubergines")
team3.add_player(SoccerPlayer("t3j1",Defenseur()))
team3.add_player(SoccerPlayer("t3j2",Def()))
team3.add_player(SoccerPlayer("t3j3",DeGoal()))
team3.add_player(SoccerPlayer("t3j4",DegageTer()))


team5=SoccerTeam("Tomates")
team5.add_player(SoccerPlayer("t5j2",DegageTer()))
team5.add_player(SoccerPlayer("t5j1",DefenGoal()))
team5.add_player(SoccerPlayer("t5j3",Def()))
team5.add_player(SoccerPlayer("t5j4",Attaquant()))

teams = [team1, team2, team3,team4,team5,team6]
#if __name__== "__main__":
#	battle=SoccerBattle(team1,team1.copy())
	#obs=PygletObserver()
	#obs.set_soccer_battle(battle)
	#pyglet.app.run()

