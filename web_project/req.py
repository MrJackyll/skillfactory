import requests

def get_weather(url):
	result = requests.get(url)
	#print(result.json()) #json преобразует строку в словарь, это нужно для того чтобы работать с элементами словаря
	#	print(result.json()['name']) #выводим name
	if result.status_code == 200:
		return result.json()
	else:
		print('smth wrong')


if __name__ == '__main__':
	data = get_weather ('http://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=cf90636aa494e41b0365ce34aa48722a')
	print(data)