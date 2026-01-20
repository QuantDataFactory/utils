#!/usr/bin/env python
# encoding: utf-8

# 板块

from typing import List
import akshare as ak


# 概念板块
def get_board_concept_name_em() -> List[str]:
    board_concept_name_em_df = ak.stock_board_concept_name_em()
    return board_concept_name_em_df["板块名称"].values.tolist()


# 行业板块
def get_board_industry_name_em() -> List[str]:
    board_industry_name_em_df = ak.stock_board_industry_name_em()
    return board_industry_name_em_df["板块名称"].values.tolist()


if __name__ == '__main__':
    print(get_board_concept_name_em())
    print(get_board_industry_name_em())
