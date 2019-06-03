#Name:Andrew Steele
#Major:CSIT
#Class:328_Network Programming
#StartDate:11/9/17
#DueDate: 11/30/17
#Instuctor:Dr. Frye
#Using Python 2.7

import socket
import os
import sys
###########################################	
#Confirms connection with 2 players
###########################################	
def initiation(p1, p2): 
	
	if (p1 == "PREPPED" and p2 == "PREPPED"): 
		return True 
	else: 
		return False 
###########################################	
#Sends players the OK to play
###########################################	
def play(players):
	
	ok = "OK" #OK="GO"
	players[0][0].send(ok.encode()) 
	players[1][0].send(ok.encode()) 
###########################################	
#Receilves the players scores from their choice from gameRules
###########################################	
def decisions(players, win_Loss):
	
	p1RPS = players[0][0].recv(1024) 
	p1RPS = p1RPS.decode() 
	p2RPS = players[1][0].recv(1024) 
	p2RPS = p2RPS.decode() 
	win_Loss = gameRules(p1RPS, p2RPS, win_Loss) 
	return win_Loss 
###########################################
#Sends the scores to the players	
###########################################	
def tally(players, win_Loss):
	
	player1Wins = win_Loss[0] 
	player2Wins = win_Loss[1] 
	draw = win_Loss[2] 
	
	player1Wins = str(player1Wins) 
	player2Wins = str(player2Wins) 
	draw = str(draw) 
	
	tally = "TALLY" #TALLY="SCORE"
	players[0][0].send(tally.encode()) 
	players[1][0].send(tally.encode()) 
###########################################	
#Player 1
###########################################		
	players[0][0].send(player1Wins.encode()) 
	players[0][0].send(player2Wins.encode()) 
	players[0][0].send(draw.encode()) 
###########################################
#Player 2
###########################################	
	players[1][0].send(player2Wins.encode()) 
	players[1][0].send(player1Wins.encode()) 
	players[1][0].send(draw.encode()) 
###########################################	
#Sends halt to end the game client side and stops server
###########################################	
	halt = "HALT" #HALT="STOP"
	players[0][0].send(halt.encode()) 
	players[1][0].send(halt.encode()) 
	
	sys.exit()

###########################################
#Game Rules/Win Conditions
###########################################	
def gameRules(p1RPS, p2RPS, win_Loss):
	
	player1Wins = win_Loss[0] 
	player2Wins = win_Loss[1] 
	draw = win_Loss[2] 
###########################################	
#Rock Win Conditions
###########################################	
	if (p1RPS == 'R' and p2RPS == 'R'): 
		print ("draw") 
		draw = draw + 1 
		
	elif (p1RPS =='R' and p2RPS == 'S'):
		print ("Player 1 victory" ) 
		player1Wins = player1Wins + 1 
		
	elif (p1RPS =='R' and p2RPS == 'P'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
        
	elif (p1RPS =='R' and p2RPS == 'L'):
		print ("Player 1 victory" ) 
		player1Wins = player1Wins + 1 
        
	elif (p1RPS =='R' and p2RPS == 'V'):
		print ("Player 2 victory" ) 
		player2Wins = player2Wins + 1 
###########################################	
#Paper Win Conditions
###########################################	
	elif (p1RPS == 'P' and p2RPS == 'R'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
		
	elif (p1RPS =='P' and p2RPS == 'S'):
		print ("Player 2 victory" ) 
		player2Wins = player2Wins + 1 
		
	elif (p1RPS =='P' and p2RPS == 'P'):
		print ("draw") 
		draw = draw + 1 
        
	elif (p1RPS == 'P' and p2RPS == 'L'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
        
	elif (p1RPS == 'P' and p2RPS == 'V'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
###########################################	
#Scissors Win Conditions
###########################################	
	elif (p1RPS == 'S' and p2RPS == 'R'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
		
	elif (p1RPS =='S' and p2RPS == 'S'):
		print ("draw" ) 
		draw = draw + 1 
		
	elif (p1RPS =='S' and p2RPS == 'P'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
        
	elif (p1RPS =='S' and p2RPS == 'L'):
		print ("Player 1 victory") #
		player1Wins = player1Wins + 1 
        
	elif (p1RPS =='S' and p2RPS == 'V'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
###########################################	
#Lizard Win Conditions
###########################################	
	elif (p1RPS == 'L' and p2RPS == 'R'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
        
	elif (p1RPS == 'L' and p2RPS == 'S'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
        
	elif (p1RPS == 'L' and p2RPS == 'P'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
        
	elif (p1RPS == 'L' and p2RPS == 'L'):
		print ("draw") 
		draw = draw + 1 
        
	elif (p1RPS == 'L' and p2RPS == 'V'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
###########################################	
#Spock Win Conditions
###########################################	 
	elif (p1RPS == 'V' and p2RPS == 'R'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1     
        
	elif (p1RPS == 'V' and p2RPS == 'S'):
		print ("Player 1 victory") 
		player1Wins = player1Wins + 1 
        
	elif (p1RPS == 'V' and p2RPS == 'P'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1  
        
	elif (p1RPS == 'V' and p2RPS == 'L'):
		print ("Player 2 victory") 
		player2Wins = player2Wins + 1 
        
	elif (p1RPS == 'V' and p2RPS == 'V'):
		print ("draw") 
		draw = draw + 1 
###########################################	
#Takes the wins_lose of the round and returns it to win_loss
###########################################	      
        win_Loss = [player1Wins, player2Wins, draw] 
	return win_Loss 
	
###########################################	
#Command line arg
###########################################	
if (len(sys.argv) != 3):
	print ("Usage: ", sys.argv[0], "Port Number, Rounds") 
	sys.exit() 
###########################################
#Inputs needed to establish port and rounds	
###########################################		
port = sys.argv[1] 
rounds = sys.argv[2] 
port = int(port) 
rounds = int(rounds) 
win_Loss = [0, 0, 0] 
players = [] 

###########################################	
#open and usable port numbers
###########################################	
if (port <1024 and port > 49151): 
	print ("Port Not Within limits of 1024-49151") 

player_S_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
player_S_socket.bind((socket.gethostname(), port))
print ('The hostname is: '+ socket.gethostname()+ ' running on port: '+ str(port)) 

while True: 
	player_S_socket.listen(2) 
	player = player_S_socket.accept() 
	
	players.append(player) 
	print ("Player 1 Established") 

	p1 = players[0][0].recv(1024)                                                                                
	p1 = p1.decode() 
	print("p1")
	holdmsg = "Please hold For P2" 
	players[0][0].send(holdmsg.encode())                                                                                
	
	player2 = player_S_socket.accept() 
	players.append(player2) 
	
	print ("Player 2 Established") 
	
	p2 = players[1][0].recv(1024)                                                                                   
	p2 = p2.decode() 
	
	print ("p2")
	
	passing = initiation(p1, p2) 
###########################################	
#Both Confimations not received
###########################################	
	if (passing == False): 
		print ("Error...Goodbye") 
		sys.exit() 
	
	pendingmsg = "Enjoy the Game" 
	players[0][0].send(pendingmsg.encode())                                                                                
	players[1][0].send(pendingmsg.encode())                                                                     
	
	
	
	for i in range (rounds): 
		play(players) 
		win_Loss = decisions(players, win_Loss) 
	tally(players, win_Loss) 
