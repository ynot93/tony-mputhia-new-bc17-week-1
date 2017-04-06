from urllib.request import urlopen
import _json

api_key = '61fa03afd214431ea7024c649688940f'
url = 'http://api.football-data.org'
json_object = urlopen(url)

data = json_object.read()

print(data)
