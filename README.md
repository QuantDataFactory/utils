# utils

基于 akshare 库的股票数据工具集，提供丰富的股票市场数据获取功能。

## 项目功能

该工具集包含以下模块：

### 1. 板块数据 (akshare_board.py)
- 获取概念板块列表
- 获取行业板块列表

### 2. 盘口异动 (akshare_change.py)
- 获取盘口异动数据
- 获取板块异动详情

### 3. 股票热点 (akshare_hot.py)
- 个股人气排行榜(实时)
- 个股人气飙升榜(实时)
- 个股人气排行榜历史趋势(365天)
- 个股人气排行榜实时变动(当日)
- 个股相关概念热度
- 个股排名详情

### 4. 股票基本信息 (akshare_info.py)
- A股所有股票列表
- 上证所有股票列表
- 深证所有股票列表
- 北证所有股票列表

### 5. 指数数据 (akshare_index.py)
- 获取股票指数信息一览
- 获取指数成份股
- 获取中证指数成份股
- 获取中证指数成份股权重

### 6. 股池数据 (akshare_pool.py)
- 涨停股池
- 昨日涨停股池
- 强势股池
- 炸板股池
- 跌停股池

### 7. 雪球数据 (akshare_xq.py)
- 雪球关注排行榜
- 雪球讨论排行榜
- 雪球分享交易排行榜

### 8. 股吧话题 (guba_topic.py)
- 获取股吧话题首页数据
- 获取股吧历史话题数据

### 9. 股吧热门 (guba_hot.py)
- 获取股吧热门排行榜数据
- 获取广场文章列表
- 获取精选文章列表

## 安装方法

1. 克隆仓库：
```bash
git clone https://github.com/QuantDataFactory/utils.git
cd utils
```

2. 使用 Pipfile 安装依赖：
```bash
pipenv install
```

3. 或直接使用 pip 安装：
```bash
pip install akshare
```

## 使用示例

### 获取概念板块列表
```python
from akshare_board import get_board_concept_name_em

concept_boards = get_board_concept_name_em()
print(concept_boards)
```

### 获取涨停股池
```python
from akshare_pool import get_zt_pool_em

# 获取指定日期的涨停股池
date = "20240120"
zt_stocks = get_zt_pool_em(date)
for stock in zt_stocks:
    print(stock)
```

### 获取个股人气排行榜
```python
from akshare_hot import get_hot_rank_em

hot_stocks = get_hot_rank_em()
for stock in hot_stocks:
    print(stock)
```

## 许可证

MIT License

## 依赖

- akshare - 金融数据接口库
- requests - HTTP请求库