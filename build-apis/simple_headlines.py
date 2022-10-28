import requests

# enhancement on simple request, get the top news by country instead
def get_news(country, api_key="33dcd70b0eed415a94c7b47eb9d22068"):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    for article in articles:
        results.append(f"TITLE - '{article['title']}, '\n\tDESCRIPTION - ', {article['description']}\n")
    return results

if __name__=="__main__":
    out = get_news(country="us")
    for l in out:
        print(l)