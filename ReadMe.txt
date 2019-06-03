#Name:Andrew Steele
#Major:CSIT
#Class:328_Network Programming
#StartDate:11/9/17
#DueDate: 11/30/17
#Instuctor:Dr. Frye

Purpose of Project: The server accepts 2 players to play a game of Big Bang style rock, paper, scissors, lizards, and spock. The players will continually 
play through the rounds til the final tally is displayed. Each time being prompted to select either R,P,S,L,or V, each of which represents a different value
in the game. The remindal of the game is to win as many matches as possible by selecting the proper attribute that negates/defeats the opposing value.

Compile and run:
    1. First you must set up the server. To get the server running the user must identify what version of python they wish to use. I used python2.7 for the program.
    2. To run the sever you must enter the command line arguments as "python2.7 <filename> <port> <rounds>" filename as the name of the serverfile you want to run,port being
    the port you wish to run on as long as it's within the accepted range, and finally the number of rounds you wish to have the players play.
    3. Once the server is set up all that's required are 2 players which to run will again require the version of python used <filename> of the client file along within
    the <hostname> and <port> in that order. (ex. "python2.7 RPSclient.py csitd 1337")
    4. Once two players enter both should see a UI that looks similar too.
            Please make your selection:
            R - Rock
            P - Paper 
            S - Scissors
            L - Lizard
            V - Spock
      The user will then input one of the values given and wait til the 2nd player also submits an answer.

Issues/Bugs:
        >Sometimes after starting a new game with 2 new players not both players get the initial game prompt.

Tasks	Estimated time	Actual Time
Design	50 Min-1Hr	    20 Minutes
Code	2 Hrs	        20+Hours
Test	30Min-1Hr	    15Hours
Debugging	1Hr-2Hrs	10+Hours

