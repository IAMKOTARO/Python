# -*- Coding: utf-8 -*-

from datetime import datetime

WAREKI_BEGIN = {
    '令和':datetime(2019, 5, 1),
    '平成':datetime(1989, 1, 8),
    '昭和':datetime(1926, 12, 25)
    }

def translator(y, m, d):
    if datetime(y, m, d) >= WAREKI_BEGIN['令和']:
        year = (y - WAREKI_BEGIN['令和'].year) + 1
        w_str = '令和'
    elif datetime(y, m, d) >= WAREKI_BEGIN['平成']:
        year = (y - WAREKI_BEGIN['平成'].year) + 1
        w_str = '平成'
    elif datetime(y, m, d) >= WAREKI_BEGIN['昭和']:
        year = (y - WAREKI_BEGIN['昭和'].year) + 1
        w_str = '昭和'
    else:
        return '昔すぎます'
    if year == 1:
        year = '元'
    return w_str + str(year) + '年'

def main():
    print(translator(1990, 10,  1)+ '10月1日')
    print(translator(2019,  4, 30)+ '4月30日')
    print(translator(2019,  5,  1)+ '5月1日')

if __name__ == '__main__':
   main()
