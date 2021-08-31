#работа с CSV - Comma Separeted Values (табличные данные)
import csv
with open ('data_us.csv', 'r', encoding='utf-8') as f:
	fields = ['number', 'time', 'course']
	reader = csv.DictReader(f, fieldnames=fields, delimiter=';')
	for row in reader:
		print(row)
