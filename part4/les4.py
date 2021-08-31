#исключения
#parts = int (input('Введите на сколько кусков нужно порезать пирог: '))
def cut_cake(parts):
	try:
		return 1/int(parts)
	except (ZeroDivisionError, ValueError, TypeError, NameError):
		return ('No no no, you write smth wrong')

cake = cut_cake('f')

#print ("Вот ваш " +str(cake) + " кусочек пирога")
print (cake)