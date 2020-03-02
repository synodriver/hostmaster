# -*- coding: utf-8 -*-
b = {"status": True, "code": 300, "msg": None,
     "data": [{"ip": "178.175.128.254", "sign": "e3ea0a5719972c34500fa346c7326046"},
              {"ip": "178.175.132.20", "sign": "118159c51e7e9cb80a34394a6bb6e09d"},
              {"ip": "178.175.132.22", "sign": "01d77d99c5d5a7da004c4869d9593469"},
              {"ip": "178.175.128.252", "sign": "7a4379b1cc03d61f449f0f4610d3272b"},
              {"ip": "178.175.129.254", "sign": "c74ae0ae9f1f370e86a5ed83fc568267"},
              {"ip": "178.175.129.252", "sign": "9569b20cbbcf55c5e9c29134ad48d48a"}]}

if __name__ == '__main__':
    from claw import get_ip, Website
    a = get_ip("exhentai.org")
    print(a)
    ex = Website("exhentai.org", a)
    ex.check_ip()
    print(ex.usable_ips)
    print(ex)
