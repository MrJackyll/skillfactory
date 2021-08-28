#functions
def get_vat (payment, percent = 20): #def - define - определяет функцию
	try:
		payment = float (payment) 
		vat = payment / 100 * percent #расчёт НДС
		vat = round(vat, 2)
		return "Sum Vat : {}".format(vat)
	except TypeError: #исключить ошибку и вывести текст в случае её появления
		return "Не возможно посчитать. Проверьте правильность ввода данных"

#result = get_vat ("ololo")
#result = get_vat (4.888, 10) #- то процент будет 10 а не как указанно по умолчанию
result = get_vat (400)
print (result)