from flask import Flask, render_template, request, jsonify
import json
#import requests
from urllib.request import urlopen

app = Flask(__name__)

@app.route('/')
def index():  
    address = request.environ['REMOTE_ADDR']
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        print (address)
    else:
        address = request.environ['HTTP_X_FORWARDED_FOR']
        print (request.environ['HTTP_X_FORWARDED_FOR'])
    url = f'http://ipinfo.io/{address}?token=8684e95f280e95'
    response = urlopen(url)
    data = json.load(response)
    ip = data['ip']
    city = data['city']
    api_key = "e4a20d5f0fdbc130656637e5ff74aa77"
    url3 = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response3 = urlopen(url3)
    data3 = json.load(response3)
    print(data3['main']['temp'])
    print()
    temp = data3['main']['temp'] - 273.15
    format_temp = f"{temp:.2f}"
    name = request.args.get('name', 'mark')
    return render_template('index.html', ip=address, city=city, temp=format_temp, name=name)