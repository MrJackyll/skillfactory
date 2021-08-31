from flask import Flask, request

from req import get_weather

from datetime import datetime

city_id = 524901
apikey = 'cf90636aa494e41b0365ce34aa48722a'

app = Flask(__name__)

@app.route('/news')
def all_the_news():
	#for item in request.args:
		#print (item)
		#print(request.args.get(item))
	colors = ['black', 'green', 'yellow', 'pink', 'red', 'purple', 'orange', 'blue']
	try:
		limit = int(request.args.get('limit'))
	except:
		limit = 10
	color = request.args.get('color') if request.args.get('color') in colors else 'black'

	#return 'News'
	return '<h1 style="color: %s">News: %s</h1>' %(color, limit)

@app.route('/')#привязуем к адрессу главную страницу
def index():
	url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&units=metric&appid=%s' % (city_id, apikey)
	weather = get_weather(url)
	cur_date = datetime.now().strftime('%d.%m.%Y %H:%M')

	result = '<p><b>Temp:</b> <i>%s</i><p>' % weather ['main']['temp'] #<p> html тег параграф
	result += '<p><b>City:</b> <i>%s</i><p>' % weather ['name']
	result += '<p><b>Date:</b> <i>%s</i><p>' % cur_date 

	return result

if __name__ == '__main__':
	app.run(debug=True) #port = 5010 - изменяет адресс порта