import random

q = 0
i = 0

zero = 0
one  = 0
two  = 0
three= 0
four = 0
five = 0
six  = 0
seven= 0
eight= 0 
nine = 0

while i != 100000:
	i += 1
	q = random.randint(0, 9)

	if q == 0:
		zero += 1

	elif q == 1:
		one += 1

	elif q == 2:
		two += 1

	elif q == 3:
		three += 1

	elif q == 4:
		four += 1
	
	elif q == 5:
		five += 1

	elif q == 6:
		six += 1

	elif q == 7:
		seven += 1

	elif q == 8:
		eight += 1

	elif q == 9:
		nine += 1

	i += 1


print zero
print one
print two
print three
print four
print five
print six
print seven
print eight
print nine