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
table = soup.find("table",id = "tableContent")
tr_list = table.find_all("tr")


#3. Copy & Save 
data_list = []
for tr in tr_list:
    td_list = tr.find_all("td")
    for td in td_list:
        data = td.string
        figures = {
        "data": data,
        }
        data_list.append(OrderedDict(figures))

pyexcel.save_as(records=data_list, dest_file_name="BCTC Vinamilk.xlsx")