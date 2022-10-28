import requests

#b2e4bd2d0a4a0d6179cf14d803150db7

#url = api.openweathermap.org/data/2.5/forecast?q={city}&appid={API key}

def my_get_weather(city, api_key="26631f0f41b95fb9f5ac0df9a8f43c92"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

    r = requests.get(url)
    content = r.json()
    info = content["list"]
    # We don't have to utilise a "for i in range(n)", just iterate over the actual thing!
    # whenever I'm iterating over i, check can I just iterate over the thing itself
    with open("weather_data.csv","a") as writefile:
        writefile.write("City,Time,Temperature,Condition\n")
        for i in range(3):
            time = info[i]["dt_txt"]
            temp = info[i]["main"]["temp"]
            condition = info[i]["weather"][0]["description"]
            line = ",".join((city, time, str(temp), condition))
            writefile.write(line + "\n")


def get_weather(city, api_key="26631f0f41b95fb9f5ac0df9a8f43c92"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"

    r = requests.get(url)
    content = r.json()
    with open("weather_data.csv","a") as writefile:
        for dicty in content["list"]:
            # In his case, he
            writefile.write(f'{dicty["dt_txt"]},{dicty["main"]["temp"]},{dicty["weather"][0]["description"]}\n')
    return content


if __name__=="__main__":
    get_weather("Dublin")