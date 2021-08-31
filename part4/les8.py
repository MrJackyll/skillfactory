#работа с файлами
with open('text.txt', 'w', encoding='utf-8') as myfile:
	myfile.write("Hi!")
with open ('text.txt', 'a', encoding='utf-8') as myfile:
	myfile.write("\nI am Alex\nYou're good =)\n\tHello world\n")
with open ('text.txt', 'r', encoding='utf-8') as myfile:
	#context = myfile.read()
	#print (context)
	for line in myfile:
		line = line.upper()
		line = line.replace ('\n', '') #заменить \n на пустоту
		print(line) 