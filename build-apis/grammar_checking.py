import requests
import json

# Until now we've used get requests which pulls ready made data. With a post request we're going to send some data
# (text for us) and the server will process the text. This time the server processes on our data and return it after
# doing calculations/processing on it


url = "https://api.languagetool.org/v2/check"
# need to also include the data we're sending up
data = {
    'text': "Tis is a nixe day",
    'language': 'auto',

}
response = requests.post(url, data)
result = json.loads(response.text)
print(result)
