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
#Prints out players options
###########################################	
def options(player_C_socket):
        valid = ['R','P','S','L','V']#list of valid inputs
        option = raw_input("Please make your selection:\nR - Rock\nP - Paper\nS - Scissors\nL - Lizard\nV - Spock\n\nInput:").upper()
###########################################	
#loops til valid input given
###########################################	
        if (option in valid):
            print ("")
            player_C_socket.send(option.encode())
            print(player_C_socket.recv)
        else:
            print('Sorry But You Didnt Choose an available option... Try Again')
            options(player_C_socket)

###########################################	
#Displays the players Victory, defeats, and draws
###########################################	
def finalTotal (victory, defeat, draws, player_C_socket):

	print ('victory: '+ victory) 
	print ('defeat: '+ defeat) 
	print ('draw: '+ draws) 
	
	halt = player_C_socket.recv(1024)
	
	if (halt == "HALT"):#Halt="STOP"
		print ("Thanks For Playing Rock, Paper, Scissors, Lizard, Spock")
		player_C_socket.close 
		sys.exit()
		os.kill()
###########################################
#Depending on the player takes their totals for each	
###########################################	        
def accumTotal(player_C_socket):

	victory = player_C_socket.recv(1) 
	defeat = player_C_socket.recv(1) 
	draws = player_C_socket.recv(1) 
	finalTotal(victory, defeat, draws, player_C_socket)         
###########################################	
#argument for client side
###########################################	
if (len(sys.argv) != 3): 
	print ("Usage: ", sys.argv[0], "Host Name, Port Number\n") 
	sys.exit() 	
###########################################	
#information needed for client side connection
###########################################		
hostname = sys.argv[1] 
port = sys.argv[2] 
print ("Port: "+ port)
port = int(port)
hostip = socket.gethostbyname(hostname)
###########################################	
###########################################	
try:
	player_C_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	player_C_socket.connect((hostname, port)) 
###########################################	
###########################################	
except OSError as err: 
	print(err.errno, err.strerror)
	sys.exit()
###########################################	
###########################################	
print ("You Have Successfully Connected")
msg = "PREPPED"#PREPPED="READY"
player_C_socket.send(msg.encode()) 
print(player_C_socket.recv)
hold = player_C_socket.recv(1024) 
print(player_C_socket.recv)
hold = hold.decode()
###########################################	
###########################################	
if (hold == "Please hold For P2"):
    print (hold)
    hold2 = player_C_socket.recv(14)
    
    hold2 = hold2.decode()
    print (hold2)
###########################################	
###########################################	
elif (hold == "Enjoy the Game"): 
	print (hold) 
###########################################	
###########################################	
while True:
    pending = player_C_socket.recv(7)
    print(player_C_socket.recv)
    pending = pending.decode()
    if (pending == "OK"):#OK="GO"
        pending = ""
        options(player_C_socket)
        print ("Waiting on Other Player...")
        print (pending)
    elif (pending == "TALLY"): #TALLY="SCORE"
        accumTotal(player_C_socket) 
    else :
        pending = ""
        print (pending)
        print("pending isn't right")
        sys.exit()