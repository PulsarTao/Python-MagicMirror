# -*- coding: utf-8 -*-
'''
Created on 2016年9月4日

@author: NowImSleepy
'''
class ApiConf():
    def Tuling(self):
            Tuling={"url":"http://www.tuling123.com/openapi/api",
                    "key":"d5f3fdfaccb93969a630f4e46751fde9",
                    "userid":"123456"}
            return Tuling
        
    def BaiduRest(self):
        BaiduRest={"url":"https://openapi.baidu.com/oauth/2.0/token",
                   "grant_type":"client_credentials",
                   "client_id":"72n3GYlVpc1n4du35GYOrT4X",
                   "client_secret":"3b83be694855a70b46590f18d17aec41"}
        return BaiduRest