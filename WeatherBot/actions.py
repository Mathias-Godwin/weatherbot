from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionWeather(Action):
	def name(self):
	    return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
            import requests
            loc = tracker.get_slot('location')
            params = {
              'access_key': '1b490d719183c8cbeda0577c9b7144e4',
              'query': loc
            }
            api_result = requests.get('http://api.weatherstack.com/current', params, verify=False)
            current = api_result.json()
		
	    country = current['location']['country']
	    city = current['location']['name']
	    condition = current['current']['weather_descriptions']
	    temperature_c = current['current']['temperature']
	    humidity = current['current']['humidity']
	    wind_mph = current['current']['wind_speed']
	    response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

	    dispatcher.utter_message(response)
	    return [SlotSet('location',loc)]

