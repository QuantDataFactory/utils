#!/usr/bin/env python
# encoding: utf-8

import time


def get_time_str_from_timestamp(timestamp: int) -> str:
    fmt = "%Y-%m-%d %H:%M:%S"
    return time.strftime(fmt, time.localtime(timestamp))


def get_date_str_from_timestamp(timestamp: int) -> str:
    fmt = "%Y%m%d"
    return time.strftime(fmt, time.localtime(timestamp))


if __name__ == "__main__":
    print(get_time_str_from_timestamp(0))
    print(get_date_str_from_timestamp(0))
