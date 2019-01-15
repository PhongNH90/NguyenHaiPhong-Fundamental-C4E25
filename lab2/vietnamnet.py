import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = "https://vietnamnet.vn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup = BeautifulSoup(content, "html.parser")

ul_news = soup.find("ul", "height-list")
li_list = ul_news.find_all("li")

new_list = []
for li in li_list:
    span = li.span
    a = span.a
    link = url + a["href"]
    title = a.string
    news = {
        "title": title,
        "link": link
    }
    new_list.append(OrderedDict(news))

pyexcel.save_as(records=new_list, dest_file_name="vietnamnet.xls")