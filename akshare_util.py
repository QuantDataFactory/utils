#!/usr/bin/env python
# encoding: utf-8
from typing import List
import akshare as ak


# 概念板块
def get_all_concept_name() -> List[str]:
    concepts_df = ak.stock_board_concept_name_em()
    return concepts_df["板块名称"].values.tolist()


# 行业板块
def get_all_industry_name() -> List[str]:
    industry_df = ak.stock_board_industry_name_em()
    return industry_df["板块名称"].values.tolist()


if __name__ == '__main__':
    print(get_all_concept_name())
    print(get_all_industry_name())
