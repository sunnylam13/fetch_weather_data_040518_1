# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 fetch_weather_data_040518_1.py

import json,requests,sys

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

url = 'http://api.openweathermap.org/data/2.5/forecast?q=%s' % (location)
logging.debug("URL to use is:  %s" % (url) )

response = requests.get(url) # returns a response object
logging.debug("Response status is:  ")
logging.debug(response.raise_for_status()) # check status

#####################################
# END GET DATA
#####################################


#####################################
# DATA PROCESSING
#####################################

# load JSON data into a Python variable

#####################################
# END DATA PROCESSING
#####################################

