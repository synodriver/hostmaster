# -*- coding: utf-8 -*-
from typing import List
import subprocess as sub
import os
from concurrent.futures import ThreadPoolExecutor, wait

"""
本模块提供必要的数据结构
"""


def is_connected(site=r'www.baidu.com'):
    """
    如果ping通site返回True
    :param site:
    :return: bool
    """
    if os.name == 'nt':
        cmd = f'ping -n 1 -w 1000 {site}'
        result = sub.Popen(cmd, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        A = result.stdout.read().decode('GBK')
        return A.find('Received = 1') != -1 or A.find('已接收 = 1') != -1
    elif os.name == 'posix':
        cmd = f'ping -c 1 -w 1 {site}'
        result = sub.Popen(cmd, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        A = result.stdout.read().decode('GBK')
        return A.find('1 received') != -1


def __init__():
    pass


class IP:
    def __init__(self, ip: str, addr: str = None):
        self.ip = ip
        self.addr = "" if addr is None else addr

    def is_connected(self):
        return is_connected(self.ip)

    def __str__(self):
        return f"{self.ip} {self.addr}"


class Website:
    """
    这个类提供网站的属性
    """

    def __init__(self, url: str, ips: List[IP] = None) -> None:
        """
        :param url: 网站的域名 如 exhentai.org
        :param ips: ["0.0.0.0","1.1.1.1"]之类的
        """
        self.url = url
        self.ips = [] if ips is None else ips
        self.usable_ips = []

    def __contains__(self, ip: str) -> bool:  # if i in xxx
        """
        检测一个网站是否拥有如下ip
        :param ip: 如"1.1.1.1"
        :return:
        """
        return ip in [i.ip for i in self.ips]

    def check_ip(self):
        """
        检查可以连接的ip
        :return:
        """
        with ThreadPoolExecutor() as p:
            result = p.map(IP.is_connected, list(self.ips))

        new_result = list(zip(self.ips, result))  # [(IP对象，True)]
        self.usable_ips = [i[0] for i in filter(lambda x: x[1], new_result)]  # List[IP]

    def __str__(self) -> str:
        if self.usable_ips:
            temp = [
                f"# {i.addr}" + "\n" + i.ip + " " + self.url + "\n"
                for i in self.usable_ips
            ]

            return "".join(temp)


if __name__ == "__main__":
    ip = IP("178.175.132.20", "厕所")
    print(ip.is_connected())
    a = Website("www.baidu.com", [IP("112.80.248.76", "莆田系医院"), IP("123.456.279.1", "精神病院")])
    a.check_ip()
    print(a.usable_ips)
    print(a)
