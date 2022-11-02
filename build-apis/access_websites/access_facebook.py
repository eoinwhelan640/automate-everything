import requests
import json

# How to download a facebook photo from my account
# url to my photo as found through fbs api interface
url = "https://graph.facebook.com/v15.0/1654149711325427?fields=link%2Cimages&access_token=<some_token>"

response = requests.get(url)
data = json.loads(response.text)

image_url = data["images"][0]["source"]
# now grab the image
image_bytes = requests.get(image_url).content

with open("image.jpg", "wb") as file:
    file.write(image_bytes)





