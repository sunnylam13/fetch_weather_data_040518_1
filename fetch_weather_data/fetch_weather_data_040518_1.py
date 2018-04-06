# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 fetch_weather_data_040518_1.py CITYNAME

import json,requests,sys

import pprint # optional import, only to see data to configure correct object, list key calls

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# COMMAND LINE PROCESSING
#####################################

# get location from command line arguments

if len(sys.argv) < 2:  # error check that location provided
	print('Usage: fetch_weather_data_040518_1 location')
	sys.exit()

location = ' '.join(sys.argv[1:])
logging.debug("Location extracted from command line is:  %s" % (location) )

#####################################
# END COMMAND LINE PROCESSING
#####################################


#####################################
# GET DATA
#####################################

# download JSON data from API

api_key = "94152b1259ca814187842e32fea8151d"
logging.debug("API key is:  %s" % (api_key) )

api_addition = "&APPID=" + api_key
logging.debug("API addition to URL is:  %s" % (api_addition) )

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s%s' % (location,api_addition)
logging.debug("URL to use is:  %s" % (url) )

response = requests.get(url) # returns a response object
logging.debug("Response object is:  ")
logging.debug(response)
logging.debug("Response status is:  ")
logging.debug(response.raise_for_status()) # check status

# logging.debug("Show response text:  ")
# logging.debug(response.text) # shows the actual JSON data downloaded

#####################################
# END GET DATA
#####################################


#####################################
# DATA PROCESSING
#####################################

# load JSON data into a Python variable

weatherData = json.loads(response.text)

# optional - display to screen in an easy to read way
# requires `import pprint`
# pprint.pprint(weatherData)

# print weather descriptions

w = weatherData['list']

#####################################
# END DATA PROCESSING
#####################################

