import requests

def get_news(topic, startTime, endTime, language="en", api_key="33dcd70b0eed415a94c7b47eb9d22068"):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={startTime}&to={endTime}&sortBy=" \
          f"popularity&language=en&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles= content["articles"]
    results = []
    for article in articles:
        results.append(f"TITLE - '{article['title']}, '\n\tDESCRIPTION - ', {article['description']}\n")
    return results

if __name__=="__main__":
    #print(get_news(topic="space", startTime="2022-9-28", endTime="2022-10-28"))
    out = get_news(topic="space", startTime="2022-9-28", endTime="2022-10-28")
    for l in out:
        print(l)