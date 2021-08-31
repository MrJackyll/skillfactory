import csv
course_list = [
	{'number': '0', 'time': '2016-09-14 00:00:00', 'course': '101.838'},
	{'number': '1', 'time': '2016-09-14 01:00:00', 'course': '101.938'},
	{'number': '2', 'time': '2016-09-14 02:00:00', 'course': '101.868'},
	{'number': '3', 'time': '2016-09-14 03:00:00', 'course': '101.738'},
	{'number': '4', 'time': '2016-09-14 04:00:00', 'course': '101.638'},
	{'number': '5', 'time': '2016-09-14 05:00:00', 'course': '101.538'},
	{'number': '6', 'time': '2016-09-14 06:00:00', 'course': '101.358'},
	{'number': '7', 'time': '2016-09-14 07:00:00', 'course': '101.668'},
	{'number': '8', 'time': '2016-09-14 08:00:00', 'course': '101.758'},
	{'number': '9', 'time': '2016-09-14 09:00:00', 'course': '101.958'}
	]
with open ('example.csv', 'w', encoding='utf-8') as f:
	fields = ['number', 'time', 'course']
	writer = csv.DictWriter(f, fieldnames=fields, delimiter=';')
	writer.writeheader()
	for course in course_list:
		writer.writerow(course)