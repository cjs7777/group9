import requests
import re
import time
import os
import json

class Content():
    def __init__(self, userName, text, source, created_at, retweet_count, reply_count, reward_count, fav_count):
        self.userName = userName
        self.text = text
        self.source = source
        self.created_at = created_at
        self.retweet_count = retweet_count
        self.reply_count = reply_count
        self.reward_count = reward_count
        self.fav_count = fav_count

    def printData(self):
        print('用户名：' + self.userName)
        print('评论内容：' + self.text)
        print('来源：' + self.source)
        print('创建时间：' + self.created_at)
        print('转发数：' + str(self.retweet_count))
        print('评论数：' + str(self.reply_count))
        print('点赞数：' + str(self.reward_count))
        print('收藏数：' + str(self.fav_count))
        print("-" * 50)


class Website():
    def __init__(self, name, baseUrl, num, totalNum):
        '''提供参数'''
        self.name = name  # 一组参数名字
        self.baseUrl = baseUrl  # 基础url
        self.num = num  # 一个页面爬取数量
        self.totalNum = totalNum # 爬取数

class Crawler():
    def __init__(self, stock):
        self.query = {
            "u": 8580808395,
            "uuid": 1387233616647565312,
            "count": 10,
            "comment": 0,
            "symbol": "SH603517",
            "hl": 0,
            "source": "all",
            "sort": "",
            "page": 1,
            "q": "",
            "type": 11,
            "session_token": "null",
            "access_token": "1d297d0adc829df80cc2cf02eef605b275ac2a90",
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        self.query['symbol'] = stock

    def getUrl(self, baseUrl, pageNum):
        '''获取URL'''
        self.query['page'] = pageNum
        str1 = json.dumps(self.query)
        str1 = str1.translate(str1.maketrans({":": "=", ",": "&", "\"": "", " ": "", "{": "", "}": ""}))
        pageUrl = baseUrl + str1
        # print(pageUrl)
        return pageUrl

    def getPage(self, url):
        '''获取页面'''
        try:
            req = requests.get(url, headers=self.headers)  # 获取页面
            req.raise_for_status()
            page = json.loads(req.text)
        except:
            print("getPage Error!")
            return None
        return page

    def parse(self, site):
        '''解析'''
        contents = []
        for i in range(0, site.totalNum, site.num):
            time.sleep(5)

            pageUrl = self.getUrl(site.baseUrl, i + 1)

            # print(pageUrl)
            page = self.getPage(pageUrl)
            # print(page)
            if page == None:
                return []

            for j in range(site.num):
                userName = page['list'][j]['user']['screen_name']
                text = page['list'][j]['text']  # 用正则表达式，如果能匹配到就转成链接

                source = page['list'][j]['source']

                tracks = json.loads(page['list'][j]['trackJson'])
                created_at = tracks['created_at']
                retweet_count = tracks['retweet_count']
                reply_count = tracks['reply_count']
                reward_count = tracks['reward_count']
                fav_count = tracks['fav_count']

                content = Content(userName, text, source, created_at, retweet_count, reply_count, reward_count, fav_count)
                contents.append(content)
                content.printData()

                time.sleep(3)

        return contents
