#!/usr/bin/env python
# encoding: utf-8
from typing import List, Optional

import baostock as bs


# 获取指定股票一段时间内的日K数据
# frequency: d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线
# adjustflag: 1:后复权 2:前复权 3:不复权
def get_history_k_data_daily(symbol: str, start_date: Optional[str], end_date: Optional[str]) -> List[List]:
    bs.login()
    query_history_k_data_df = (
        bs.query_history_k_data_plus(symbol,
                                     "date,code,open,high,low,close,volume,amount",
                                     start_date=start_date, end_date=end_date,
                                     frequency="d", adjustflag="2"))
    resp = query_history_k_data_df.get_data()[["date", "code", "open", "high",
                                               "low", "close", "volume", "amount"]].values.tolist()
    bs.logout()
    return resp


if __name__ == '__main__':
    print(get_history_k_data_daily("sz.000001", "2024-01-01", None))
