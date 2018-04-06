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


