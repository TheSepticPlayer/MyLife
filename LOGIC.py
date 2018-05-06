import sys
import subprocess
import random 

print ("Welcome To LOGIC")

def givemeafact(n):
	if n == 1:
		return ("The Pythonidae, commonly known simply as pythons, are a family of nonvenomous snakes.")
	elif n == 2:
		return ("Pythons are found in Africa, Asia, and Australia.")
	elif n == 3:
		return ("There is actually a poem written by Tim Peters named as THE ZEN OF PYTHON which can be read by just writing import this in the interpreter.")
	elif n == 4:
		return ("In the UK, it is illegal to eat mince pies on Christmas Day!")
	elif n == 5:
		return ("When hippos are upset, their sweat turns red.")
	elif n == 6:
		return ("A flock of crows is known as a murder.")
while 7 == 7:
	commandline = input("type \"quit\" to quit program, type \"help\" to get help \: ")
	
	if commandline == "quit":
		sys.exit("Command Executed!")

	elif commandline == "help":
		print ("quit divide multiply givemeafact")

	elif commandline == "divide":
		d = input("")
		print (int(d[0])/int(d[2]))

	elif commandline == "multiply":
		d = input("")
		print (int(d[0])*int(d[2]))

	elif commandline == "givemeafact":
		print (givemeafact(random.randint(1,6)))

