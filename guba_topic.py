#!/usr/bin/env python
# encoding: utf-8
import urllib
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "gubatopic.eastmoney.com",
    "Origin": "https://gubatopic.eastmoney.com",
    "Referer": "https://gubatopic.eastmoney.com/",
}


# 获取股吧话题首页数据
def get_topic_home_page(page: int, limit: int):
    url = "https://gubatopic.eastmoney.com/interface/GetData.aspx"
    param = {
        "ps": limit,
        "p": page,
        "htid": 0,
        "code": "",
        "type": 0,
        "sort": 0,
    }
    params = {
        "path": "newtopic/api/Topic/HomePageListRead",
        "param": urllib.parse.urlencode(param),
        "env": 2,
    }
    data = urllib.parse.urlencode(params)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    return resp.json()


# 获取股吧历史话题数据
def get_topic_history(page: int, limit: int):
    url = "https://gubatopic.eastmoney.com/interface/GetData.aspx"
    param = {
        "ps": limit,
        "p": page,
        "htid": 0,
        "code": "",
        "type": 0,
        "sort": 0,
    }
    params = {
        "path": "newtopic/api/Topic/HistoryTopicRead",
        "param": urllib.parse.urlencode(param),
        "env": 2,
    }
    data = urllib.parse.urlencode(params)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    return resp.json()


if __name__ == "__main__":
    print(get_topic_home_page(page=0, limit=10))
    print(get_topic_history(page=0, limit=10))
