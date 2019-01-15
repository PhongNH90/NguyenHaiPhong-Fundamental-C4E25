import pyexcel
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup = BeautifulSoup(content, "html.parser")

#2. Find ROI
table = soup.find("table", "tableContent")
tr_list = table.find_all("tr")


#3. Copy & Save 
new_list = []
for tr in tr_list:
    td_list = tr_list.find_all("td")
    artist = li.h4.a.string
    link = li.h4.a["href"]

    news = {
        "song": song,
        "artist": artist,
        "link": link
    }
    new_list.append(OrderedDict(news))

pyexcel.save_as(records=new_list, dest_file_name="itunes.xlsx")