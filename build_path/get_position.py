import requests
from bs4 import BeautifulSoup

from get_district import get_district

def get_position():
    root_path = "https://bj.lianjia.com"
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
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
            res[district][item.get_text()] = root_path + item.get("href")
    return res

if __name__ == "__main__":
    print(get_position())
