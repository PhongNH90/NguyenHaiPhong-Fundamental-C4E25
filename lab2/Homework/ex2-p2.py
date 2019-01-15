import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from youtube_dl import YoutubeDL


url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup = BeautifulSoup(content, "html.parser")

#2. Find ROI
section = soup.find("section", "section chart-grid")
li_list = section.find_all("li")
# print(li_list)

#3. Copy & Save 
new_list = []
for li in li_list:
    song = li.h3.a.string
    artist = li.h4.a.string
    link = li.h4.a["href"]

    news = {
        "song": song,
        "artist": artist,
        "link": link
    }
    new_list.append(OrderedDict(news))
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
dl = YoutubeDL(options)
dl.download(["Connection", "One Republic"])