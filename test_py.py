#!/usr/bin/python
# -*- coding: UTF-8 -*-

from news import News

a = News("标题", "时间", "作者", "描述", "字数")


with open("result.json", "a+", encoding='utf8') as f:
    f.write(a.to_str() + ',\n')
