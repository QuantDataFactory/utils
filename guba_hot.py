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
def get_hot_ranking(limit: int):
    url = "https://gubatopic.eastmoney.com/interface/GetData.aspx"
    param = {
        "pageSize": limit,
        "condition": "",
        "origin": "",
    }
    params = {
        "path": "/operation/api/HotRanking/List",
        "param": urllib.parse.urlencode(param),
        "env": 2,
    }
    data = urllib.parse.urlencode(params)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    return resp.json()


# 广场
def get_hot_post_square(page: int, limit: int):
    url = "https://gubatopic.eastmoney.com/interface/GetData.aspx"
    param = {
        "ps": limit,
        "p": page,
        "pageOffset": 1,
        "uid": "",
        "euid": "not_logged_in_euid",
    }
    params = {
        "path": "/hotpost/api/Square/ArticleList",
        "param": urllib.parse.urlencode(param),
        "env": 2,
    }
    data = urllib.parse.urlencode(params)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    return resp.json()


# 精选
def get_hot_post_selection(page: int, limit: int):
    url = "https://gubatopic.eastmoney.com/interface/GetData.aspx"
    param = {
        "ps": limit,
        "p": page,
        "pageOffset": 1,
        "uid": "",
        "euid": "not_logged_in_euid",
    }
    params = {
        "path": "/hotpost/api/Selection/Articlelist",
        "param": urllib.parse.urlencode(param),
        "env": 2,
    }
    data = urllib.parse.urlencode(params)
    resp = requests.post(url, data=data, headers=headers, timeout=10)
    return resp.json()


if __name__ == "__main__":
    print(get_hot_ranking(50))
    print(get_hot_post_square(20, 0))
    print(get_hot_post_selection(20, 0))
