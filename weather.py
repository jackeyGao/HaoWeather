# -*- coding: utf-8 -*-
'''
File Name: weather.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 二  9/30 11:41:49 2014
'''

import requests
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

""" 申请链接http://www.haoservice.com/center?subNav=apply
    请求权限
    包月体验用户：50  次/天
    初级用户：1500  次/天
    中级用户：15000  次/天
    高级用户：30000  次/天
    VIP用户：100000  次/天
    超级不限次用户：不限  次/天
    资费标准
    包月体验用户：0.00  元/月
    初级用户：19.00  元/月
    中级用户：99.00  元/月
    高级用户：299.00  元/月
    VIP用户：499.00  元/月
    超级不限次用户：999.00  元/月
"""
KEY = '7975e40caea94affa97d9d4277642446'


class Weather:

    def __init__(self, cityname):
        self.cityname = cityname
        self.api_key = KEY
        self.api_url = 'http://apis.haoservice.com/weather?cityname=%s&key=%s'\
                % (self.cityname, self.api_key)
        self.data = self.getResponse()


    def getResponse(self):
        res = requests.get(self.api_url)
        data = json.loads(res.text)
        return data

    def getResponseFromLocal(self):
        with open('json', 'r') as f:
            content = f.read()

        data = json.loads(content)
        return data


    def showJson(self):
        return json.dumps(self.data, sort_keys=True, indent=2)


    def getToday(self):
        message = u'''今天是{date_y} {week}, {city}天气{weather}, 温度区间{temperature}.预计'''\
                .format(**self.data["result"]["today"])
        return message

    def getFuture(self):
        humanDate = { 1:'明天', 2:'后天', 3: '大后天' }
        futures = self.data["result"]["future"]

        data = [ (humanDate.get(i, futures[i]["week"]), futures[i]["weather"], futures[i]["temperature"]) \
                for i in range(1,6) ]
        return data

    def showFullMessage(self):
        future = self.getFuture()
        futureMessage = u''
        todayMessage = self.getToday()
        for i in future:
            futureMessage += u'{0} {1} {2},'.format(i[0], i[1], i[2])

        FullMessage = todayMessage + futureMessage.strip(',') + '.'
        return FullMessage


if __name__ == '__main__':
    wt = Weather('商丘')
    print wt.showFullMessage()

        

