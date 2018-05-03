import random


t = 0
w = ""
m = ""
s = ""

def randomsymbolgen():
	return chr(random.randint(33, 64))

def randomlettergen():
	return chr(random.randint(65,122))
	

#Weak Password Gen
def letterandnumbergen():
 n = random.randint(1, 2)

 if n == 0:
	w = str(random.randint(0, 9,)) + randomlettergen()
 	return w
 else:
 	w = str(random.randint(0, 9,)) + randomlettergen()
 	return w

def weakpasswordgen():
	return str(letterandnumbergen()) + str(letterandnumbergen()) 

def symbolletternumber():
	return str(letterandnumbergen()) + str(randomsymbolgen())

def mediumpasswordgen():
	return str(symbolletternumber()) + str(letterandnumbergen())

def strongpasswordgen():
	return str(mediumpasswordgen()) + str(weakpasswordgen())





uin = input("How storng do you want your password to be?  (1 = weak 2 = medium 3 = strong)")

if uin == 1:
	print weakpasswordgen()
elif uin == 2:
	print mediumpasswordgen()
elif uin == 3:
	print strongpasswordgen()
else:
	print "Please type something from 1-3"





