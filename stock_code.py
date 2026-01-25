#!/usr/bin/env python
# encoding: utf-8


def to_basic_type_stock_code(stock_code: str) -> str:
    if "." in stock_code:
        codes = stock_code.split(".")
        if codes[0].lower() in ("sh", "sz"):
            return codes[1]
        elif codes[1].lower() in ("sz", "sh"):
            return codes[0]
        else:
            return stock_code
    elif stock_code.lower().startswith("sz") or stock_code.lower().startswith("sh"):
        return stock_code[2:]
    else:
        return stock_code


def to_akshare_type_stock_code(stock_code: str) -> str:
    basic_type_code = to_basic_type_stock_code(stock_code)
    if basic_type_code.startswith("6"):
        return "SH" + basic_type_code
    elif basic_type_code.startswith("0") or basic_type_code.startswith("3"):
        return "SZ" + basic_type_code
    else:
        return stock_code


def to_baostock_type_stock_code(stock_code: str) -> str:
    basic_type_code = to_basic_type_stock_code(stock_code)
    if basic_type_code.startswith("6"):
        return "sh." + basic_type_code
    elif basic_type_code.startswith("0") or basic_type_code.startswith("3"):
        return "sz." + basic_type_code
    else:
        return stock_code


if __name__ == "__main__":
    print("----basic----")
    print(to_basic_type_stock_code("000001"))
    print(to_basic_type_stock_code("000001.SZ"))
    print(to_basic_type_stock_code("sz.000001"))
    print(to_basic_type_stock_code("SZ000001"))
    print("----akshare----")
    print(to_akshare_type_stock_code("000001"))
    print(to_akshare_type_stock_code("000001.SZ"))
    print(to_akshare_type_stock_code("sz.000001"))
    print(to_akshare_type_stock_code("SZ000001"))
    print("----baostock----")
    print(to_baostock_type_stock_code("000001"))
    print(to_baostock_type_stock_code("000001.SZ"))
    print(to_baostock_type_stock_code("sz.000001"))
    print(to_baostock_type_stock_code("SZ000001"))
