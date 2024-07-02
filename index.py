# app.py

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    
    # Get client's IP address
    client_ip = request.remote_addr
    
    # Get location information using ipinfo.io
    location_response = requests.get(f"https://ipinfo.io/{client_ip}/json")
    location_data = location_response.json()
    city = location_data.get('city', 'Unknown')
    
    # Get temperature using OpenWeatherMap API
    weather_api_key = '355012dae7a7985b0f1083912ac6ee2f'
    weather_response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric")
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']
    
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
