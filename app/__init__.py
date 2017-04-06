__author__ = 'alee'
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


from app import views

import urllib.request as getstuff
import json
f = getstuff.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
latitude = location['latitude']
longitude = location['longitude']