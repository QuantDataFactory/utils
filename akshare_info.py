#!/usr/bin/env python
# encoding: utf-8

# 基本信息

from typing import List
import akshare as ak


# A股所有股票列表
def get_info_a_code_name() -> List[List]:
    info_a_code_name_df = ak.stock_info_a_code_name()
    return info_a_code_name_df[["code", "name"]].values.tolist()


# 上证所有股票列表
def get_info_sh_name_code() -> List[List]:
    info_sh_name_code_df = ak.stock_info_sh_name_code()
    return info_sh_name_code_df[["证券代码", "证券简称"]].values.tolist()


# 深证所有股票列表
def get_info_sz_name_code() -> List[List]:
    info_sz_name_code_df = ak.stock_info_sz_name_code()
    return info_sz_name_code_df[["A股代码", "A股简称"]].values.tolist()


# 北证所有股票列表
def get_info_bj_name_code() -> List[List]:
    info_bj_name_code_df = ak.stock_info_bj_name_code()
    return info_bj_name_code_df[["证券代码", "证券简称"]].values.tolist()


if __name__ == '__main__':
    print(get_info_a_code_name())
    print(get_info_sh_name_code())
    print(get_info_sz_name_code())
    print(get_info_bj_name_code())
