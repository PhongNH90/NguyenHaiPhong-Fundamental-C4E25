import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

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

pyexcel.save_as(records=new_list, dest_file_name="itunes.xlsx")