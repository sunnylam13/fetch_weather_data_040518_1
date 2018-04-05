try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program makes checking weather easier by skipping the step of opening your web browser.  It downloads the weather forecast for the next few days and prints it as plain text.',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/fetch_weather_data_040518_1',
	'download_url': 'https://github.com/sunnylam13/fetch_weather_data_040518_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['json,requests,sys'],
	'scripts': [],
	'name': 'Fetch Current Weather Data'
}

setup(**config)