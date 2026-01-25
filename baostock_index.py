#!/usr/bin/env python
# encoding: utf-8
from typing import List

import baostock as bs


# 获取中证50成分股
def get_sz50_stocks() -> List[List]:
    bs.login()
    query_sz50_stocks_df = bs.query_sz50_stocks()
    resp = query_sz50_stocks_df.get_data()[["code", "code_name"]].values.tolist()
    bs.logout()
    return resp


# 获取沪深300成分股
def get_hs300_stocks() -> List[List]:
    bs.login()
    query_hs300_stocks_df = bs.query_hs300_stocks()
    resp = query_hs300_stocks_df.get_data()[["code", "code_name"]].values.tolist()
    bs.logout()
    return resp


# 获取中证500成分股
def get_zz500_stocks() -> List[List]:
    bs.login()
    query_zz500_stocks_df = bs.query_zz500_stocks()
    resp = query_zz500_stocks_df.get_data()[["code", "code_name"]].values.tolist()
    bs.logout()
    return resp


if __name__ == "__main__":
    print(get_sz50_stocks())
    print(get_hs300_stocks())
    print(get_zz500_stocks())
