from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml
html = urlopen("https://www.baidu.com/more/")
bsObj = BeautifulSoup(html,"html.parser")
for link in bsObj.select('div .con'):
    for i in link.find_all("a"):
        print(i.get_text())
        print(i['href'])
    print(link.find_all("span")[0].get_text())
