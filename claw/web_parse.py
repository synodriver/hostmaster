# -*- coding: utf-8 -*-
import requests
from typing import List
from .website import IP

"""
本文件负责解析网页

a = {"status": True, "code": 300, "msg": None,
     "data": [{"ip": "178.175.128.254", "sign": "e3ea0a5719972c34500fa346c7326046"},
              {"ip": "178.175.132.20", "sign": "118159c51e7e9cb80a34394a6bb6e09d"},
              {"ip": "178.175.132.22", "sign": "01d77d99c5d5a7da004c4869d9593469"},
              {"ip": "178.175.128.252", "sign": "7a4379b1cc03d61f449f0f4610d3272b"},
              {"ip": "178.175.129.254", "sign": "c74ae0ae9f1f370e86a5ed83fc568267"},
              {"ip": "178.175.129.252", "sign": "9569b20cbbcf55c5e9c29134ad48d48a"}]}
              
{"ret":"ok","ip":"178.175.128.254","data":["摩尔多瓦","","","","","00373"]}
"""

site = "https://site.ip138.com/domain/read.do?domain="

site_for_addr = "https://api.ip138.com/query/?ip=178.175.132.22&oid=5&mid=5&datatype=\
jsonp&sign="


def __init__():
    pass


header1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/76.0.3809.100 Safari/537.36",
    "Host": "site.ip138.com",
    # "Cookie": "PHPSESSID = 5\
    #     r4d0jp7ou6rpesn5ivt1f8ro5;\
    #     Hm_lpvt_d39191a0b09bb1eb023933edaa468cd5 = 1582984318;\
    #     Hm_lvt_d39191a0b09bb1eb023933edaa468cd5 = 1582817205, 1582959802, 1582959818, 1582959972"
    # Referer: https: // site.ip138.com / exhentai.org /
}
header2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/76.0.3809.100 Safari/537.36",
    "Host": "api.ip138.com",
    "Accept": "text / html, application / xhtml + xml, application / xml;\
            q = 0.9, * / *; q = 0.8",
    "Accept - Language": "zh - Hans - CN, zh - Hans;\
    q = 0.8, zh - Hant - TW;\
    q = 0.7, zh - Hant;\
    q = 0.5, en - US;\
    q = 0.3, en;\
    q = 0.2",
    "Upgrade - Insecure - Requests": "1"
}


def get_ip(url: str) -> List[IP]:
    """
    :param url: 要查询的域名
    :return: ip对象
    """
    try:
        header1["Referer"] = f"https://site.ip138.com/{url}/"
        header2["Referer"] = f"https://site.ip138.com/{url}/"
        html = requests.get(site + url, headers=header1).json()
        ips = [i["ip"] for i in html["data"]]  # List[str]

        signs = [i["sign"] for i in html["data"]]  # List[str]
        # print(ips[0], '  ', signs[0])
        temp = zip(ips, signs)
        addrs_text = [
            requests.get(
                f"https://api.ip138.com/query/?ip={i[0]}"
                + "&oid=5&mid=5&datatype=jsonp\
        &sign="
                + i[1],
                headers=header2,
            ).text
            for i in list(temp)
        ]

        indexes = [(i.index("\t") + 1, i.index(" ")) for i in addrs_text]
        addrs = [i[0][i[1][0]:i[1][1]] for i in zip(addrs_text, indexes)]  # List[str]

        return [IP(i[0], i[1]) for i in zip(ips, addrs)]
    except KeyError as e:
        print(html)
        print(e.args)
        print("被网站限制了，去刷新")
        raise e

"""
https://api.ip138.com/query/?ip=178.175.128.254&oid=5&mid=5&datatype=jsonp&sign=e3ea0a5719972c34500fa346c7326046
"""
