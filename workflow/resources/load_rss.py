# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

import json

def load_config_with(path):
    with open(path, "r") as fp:
        data = json.loads(fp.read())
    return data

r = load_config_with("rss.json")
print(r)
rr = json.dumps(r, indent=4, ensure_ascii=False)
print(rr)