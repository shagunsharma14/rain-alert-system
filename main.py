import requests
from twilio.rest import Client
import os
account_sid = "AC6eb177de327d1e373b4f65c84b2da52f"
auth_token = os.environ.get("AUTH_TOKEN")
API_KEY = os.environ.get("OWM_API_KEY")
END_POINT = "http://api.weatherapi.com/v1/forecast.json"
parameters = {
            "q" : "12.949230,75.381813",
            "key" : API_KEY,
            "forecastday" : "hour"

}

response = requests.get(url=END_POINT,params=parameters)
response.raise_for_status()
hourly_weather_data = response.json()["forecast"]["forecastday"][0]["hour"]
twelve_hour_data = hourly_weather_data[:12]

will_rain = False

for hour in twelve_hour_data:
    condition_code = int(hour["condition"]["code"])
    if condition_code > 1063:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella.",
        from_ = '+1 978 637 6556',
        to= f'{os.environ.get("PH_NO")}'
    )
    print(message.status)