#!/bin/python
# -*- coding:UTF-8 -*-

import prettytable as pt

# 显示坐席
def show_ticket(row_num):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位A','座位B','座位C','座位D','座位F']
    for i in range(row_num):
        lst=[f'第{i + 1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)

# 订票
def order_ticket(row_num,row,column):
    print('row的值：',row)
    print('column的值：',column)
    # 13,F
    tb = pt.PrettyTable()
    tb.field_names = ['排号', '座位A', '座位B', '座位C', '座位D', '座位F' ]
    for row_no in range(row_num): # range(13):0..12
        row_no+=1
        if row_no == int(row) and column == 'A':
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(1)] = '已售'
            tb.add_row(lst)
        elif row_no == int(row) and column == 'B':
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(2)] = '已售'
            tb.add_row(lst)
        elif row_no == int(row) and column == 'C':
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(3)] = '已售'
            tb.add_row(lst)
        elif row_no == int(row) and column == 'D':
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(4)] = '已售'
            tb.add_row(lst)
        elif row_no == int(row) and column == 'F':
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(5)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
            # print('无此座位，请重新选择')
            # order_ticket(row_num,row,column)
    # else:
    #     lst = [f'第{row_no}行', '有票', '有票', '有票', '有票', '有票']
    #     tb.add_row(lst)
    #     print('执行这里啦')
    #     # print('输入格式有误，如13排F号座位，请输入13,F')
    print(tb)

    # d = dict(eval(str(tb)))
    with open('tickets.txt','w',encoding='utf-8') as wfile:
        wfile.write(str(tb))
    # show_ticket(row_num)

if __name__ == '__main__':
    row_num = 13

    show_ticket(row_num)

    choose_num=input('请输入选择的座位,如13,F表示13排F号座位\n')
    try:
        row,column=choose_num.split(',')
        print('排号：',row)
        print('座位号：',column)
    except:
        print('输入格式有误，如13排F号座位，请输入13,F')
    order_ticket(row_num,row,column)