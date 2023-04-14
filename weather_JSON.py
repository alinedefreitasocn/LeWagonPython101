import os; os.system("pip install requests")
import requests
response = requests.get("https://weather.lewagon.com/data/2.5/forecast?lat=51.5073219&lon=-0.1276474&units=metric").json()
# Do not modify the code above


def weather_forecast(response):
    city = response.get('city').get('name')
    next_day = str(datetime.date.today() + datetime.timedelta(days=1)) + " 06:00:00"
    # outputs is a list of dictionaries
    outputs = response.get('list')
    forecast = 
    #for hour in outputs:
    #    if hour.get('dt_txt') == next_day:
    #        forecast = hour['weather'][0].get('description')
    
    return f'The weather in {city} tomorrow is {forecast}'
