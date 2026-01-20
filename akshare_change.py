#!/usr/bin/env python
# encoding: utf-8

# 异动

from typing import List
import akshare as ak

symbol_map = {
    "火箭发射": "8201",
    "快速反弹": "8202",
    "大笔买入": "8193",
    "封涨停板": "4",
    "打开跌停板": "32",
    "有大买盘": "64",
    "竞价上涨": "8207",
    "高开5日线": "8209",
    "向上缺口": "8211",
    "60日新高": "8213",
    "60日大幅上涨": "8215",
    "加速下跌": "8204",
    "高台跳水": "8203",
    "大笔卖出": "8194",
    "封跌停板": "8",
    "打开涨停板": "16",
    "有大卖盘": "128",
    "竞价下跌": "8208",
    "低开5日线": "8210",
    "向下缺口": "8212",
    "60日新低": "8214",
    "60日大幅下跌": "8216",
}

reversed_symbol_map = {v: k for k, v in symbol_map.items()}


# 盘口异动
def get_changes_em(symbol: str) -> List[List]:
    changes_em_df = ak.stock_changes_em(symbol)
    return changes_em_df[["时间", "代码", "名称", "板块", "相关信息"]].values.tolist()


# 板块异动详情
def get_board_change_em() -> List[List]:
    board_change_em_df = ak.stock_board_change_em()
    return board_change_em_df[["板块名称", "涨跌幅", "主力净流入", "板块异动总次数",
                               "板块异动最频繁个股及所属类型-股票代码",
                               "板块异动最频繁个股及所属类型-股票名称",
                               "板块异动最频繁个股及所属类型-买卖方向",
                               "板块具体异动类型列表及出现次数"]].values.tolist()


if __name__ == '__main__':
    print(get_changes_em(symbol="大笔买入"))
    print(get_board_change_em())
