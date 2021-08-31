#условные операторы
age = int (input ("Enter yr age: "))
print ("yr age " + str(age))
if age > 18 and age < 80:
	print ("You can drink")
elif age >= 80:
	print ("Do you really need this?")
else:
	print ("dont even think about it!")