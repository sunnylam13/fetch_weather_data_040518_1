# Scratch Notes and Log

## Thursday, April 5, 2018 9:50 AM

program uses `requests`

program aims...

* read requested location from command line

* download JSON weather data from [OpenWeatherMap.org](http://openweathermap.org/)

* convert string of JSON data to a Python data structure

* print weather for today and next 2 days

code should do...

* join strings in `sys.argv` to get location

* call `requests.get()` to download weather data

* call `json.loads()` to convert JSON data to Python data

* print weather forecast

## Thursday, April 5, 2018 10:01 AM

	if len(sys.argv) < 2:  # error check that location provided
		print('Usage: fetch_weather_data_040518_1 location')
		sys.exit()

	location = ' '.join(sys.argv[1:])

where `sys.argv[0]` is the script filename

the command line arguments are split on spaces

--------------------------------

EXAMPLE:  meaning argument `San Francisco, CA` would make `sys.argv` hold...

	['programName','San','Francisco','CA']

--------------------------------

you use `join()` to join all the strings except the firt

	location = ' '.join(sys.argv[1:])

so you kill off the spaces you don't need

## Thursday, April 5, 2018 10:03 AM

[OpenWeatherMap.org](http://openweathermap.org/)

to get weather for next 2 days

use 5 day, 3 hour

use [Call 5 day / 3 hour forecast data](http://openweathermap.org/forecast5)

	By city name
	Description:
	You can search weather forecast for 5 days with data every 3 hours by city name. All weather data can be obtained in JSON and XML formats.
	There is a possibility to receive a central district of the city/town with its own parameters (geographic coordinates/id/name) in API response. Example

	API call:
	api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
	Parameters:
	q city name and country code divided by comma, use ISO 3166 country codes

	Examples of API calls:
	api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml

use

	api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

use [16 day weather forecast](http://openweathermap.org/forecast16)

> 16 day forecasts is available at any location or city. Forecasts include daily weather and available in JSON or XML format. It is only available for all paid accounts.

	By city name
	Description:
	You can search 16 day weather forecast with daily average parameters by city name. All weather data can be obtained in JSON and XML formats.
	There is a possibility to receive a central district of the city/town with its own parameters (geographic coordinates/id/name) in API response. Example

	API call:
	api.openweathermap.org/data/2.5/forecast/daily?q={city name},{country code}&cnt={cnt}
	Parameters:
	q city name and country code divided by comma, use ISO 3166 country codes

	cnt number of days returned (from 1 to 16)

	Examples of API calls:
	Call 7 days forecast by city name in XML format and metric units api.openweathermap.org/data/2.5/forecast/daily?q=London&mode=xml&units=metric&cnt=7

use

	api.openweathermap.org/data/2.5/forecast/daily?q={city name},{country code}&cnt={cnt}

it's unfortunate that daily is only available for paid accounts

meaning I have to change the target URL

	api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

drop `{country code}`

	api.openweathermap.org/data/2.5/forecast?q={city name}

## Friday, April 6, 2018 10:15 AM

Forgot that you have to sign up for the Free plan first in order to use the API call...

Info on using your API key...

	http://openweathermap.org/appid

created a separate key for fetch weather program

max 60 calls an hour

### How to use API key in API call

Description:
To get access to weather API you need an API key whatever account you chose from Free to Enterprise.

Activation of an API key for Free and Startup plans takes 10 minutes. For other tariff plans it is 10 to 60 minutes.

We keep right to not to process API requests without API key.

### API call:

	http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}

Parameters:

APPID {APIKEY} is your unique API key 

Example of API call:

api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111 

## Friday, April 6, 2018 4:09 PM

	python3 fetch_weather_data_040518_1.py Toronto

works

using

	python3 fetch_weather_data_040518_1.py "Toronto, ON"

	python3 fetch_weather_data_040518_1.py "Toronto,ON"

does not

## Friday, April 6, 2018 4:15 PM

	# logging.debug("Show response text:  ")
	# logging.debug(response.text) # shows the actual JSON data downloaded

if you want to see this data another way

pass it to `pprint.pprint()`

weather descriptions we want are after `main` and `description`

## Friday, April 6, 2018 4:19 PM

Example data downloaded for Toronto...

must analyze data to determine what is

* current weather

* tomorrow weather

* day after weather

----------------

	{'city': {'coord': {'lat': 43.654, 'lon': -79.3873},
	          'country': 'CA',
	          'id': 6167865,
	          'name': 'Toronto',
	          'population': 4612191},
	 'cnt': 40,
	 'cod': '200',
	 'list': [{'clouds': {'all': 64},
	           'dt': 1523048400,
	           'dt_txt': '2018-04-06 21:00:00',
	           'main': {'grnd_level': 995.28,
	                    'humidity': 73,
	                    'pressure': 995.28,
	                    'sea_level': 1014.61,
	                    'temp': 277.21,
	                    'temp_kf': -0.21,
	                    'temp_max': 277.418,
	                    'temp_min': 277.21},
	           'rain': {'3h': 0.12},
	           'snow': {'3h': 0.002},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'light rain',
	                        'icon': '10d',
	                        'id': 500,
	                        'main': 'Rain'}],
	           'wind': {'deg': 256, 'speed': 9.18}},
	          {'clouds': {'all': 48},
	           'dt': 1523059200,
	           'dt_txt': '2018-04-07 00:00:00',
	           'main': {'grnd_level': 997.86,
	                    'humidity': 75,
	                    'pressure': 997.86,
	                    'sea_level': 1017.35,
	                    'temp': 273.98,
	                    'temp_kf': -0.16,
	                    'temp_max': 274.136,
	                    'temp_min': 273.98},
	           'rain': {'3h': 0.0425},
	           'snow': {'3h': 0.073},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light rain',
	                        'icon': '10n',
	                        'id': 500,
	                        'main': 'Rain'}],
	           'wind': {'deg': 258.004, 'speed': 9.48}},
	          {'clouds': {'all': 20},
	           'dt': 1523070000,
	           'dt_txt': '2018-04-07 03:00:00',
	           'main': {'grnd_level': 1001.71,
	                    'humidity': 73,
	                    'pressure': 1001.71,
	                    'sea_level': 1021.32,
	                    'temp': 271.51,
	                    'temp_kf': -0.1,
	                    'temp_max': 271.617,
	                    'temp_min': 271.51},
	           'rain': {},
	           'snow': {'3h': 0.153},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13n',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 286.003, 'speed': 9.53}},
	          {'clouds': {'all': 0},
	           'dt': 1523080800,
	           'dt_txt': '2018-04-07 06:00:00',
	           'main': {'grnd_level': 1004.19,
	                    'humidity': 74,
	                    'pressure': 1004.19,
	                    'sea_level': 1024,
	                    'temp': 269.84,
	                    'temp_kf': -0.05,
	                    'temp_max': 269.895,
	                    'temp_min': 269.84},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 289.003, 'speed': 9.76}},
	          {'clouds': {'all': 0},
	           'dt': 1523091600,
	           'dt_txt': '2018-04-07 09:00:00',
	           'main': {'grnd_level': 1006.59,
	                    'humidity': 75,
	                    'pressure': 1006.59,
	                    'sea_level': 1026.59,
	                    'temp': 269.042,
	                    'temp_kf': 0,
	                    'temp_max': 269.042,
	                    'temp_min': 269.042},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 301.503, 'speed': 8}},
	          {'clouds': {'all': 0},
	           'dt': 1523102400,
	           'dt_txt': '2018-04-07 12:00:00',
	           'main': {'grnd_level': 1008.77,
	                    'humidity': 77,
	                    'pressure': 1008.77,
	                    'sea_level': 1028.73,
	                    'temp': 268.664,
	                    'temp_kf': 0,
	                    'temp_max': 268.664,
	                    'temp_min': 268.664},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 301.501, 'speed': 6.63}},
	          {'clouds': {'all': 12},
	           'dt': 1523113200,
	           'dt_txt': '2018-04-07 15:00:00',
	           'main': {'grnd_level': 1009.86,
	                    'humidity': 73,
	                    'pressure': 1009.86,
	                    'sea_level': 1029.76,
	                    'temp': 271.733,
	                    'temp_kf': 0,
	                    'temp_max': 271.733,
	                    'temp_min': 271.733},
	           'rain': {},
	           'snow': {'3h': 0.0047499999999998},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 302.501, 'speed': 5.84}},
	          {'clouds': {'all': 56},
	           'dt': 1523124000,
	           'dt_txt': '2018-04-07 18:00:00',
	           'main': {'grnd_level': 1008.92,
	                    'humidity': 71,
	                    'pressure': 1008.92,
	                    'sea_level': 1028.72,
	                    'temp': 273.267,
	                    'temp_kf': 0,
	                    'temp_max': 273.267,
	                    'temp_min': 273.267},
	           'rain': {},
	           'snow': {'3h': 0.0062500000000001},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 285.001, 'speed': 3.76}},
	          {'clouds': {'all': 80},
	           'dt': 1523134800,
	           'dt_txt': '2018-04-07 21:00:00',
	           'main': {'grnd_level': 1007.77,
	                    'humidity': 66,
	                    'pressure': 1007.77,
	                    'sea_level': 1027.61,
	                    'temp': 273.794,
	                    'temp_kf': 0,
	                    'temp_max': 273.794,
	                    'temp_min': 273.794},
	           'rain': {},
	           'snow': {'3h': 0.0050000000000001},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 275.503, 'speed': 3.4}},
	          {'clouds': {'all': 80},
	           'dt': 1523145600,
	           'dt_txt': '2018-04-08 00:00:00',
	           'main': {'grnd_level': 1008.35,
	                    'humidity': 66,
	                    'pressure': 1008.35,
	                    'sea_level': 1028.18,
	                    'temp': 272.532,
	                    'temp_kf': 0,
	                    'temp_max': 272.532,
	                    'temp_min': 272.532},
	           'rain': {},
	           'snow': {'3h': 0.0275},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 307.006, 'speed': 3.47}},
	          {'clouds': {'all': 68},
	           'dt': 1523156400,
	           'dt_txt': '2018-04-08 03:00:00',
	           'main': {'grnd_level': 1009.07,
	                    'humidity': 73,
	                    'pressure': 1009.07,
	                    'sea_level': 1028.98,
	                    'temp': 270.653,
	                    'temp_kf': 0,
	                    'temp_max': 270.653,
	                    'temp_min': 270.653},
	           'rain': {},
	           'snow': {'3h': 0.025},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 309.001, 'speed': 2.68}},
	          {'clouds': {'all': 0},
	           'dt': 1523167200,
	           'dt_txt': '2018-04-08 06:00:00',
	           'main': {'grnd_level': 1008.21,
	                    'humidity': 80,
	                    'pressure': 1008.21,
	                    'sea_level': 1028.07,
	                    'temp': 267.526,
	                    'temp_kf': 0,
	                    'temp_max': 267.526,
	                    'temp_min': 267.526},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 286.502, 'speed': 2.26}},
	          {'clouds': {'all': 0},
	           'dt': 1523178000,
	           'dt_txt': '2018-04-08 09:00:00',
	           'main': {'grnd_level': 1007.94,
	                    'humidity': 82,
	                    'pressure': 1007.94,
	                    'sea_level': 1027.9,
	                    'temp': 265.844,
	                    'temp_kf': 0,
	                    'temp_max': 265.844,
	                    'temp_min': 265.844},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 280.505, 'speed': 3.22}},
	          {'clouds': {'all': 20},
	           'dt': 1523188800,
	           'dt_txt': '2018-04-08 12:00:00',
	           'main': {'grnd_level': 1009.12,
	                    'humidity': 88,
	                    'pressure': 1009.12,
	                    'sea_level': 1029.13,
	                    'temp': 267.533,
	                    'temp_kf': 0,
	                    'temp_max': 267.533,
	                    'temp_min': 267.533},
	           'rain': {},
	           'snow': {'3h': 0.02},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 313.501, 'speed': 4.06}},
	          {'clouds': {'all': 32},
	           'dt': 1523199600,
	           'dt_txt': '2018-04-08 15:00:00',
	           'main': {'grnd_level': 1010.54,
	                    'humidity': 76,
	                    'pressure': 1010.54,
	                    'sea_level': 1030.32,
	                    'temp': 272.329,
	                    'temp_kf': 0,
	                    'temp_max': 272.329,
	                    'temp_min': 272.329},
	           'rain': {},
	           'snow': {'3h': 0.0075000000000003},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 314.501, 'speed': 4}},
	          {'clouds': {'all': 68},
	           'dt': 1523210400,
	           'dt_txt': '2018-04-08 18:00:00',
	           'main': {'grnd_level': 1010.32,
	                    'humidity': 68,
	                    'pressure': 1010.32,
	                    'sea_level': 1030.22,
	                    'temp': 273.255,
	                    'temp_kf': 0,
	                    'temp_max': 273.255,
	                    'temp_min': 273.255},
	           'rain': {},
	           'snow': {'3h': 0.0375},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13d',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 305.001, 'speed': 5.47}},
	          {'clouds': {'all': 24},
	           'dt': 1523221200,
	           'dt_txt': '2018-04-08 21:00:00',
	           'main': {'grnd_level': 1011.66,
	                    'humidity': 67,
	                    'pressure': 1011.66,
	                    'sea_level': 1031.37,
	                    'temp': 273.618,
	                    'temp_kf': 0,
	                    'temp_max': 273.618,
	                    'temp_min': 273.618},
	           'rain': {},
	           'snow': {'3h': 0.0025000000000004},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 317.503, 'speed': 5.41}},
	          {'clouds': {'all': 0},
	           'dt': 1523232000,
	           'dt_txt': '2018-04-09 00:00:00',
	           'main': {'grnd_level': 1014.39,
	                    'humidity': 64,
	                    'pressure': 1014.39,
	                    'sea_level': 1034.17,
	                    'temp': 271.221,
	                    'temp_kf': 0,
	                    'temp_max': 271.221,
	                    'temp_min': 271.221},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 323.001, 'speed': 4.2}},
	          {'clouds': {'all': 32},
	           'dt': 1523242800,
	           'dt_txt': '2018-04-09 03:00:00',
	           'main': {'grnd_level': 1015.71,
	                    'humidity': 76,
	                    'pressure': 1015.71,
	                    'sea_level': 1035.73,
	                    'temp': 268.267,
	                    'temp_kf': 0,
	                    'temp_max': 268.267,
	                    'temp_min': 268.267},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'scattered clouds',
	                        'icon': '03n',
	                        'id': 802,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 338.003, 'speed': 4.31}},
	          {'clouds': {'all': 48},
	           'dt': 1523253600,
	           'dt_txt': '2018-04-09 06:00:00',
	           'main': {'grnd_level': 1016.53,
	                    'humidity': 80,
	                    'pressure': 1016.53,
	                    'sea_level': 1036.71,
	                    'temp': 267.083,
	                    'temp_kf': 0,
	                    'temp_max': 267.083,
	                    'temp_min': 267.083},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'scattered clouds',
	                        'icon': '03n',
	                        'id': 802,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 349.501, 'speed': 2.96}},
	          {'clouds': {'all': 64},
	           'dt': 1523264400,
	           'dt_txt': '2018-04-09 09:00:00',
	           'main': {'grnd_level': 1017.25,
	                    'humidity': 84,
	                    'pressure': 1017.25,
	                    'sea_level': 1037.42,
	                    'temp': 266.984,
	                    'temp_kf': 0,
	                    'temp_max': 266.984,
	                    'temp_min': 266.984},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'broken clouds',
	                        'icon': '04n',
	                        'id': 803,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 15.0006, 'speed': 2.52}},
	          {'clouds': {'all': 88},
	           'dt': 1523275200,
	           'dt_txt': '2018-04-09 12:00:00',
	           'main': {'grnd_level': 1018.2,
	                    'humidity': 75,
	                    'pressure': 1018.2,
	                    'sea_level': 1038.26,
	                    'temp': 269.185,
	                    'temp_kf': 0,
	                    'temp_max': 269.185,
	                    'temp_min': 269.185},
	           'rain': {'3h': 0.005},
	           'snow': {'3h': 0.0024999999999999},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'light rain',
	                        'icon': '10d',
	                        'id': 500,
	                        'main': 'Rain'}],
	           'wind': {'deg': 79.0004, 'speed': 3.06}},
	          {'clouds': {'all': 68},
	           'dt': 1523286000,
	           'dt_txt': '2018-04-09 15:00:00',
	           'main': {'grnd_level': 1017.53,
	                    'humidity': 75,
	                    'pressure': 1017.53,
	                    'sea_level': 1037.43,
	                    'temp': 272.995,
	                    'temp_kf': 0,
	                    'temp_max': 272.995,
	                    'temp_min': 272.995},
	           'rain': {},
	           'snow': {'3h': 0.0049999999999999},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 105.001, 'speed': 4.36}},
	          {'clouds': {'all': 68},
	           'dt': 1523296800,
	           'dt_txt': '2018-04-09 18:00:00',
	           'main': {'grnd_level': 1016.32,
	                    'humidity': 71,
	                    'pressure': 1016.32,
	                    'sea_level': 1036.05,
	                    'temp': 274.315,
	                    'temp_kf': 0,
	                    'temp_max': 274.315,
	                    'temp_min': 274.315},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'broken clouds',
	                        'icon': '04d',
	                        'id': 803,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 115.001, 'speed': 5.56}},
	          {'clouds': {'all': 76},
	           'dt': 1523307600,
	           'dt_txt': '2018-04-09 21:00:00',
	           'main': {'grnd_level': 1014.22,
	                    'humidity': 69,
	                    'pressure': 1014.22,
	                    'sea_level': 1033.83,
	                    'temp': 274.129,
	                    'temp_kf': 0,
	                    'temp_max': 274.129,
	                    'temp_min': 274.129},
	           'rain': {},
	           'snow': {'3h': 0.0024999999999999},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 99.5004, 'speed': 5.87}},
	          {'clouds': {'all': 92},
	           'dt': 1523318400,
	           'dt_txt': '2018-04-10 00:00:00',
	           'main': {'grnd_level': 1013.48,
	                    'humidity': 73,
	                    'pressure': 1013.48,
	                    'sea_level': 1033.05,
	                    'temp': 272.867,
	                    'temp_kf': 0,
	                    'temp_max': 272.867,
	                    'temp_min': 272.867},
	           'rain': {},
	           'snow': {'3h': 0.165},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13n',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 88.0018, 'speed': 5.91}},
	          {'clouds': {'all': 92},
	           'dt': 1523329200,
	           'dt_txt': '2018-04-10 03:00:00',
	           'main': {'grnd_level': 1012.92,
	                    'humidity': 78,
	                    'pressure': 1012.92,
	                    'sea_level': 1032.7,
	                    'temp': 272.523,
	                    'temp_kf': 0,
	                    'temp_max': 272.523,
	                    'temp_min': 272.523},
	           'rain': {},
	           'snow': {'3h': 0.6025},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13n',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 81.5007, 'speed': 5.55}},
	          {'clouds': {'all': 88},
	           'dt': 1523340000,
	           'dt_txt': '2018-04-10 06:00:00',
	           'main': {'grnd_level': 1010.52,
	                    'humidity': 88,
	                    'pressure': 1010.52,
	                    'sea_level': 1030.38,
	                    'temp': 272.605,
	                    'temp_kf': 0,
	                    'temp_max': 272.605,
	                    'temp_min': 272.605},
	           'rain': {},
	           'snow': {'3h': 1.1},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13n',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 77.0034, 'speed': 4.71}},
	          {'clouds': {'all': 92},
	           'dt': 1523350800,
	           'dt_txt': '2018-04-10 09:00:00',
	           'main': {'grnd_level': 1008.83,
	                    'humidity': 91,
	                    'pressure': 1008.83,
	                    'sea_level': 1028.68,
	                    'temp': 272.505,
	                    'temp_kf': 0,
	                    'temp_max': 272.505,
	                    'temp_min': 272.505},
	           'rain': {},
	           'snow': {'3h': 1.0925},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13n',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 57.0005, 'speed': 3.45}},
	          {'clouds': {'all': 92},
	           'dt': 1523361600,
	           'dt_txt': '2018-04-10 12:00:00',
	           'main': {'grnd_level': 1008.81,
	                    'humidity': 89,
	                    'pressure': 1008.81,
	                    'sea_level': 1028.64,
	                    'temp': 272,
	                    'temp_kf': 0,
	                    'temp_max': 272,
	                    'temp_min': 272},
	           'rain': {},
	           'snow': {'3h': 0.595},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13d',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 7.00079, 'speed': 4.01}},
	          {'clouds': {'all': 88},
	           'dt': 1523372400,
	           'dt_txt': '2018-04-10 15:00:00',
	           'main': {'grnd_level': 1009.65,
	                    'humidity': 85,
	                    'pressure': 1009.65,
	                    'sea_level': 1029.29,
	                    'temp': 273.156,
	                    'temp_kf': 0,
	                    'temp_max': 273.156,
	                    'temp_min': 273.156},
	           'rain': {},
	           'snow': {'3h': 0.4225},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'light snow',
	                        'icon': '13d',
	                        'id': 600,
	                        'main': 'Snow'}],
	           'wind': {'deg': 341.504, 'speed': 5.91}},
	          {'clouds': {'all': 80},
	           'dt': 1523383200,
	           'dt_txt': '2018-04-10 18:00:00',
	           'main': {'grnd_level': 1009.55,
	                    'humidity': 76,
	                    'pressure': 1009.55,
	                    'sea_level': 1029.2,
	                    'temp': 275.439,
	                    'temp_kf': 0,
	                    'temp_max': 275.439,
	                    'temp_min': 275.439},
	           'rain': {},
	           'snow': {'3h': 0.0225},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 328, 'speed': 6.37}},
	          {'clouds': {'all': 24},
	           'dt': 1523394000,
	           'dt_txt': '2018-04-10 21:00:00',
	           'main': {'grnd_level': 1009.61,
	                    'humidity': 69,
	                    'pressure': 1009.61,
	                    'sea_level': 1029.06,
	                    'temp': 275.986,
	                    'temp_kf': 0,
	                    'temp_max': 275.986,
	                    'temp_min': 275.986},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'few clouds',
	                        'icon': '02d',
	                        'id': 801,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 320.501, 'speed': 6.86}},
	          {'clouds': {'all': 0},
	           'dt': 1523404800,
	           'dt_txt': '2018-04-11 00:00:00',
	           'main': {'grnd_level': 1011.09,
	                    'humidity': 72,
	                    'pressure': 1011.09,
	                    'sea_level': 1030.8,
	                    'temp': 273.546,
	                    'temp_kf': 0,
	                    'temp_max': 273.546,
	                    'temp_min': 273.546},
	           'rain': {},
	           'snow': {'3h': 0.0049999999999999},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 311.501, 'speed': 6.11}},
	          {'clouds': {'all': 0},
	           'dt': 1523415600,
	           'dt_txt': '2018-04-11 03:00:00',
	           'main': {'grnd_level': 1012.13,
	                    'humidity': 74,
	                    'pressure': 1012.13,
	                    'sea_level': 1031.95,
	                    'temp': 271.179,
	                    'temp_kf': 0,
	                    'temp_max': 271.179,
	                    'temp_min': 271.179},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 300.5, 'speed': 5.66}},
	          {'clouds': {'all': 0},
	           'dt': 1523426400,
	           'dt_txt': '2018-04-11 06:00:00',
	           'main': {'grnd_level': 1011.56,
	                    'humidity': 77,
	                    'pressure': 1011.56,
	                    'sea_level': 1031.47,
	                    'temp': 270.555,
	                    'temp_kf': 0,
	                    'temp_max': 270.555,
	                    'temp_min': 270.555},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 295.004, 'speed': 5.92}},
	          {'clouds': {'all': 0},
	           'dt': 1523437200,
	           'dt_txt': '2018-04-11 09:00:00',
	           'main': {'grnd_level': 1011.73,
	                    'humidity': 76,
	                    'pressure': 1011.73,
	                    'sea_level': 1031.68,
	                    'temp': 270.089,
	                    'temp_kf': 0,
	                    'temp_max': 270.089,
	                    'temp_min': 270.089},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'n'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01n',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 295.509, 'speed': 5.91}},
	          {'clouds': {'all': 0},
	           'dt': 1523448000,
	           'dt_txt': '2018-04-11 12:00:00',
	           'main': {'grnd_level': 1012.78,
	                    'humidity': 77,
	                    'pressure': 1012.78,
	                    'sea_level': 1032.76,
	                    'temp': 270.613,
	                    'temp_kf': 0,
	                    'temp_max': 270.613,
	                    'temp_min': 270.613},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 290.003, 'speed': 5.11}},
	          {'clouds': {'all': 0},
	           'dt': 1523458800,
	           'dt_txt': '2018-04-11 15:00:00',
	           'main': {'grnd_level': 1013.05,
	                    'humidity': 74,
	                    'pressure': 1013.05,
	                    'sea_level': 1032.82,
	                    'temp': 275.059,
	                    'temp_kf': 0,
	                    'temp_max': 275.059,
	                    'temp_min': 275.059},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'clear sky',
	                        'icon': '01d',
	                        'id': 800,
	                        'main': 'Clear'}],
	           'wind': {'deg': 272.502, 'speed': 4.16}},
	          {'clouds': {'all': 76},
	           'dt': 1523469600,
	           'dt_txt': '2018-04-11 18:00:00',
	           'main': {'grnd_level': 1010.64,
	                    'humidity': 66,
	                    'pressure': 1010.64,
	                    'sea_level': 1030.29,
	                    'temp': 276.602,
	                    'temp_kf': 0,
	                    'temp_max': 276.602,
	                    'temp_min': 276.602},
	           'rain': {},
	           'snow': {},
	           'sys': {'pod': 'd'},
	           'weather': [{'description': 'broken clouds',
	                        'icon': '04d',
	                        'id': 803,
	                        'main': 'Clouds'}],
	           'wind': {'deg': 237.503, 'speed': 5.36}}],
	 'message': 0.0043}

-------------------

## Friday, April 6, 2018 5:39 PM

Ideas for similar programs

* collect weather forecasts for several camp sites or hike trails to see which have the best weather

* schedule a program to regularly check weather and send you a frost alert if you need to move your plants indoors

* pull weather data from many sites to show all at once or calculate and show the average of the multiple weather predictions



