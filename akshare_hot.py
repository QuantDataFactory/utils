#!/usr/bin/env python
# encoding: utf-8

# 热点

from typing import List
import akshare as ak


# 个股人气排行榜(实时排行榜)
def get_hot_rank_em() -> List[List]:
    hot_rank_em_df = ak.stock_hot_rank_em()
    return hot_rank_em_df[["当前排名", "代码", "股票名称", "最新价", "涨跌幅"]].values.tolist()


# 个股人气飙升榜(实时排行榜)
def get_hot_up_em() -> List[List]:
    hot_up_em_df = ak.stock_hot_up_em()
    return hot_up_em_df[["排名较昨日变动", "当前排名", "代码", "股票名称", "最新价", "涨跌幅"]].values.tolist()


# 个股人气排行榜历史趋势(过去365天数据 以天为周期）
def get_hot_rank_detail_em(symbol) -> List[List]:
    hot_rank_detail_em_df = ak.stock_hot_rank_detail_em(symbol)
    return hot_rank_detail_em_df[["时间", "排名", "证券代码", "新晋粉丝", "铁杆粉丝"]].values.tolist()


# 个股人气排行榜实时变动(当日数据 以10分钟为周期)
def get_hot_rank_detail_realtime_em(symbol) -> List[List]:
    hot_rank_detail_realtime_em_df = ak.stock_hot_rank_detail_realtime_em(symbol)
    return hot_rank_detail_realtime_em_df[["时间", "排名"]].values.tolist()


# 个股相关概念热度
def get_hot_keyword_em(symbol) -> List[List]:
    hot_keyword_em_df = ak.stock_hot_keyword_em(symbol)
    return hot_keyword_em_df[["时间", "股票代码", "概念名称", "概念代码", "热度"]].values.tolist()


# 个股排名详情
def get_hot_rank_latest_em(symbol) -> List[List]:
    hot_rank_latest_em_df = ak.stock_hot_rank_latest_em(symbol)
    return hot_rank_latest_em_df[["item", "value"]].values.tolist()


# 个股关联股票信息
def get_hot_rank_relate_em(symbol) -> List[List]:
    hot_rank_relate_em_df = ak.stock_hot_rank_relate_em(symbol)
    return hot_rank_relate_em_df[["时间", "股票代码", "相关股票代码", "涨跌幅"]].values.tolist()


if __name__ == '__main__':
    print(get_hot_rank_em())
    print(get_hot_up_em())
    print(get_hot_rank_detail_em("SH600089"))
    print(get_hot_rank_detail_realtime_em("SH600089"))
    print(get_hot_keyword_em("SH600089"))
    print(get_hot_rank_latest_em("SH600089"))
    print(get_hot_rank_relate_em("SH600089"))
