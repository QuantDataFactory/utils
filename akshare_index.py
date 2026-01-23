#!/usr/bin/env python
# encoding: utf-8

# 指数

from typing import List
import akshare as ak


# 股票指数信息一览
def get_index_stock_info() -> List[List]:
    index_stock_info_df = ak.index_stock_info()
    return index_stock_info_df[["index_code", "display_name"]].values.tolist()


# 获成份股
def get_index_stock_cons(symbol: str) -> List[List]:
    index_stock_cons_df = ak.index_stock_cons(symbol)
    return index_stock_cons_df[["品种代码", "品种名称"]].values.tolist()


# 获取中证指数成份股
def get_index_stock_cons_csindex(symbol: str) -> List[List]:
    index_stock_cons_csindex_df = ak.index_stock_cons_csindex(symbol)
    return index_stock_cons_csindex_df[["指数代码", "指数名称", "指数英文名称", "成分券代码", "成分券名称",
                                        "成分券英文名称", "交易所", "交易所英文名称"]].values.tolist()


# 获取中证指数成份股权重
def get_index_stock_cons_weight_csindex(symbol: str) -> List[List]:
    index_stock_cons_weight_csindex_df = ak.index_stock_cons_weight_csindex(symbol)
    return index_stock_cons_weight_csindex_df[["指数代码", "指数名称", "指数英文名称", "成分券代码", "成分券名称",
                                               "成分券英文名称", "交易所", "交易所英文名称", "权重"]].values.tolist()


if __name__ == "__main__":
    print(get_index_stock_info())
    print(get_index_stock_cons("000300"))
    print(get_index_stock_cons_csindex("000905"))
    print(get_index_stock_cons_weight_csindex("000300"))
