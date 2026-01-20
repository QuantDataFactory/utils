#!/usr/bin/env python
# encoding: utf-8
import time
# 股池

from typing import List
import akshare as ak


# 涨停股池
def get_zt_pool_em(date_str: str) -> List[List]:
    zt_pool_em_df = ak.stock_zt_pool_em(date_str)
    return zt_pool_em_df[["代码", "名称", "涨跌幅", "最新价", "成交额", "流通市值", "总市值",
                          "换手率", "封板资金", "首次封板时间", "最后封板时间", "炸板次数",
                          "涨停统计", "连板数", "所属行业"]].values.tolist()


# 昨日涨停股池
def get_zt_pool_previous_em(date_str: str) -> List[List]:
    zt_pool_previous_em_df = ak.stock_zt_pool_previous_em(date_str)
    return zt_pool_previous_em_df[["代码", "名称", "涨跌幅", "最新价", "成交额", "流通市值", "总市值",
                                   "换手率", "涨速", "振幅", "昨日封板时间", "昨日连板数",
                                   "涨停统计", "所属行业"]].values.tolist()


# 强势股池
def get_zt_pool_strong_em(date_str: str) -> List[List]:
    zt_pool_strong_em_df = ak.stock_zt_pool_strong_em(date_str)
    return zt_pool_strong_em_df[["代码", "名称", "涨跌幅", "最新价", "成交额", "流通市值", "总市值",
                                 "换手率", "涨速", "是否新高", "量比",
                                 "涨停统计", "入选理由", "所属行业"]].values.tolist()


# 炸板股池
def get_zt_pool_zbgc_em(date_str: str) -> List[List]:
    zt_pool_zbgc_em_df = ak.stock_zt_pool_zbgc_em(date_str)
    return zt_pool_zbgc_em_df[["代码", "名称", "涨跌幅", "最新价", "成交额", "流通市值", "总市值",
                               "换手率", "涨速", "振幅", "首次封板时间", "炸板次数",
                               "涨停统计", "所属行业"]].values.tolist()


# 跌停股池
def get_zt_pool_dtgc_em(date_str: str) -> List[List]:
    zt_pool_dtgc_em_df = ak.stock_zt_pool_dtgc_em(date_str)
    return zt_pool_dtgc_em_df[["代码", "名称", "涨跌幅", "最新价", "成交额", "流通市值", "总市值", "动态市盈率",
                               "换手率", "封单资金", "最后封板时间", "板上成交额",
                               "连续跌停", "开板次数", "所属行业"]].values.tolist()


if __name__ == "__main__":
    from __init__ import get_date_str_from_timestamp

    date_str = get_date_str_from_timestamp(int(time.time()))

    print(get_zt_pool_em(date_str))
    print(get_zt_pool_previous_em(date_str))
    print(get_zt_pool_strong_em(date_str))
    print(get_zt_pool_zbgc_em(date_str))
    print(get_zt_pool_dtgc_em(date_str))
