#!/usr/bin/env python
# encoding: utf-8
from typing import Dict, List

import akshare as ak


# 概念板块
def get_all_concept_name() -> List[str]:
    concepts_df = ak.stock_board_concept_name_em()
    return concepts_df["板块名称"].values.tolist()


# 行业板块
def get_all_industry_name() -> List[str]:
    industry_df = ak.stock_board_industry_name_em()
    return industry_df["板块名称"].values.tolist()


# 个股人气排行榜(实时排行榜)
def get_hot_rank() -> List[List]:
    hot_rank_df = ak.stock_hot_rank_em()
    return hot_rank_df[["当前排名", "代码", "股票名称", "最新价", "涨跌幅"]].values.tolist()


# 个股人气飙升榜(实时排行榜)
def get_hot_up() -> List[List]:
    hot_up_df = ak.stock_hot_up_em()
    return hot_up_df[["排名较昨日变动", "当前排名", "代码", "股票名称", "最新价", "涨跌幅"]].values.tolist()


# 个股人气排行榜历史趋势(过去365天数据 以天为周期）
def get_hot_rank_detail(symbol) -> List[List]:
    hot_rank_detail_df = ak.stock_hot_rank_detail_em(symbol)
    return hot_rank_detail_df[["时间", "排名", "证券代码", "新晋粉丝", "铁杆粉丝"]].values.tolist()[:-1]


# 个股人气排行榜实时变动(当日数据 以10分钟为周期)
def get_hot_rank_detail_realtime(symbol) -> List[List]:
    hot_rank_detail_realtime_df = ak.stock_hot_rank_detail_realtime_em(symbol)
    return hot_rank_detail_realtime_df[["时间", "排名"]].values.tolist()


# 个股相关概念热度
def get_hot_keyword(symbol) -> List[List]:
    hot_keyword_df = ak.stock_hot_keyword_em(symbol)
    return hot_keyword_df[["时间", "股票代码", "概念名称", "概念代码", "热度"]].values.tolist()


# 个股排名详情
def get_hot_rank_latest(symbol) -> List[List]:
    hot_rank_latest_df = ak.stock_hot_rank_latest_em(symbol)
    return hot_rank_latest_df[["item", "value"]].values.tolist()


# 个股关联股票信息
def get_hot_rank_relate(symbol) -> List[List]:
    hot_rank_relate_df = ak.stock_hot_rank_relate_em(symbol)
    return hot_rank_relate_df[["时间", "股票代码", "相关股票代码", "涨跌幅"]].values.tolist()


if __name__ == '__main__':
    print(get_all_concept_name())
    print(get_all_industry_name())
    print(get_hot_rank())
    print(get_hot_up())
    print(get_hot_rank_detail("SH600089"))
    print(get_hot_rank_detail_realtime("SH600089"))
    print(get_hot_keyword("SH600089"))
    print(get_hot_rank_latest("SH600089"))
    print(get_hot_rank_relate("SH600089"))
