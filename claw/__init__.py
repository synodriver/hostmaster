# -*- coding: utf-8 -*-
from .website import IP, Website
from .web_parse import get_ip

__all__ = ["web_parse", "website"]

if __name__ == "__main__":
    print(get_ip("exhentai.org"))
