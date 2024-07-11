from flask import Flask, request
import json
#import requests
from urllib.request import urlopen

app = Flask(__name__)


@app.route('/api/hello')
def index():
    address = request.environ['REMOTE_ADDR']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        address = address
    else:
        address = request.environ['HTTP_X_FORWARDED_FOR']
    url = f'http://ipinfo.io/{address}?token=8684e95f280e95'
    response = urlopen(url)
    data = json.load(response)
    city = data['city']
    api_key = "e4a20d5f0fdbc130656637e5ff74aa77"
    url3 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response3 = urlopen(url3)
    data3 = json.load(response3)
    temp = data3['main']['temp'] - 273.15
    format_temp = f"{temp:.2f}"
    name = request.args.get('visitor_name', 'mark')
    API_RESULT = {"client_ip": address, "location": city, "greeting": f"Hello, {name}!, the temperature is {format_temp} degrees celcius in {city}"}
    return API_RESULT
