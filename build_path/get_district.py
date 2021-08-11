import requests
from bs4 import BeautifulSoup

def get_district(is_pc=True):
    url = "https://bj.lianjia.com/ershoufang/rs/"
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res_root = "https://bj.lianjia.com"
    if not is_pc:
        res_root = "https://m.lianjia.com/bj"

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, "lxml")

    res = {}
    position = soup.find_all("div", attrs={"data-role": "ershoufang"})
    items = position[0].contents[1].find_all("a")
    for item in items:
        child_items = item.get("href").split("/")
        res[item.get_text()] = res_root + "/".join([child_items[0], child_items[1], "index", child_items[2]])
    return res

if __name__ == "__main__":
    print(get_district())
    print(get_district(is_pc=False))
