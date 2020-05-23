import requests
from lxml import etree
from opdata.opexcel import Operatingexcel

# 小例子，获取虎扑体育NBA球星数据
def use_requsert_dome():
    url = 'https://nba.hupu.com/stats/players'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    response = requests.get(url,headers)
    if response.status_code == 200:
        return response.text
    else:
        return None
def text_to_dic(text):
    dict = {}
    html = etree.HTML(text)
    pags = html.xpath('//*[@id="data_js"]/div[4]/div/table/tbody')
    for i in pags:
        name = i.xpath('//tr/td[2]/a/text()')
        team = i.xpath('//tr/td[3]/a/text()')
        score = i.xpath('//tr/td[4]/text()')
        hit_shoot = i.xpath('//tr/td[5]/text()')
        hit_rate = i.xpath('//tr/td[6]/text()')
        hit_rate_3 = i.xpath('//tr/td[8]/text()')
        hit_rate_f = i.xpath('//tr/td[10]/text()')
        session = i.xpath('//tr/td[11]/text()')
        time = i.xpath('//tr/td[12]/text()')
    dict["name"]=name
    dict["team"] = team
    dict["score"] = score[1:]
    dict["hit_shoot"] = hit_shoot[1:]
    dict["hit_rate"] = hit_rate[1:]
    dict["hit_rate_3"] = hit_rate_3[1:]
    dict["hit_rate_f"] = hit_rate_f[1:]
    dict["session"] = session[1:]
    dict["time"] = time[1:]
    return dict

if __name__ == '__main__':
    text = use_requsert_dome()
    if text != None:
        dict = text_to_dic(text)
        ol = Operatingexcel()
        ol.set_excel_dic(dict,"data\csdn_data.xlsx",0,0)