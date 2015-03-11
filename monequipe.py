from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from stratatt import *
from stratdef import *
from stratmix import *

team1=SoccerTeam("Poireaux")
team1.add_player(SoccerPlayer("t1j1",DegageTer()))

team4=SoccerTeam("Carottes")
team4.add_player(SoccerPlayer("t4j2",MixSimple()))

team2=SoccerTeam("Patates")
team2.add_player(SoccerPlayer("t2j1",Degage()))
team2.add_player(SoccerPlayer("t2j2",DefenseurBis()))

team6=SoccerTeam("Oignons")
team6.add_player(SoccerPlayer("t6j1",DefenseurBis()))
team6.add_player(SoccerPlayer("t6j2",DegageTer()))

team3=SoccerTeam("Aubergines")
team3.add_player(SoccerPlayer("t3j1",DefenseurBis()))
team3.add_player(SoccerPlayer("t3j2",DefBis()))
team3.add_player(SoccerPlayer("t3j3",DeGoalBis()))
team3.add_player(SoccerPlayer("t3j4",DegageTer()))


team5=SoccerTeam("Tomates")
team5.add_player(SoccerPlayer("t5j2",DegageTer()))
team5.add_player(SoccerPlayer("t5j1",DefenGoalBis()))
team5.add_player(SoccerPlayer("t5j3",DefBis()))
team5.add_player(SoccerPlayer("t5j4",Attaquant()))

teams = [team1, team2, team3,team4,team5,team6]
#if __name__== "__main__":
#	battle=SoccerBattle(team1,team1.copy())
	#obs=PygletObserver()
	#obs.set_soccer_battle(battle)
	#pyglet.app.run()

