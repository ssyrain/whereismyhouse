import requests
from bs4 import BeautifulSoup
import json

from get_district import get_district

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

def get_position(dump_res=False):
    root_path = "https://bj.lianjia.com"
    res = {}
    district_urls = get_district()
    for district in district_urls.keys():
        res[district] = {}
        district_url = district_urls[district]
        page = requests.get(district_url, headers=header)
        soup = BeautifulSoup(page.text, "lxml")
        items = soup.find_all("div", attrs={"data-role": "ershoufang"})
        position_urls = items[0].find_all("div")[1].find_all("a")
        for item in position_urls:
            res[district][item.get_text()] = {}
            url = root_path + item.get("href")
            res[district][item.get_text()]["url"] = url
            res[district][item.get_text()]["page_count"] = get_total_page(url)
    if dump_res:
        with open('./data.json', 'w') as f:
            json.dump(res, f)
    return res

def get_total_page(url):
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, "lxml")
    items = soup.find_all("div", class_="page-box house-lst-page-box")
    try:
        return eval(items[0].get("page-data")).get("totalPage")
    except:
        return 0

if __name__ == "__main__":
    print(get_position(dump_res=True))
