#!/usr/bin/env python
# encoding: utf-8

# 雪球

from typing import List
import akshare as ak


# 雪球关注排行榜(累积排行)
def get_stock_hot_follow_xq() -> List[List]:
    stock_hot_follow_xq_df = ak.stock_hot_follow_xq()
    return stock_hot_follow_xq_df[["股票代码", "股票简称", "关注", "最新价"]].values.tolist()


# 雪球讨论排行榜(累积排行)
def get_stock_hot_tweet_xq() -> List[List]:
    stock_hot_tweet_xq_df = ak.stock_hot_tweet_xq()
    return stock_hot_tweet_xq_df[["股票代码", "股票简称", "关注", "最新价"]].values.tolist()


# 雪球分享交易排行榜(累积排行)
def get_stock_hot_deal_xq() -> List[List]:
    stock_hot_deal_xq_df = ak.stock_hot_deal_xq()
    return stock_hot_deal_xq_df[["股票代码", "股票简称", "关注", "最新价"]].values.tolist()


if __name__ == '__main__':
    print(get_stock_hot_follow_xq())
    print(get_stock_hot_tweet_xq())
    print(get_stock_hot_deal_xq())
