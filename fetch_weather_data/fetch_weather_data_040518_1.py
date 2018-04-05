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

#####################################
# END COMMAND LINE PROCESSING
#####################################

#####################################
# DATA PROCESSING
#####################################

# download JSON data from API


# load JSON data into a Python variable

#####################################
# END DATA PROCESSING
#####################################

