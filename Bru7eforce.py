import hashlib
import itertools



match = "AC34BFB5683".lower() #This was the first 11 digits the user wanted to find the SHA256 for.

numbers = '0123456789'

print("LETS GOOO")
print("")
print("|--------------------------------------------------------------------|")
count = 0
for c in itertools.product(numbers, repeat=7):
	m = hashlib.sha256()
	number = ""
	for x in c:
		number+= str(x)
	m.update(str(number).encode('utf'))
	pin = m.hexdigest()
	print("| Try " + str(count) + " | " + number +" | " + str(pin)+"|")
	if str(pin[0:11]) == match:
		print("FOUND: " + str(c))
		break
	else:
		count = count + 1
	