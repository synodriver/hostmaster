# -*- coding: utf-8 -*-
"""
https://api.ip138.com/query/?ip=178.175.129.254&oid=5&mid=5&datatype=jsonp&sign=c74ae0ae9f1f370e86a5ed83fc568267&
callback=jsonp_003896287272503862
从ip138获取指定域名的IP写入host
get方法
https://www.ip138.com/
https://site.ip138.com/domain/write.do?input=exhentai.org&token=d5a817ae4975d91a491f267a8204b330
HTTP/1.0	GET	200	text/html		63.88 毫秒	document
各种加密 呕…………
https://site.ip138.com/domain/read.do?domain=exhentai.org&time=1582959972265
"""
__author__ = "帝国皇家近卫军"
__version__ = "1.0"

import json
from claw import get_ip, Website

# 浏览器的useragent，可以用很多个
agents = []


def update_host(host: str, path: str) -> None:
    with open(path, "w", encoding="utf-8", ) as f:
        f.write(host)


def main() -> None:
    print('*' * 30 + "正在更新host" + '*' * 30)
    with open("config.json", 'r') as f:
        config = json.load(f)
    host_path = config["host_path"]  # List[str]
    domains = config["domains"]  # List[str]
    # 取host模板
    with open("model.txt", 'r') as f:
        model = f.read()
    words = model
    websites = []  # List[Website]
    for i in domains:
        websites.append(Website(i, get_ip(i)))
    for i in websites:
        print("正在检查%s可用的ip" % (i.url,))
        i.check_ip()
        print("检查%s完成" % (i.url,))
        words += str(i)
    update_host(words, host_path)
    print(words)
    print("修改成功")


if __name__ == "__main__":
    main()
