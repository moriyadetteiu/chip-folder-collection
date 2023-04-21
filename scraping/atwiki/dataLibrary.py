import requests
from bs4 import BeautifulSoup

WIKI_URLS = {
    5: "https://w.atwiki.jp/www-iris/pages/1780.html"
}

def scrape_chips(version):
    req = requests.get(WIKI_URLS[version])
    req.encoding = req.apparent_encoding

    soup = BeautifulSoup(req.text, "html.parser")

    table = soup.find_all("table")[1]
    code_selector = "tr > td:nth-child(8),tr > td:nth-child(9),tr > td:nth-child(10),tr > td:nth-child(11)"
    chips = [
        {
            'name': tr.select_one("tr > td:nth-child(2) > a").text,
            'class': tr.select_one("tr > td:nth-child(4)").text,
            'attribute': tr.select_one("tr > td:nth-child(5) > a").text,
            'good_or_evil': tr.select_one("tr > td:nth-child(6)").text,
            'codes': [
                code.text for code in tr.select(code_selector) if code.text != ''
            ],
            'standard_size': int(tr.select_one("tr > td:nth-child(12)").text),
        } for tr in table.select("table > tr")
    ]
    return chips
