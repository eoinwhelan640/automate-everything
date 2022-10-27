import requests
from datetime import datetime as dt
import time

# We'll convert these into unix epoch times
ticker = input("Enter ticker symbol: ").upper()
from_date = input("Enter start date in format yyyy/mm/dd: ")
from_datetime = dt.strptime(from_date, '%Y/%m/%d')
from_epoch = int(time.mktime(from_datetime.timetuple()))

to_date = input("Enter end date in format yyyy/mm/dd: ")
to_datetime = dt.strptime(to_date, '%Y/%m/%d')
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&" \
      f"interval=1d&events=history&includeAdjustedClose=true"
print(url)
# Trying to do this alone would be foridden. Websites don't like scripts hitting them, so need to act like we're a
# browser by using the headers
#content = requests.get(lulu).content
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/88.0.4324.96 Safari/537.36"}

# using content ensures bytes and is a more general approach, we could specify "text" and get string data
# but if we're getting mp3/images/data etc its good to stay generic
content = requests.get(url, headers=headers).content
# get it back as byte object. Need to write it down as byte file so we have it locally
print(type(content))

# It's pretty handy that the content is in bytes, so whe  we write down with wb it comes out in the correct csv format
with open("stock.csv","wb") as write_file:
       write_file.write(content)


