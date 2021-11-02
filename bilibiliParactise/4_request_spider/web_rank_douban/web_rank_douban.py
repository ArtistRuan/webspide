
"""
获取豆瓣网喜剧排名电影，一次获取20部
"""

import requests
import json
import func_timeout
import sys

@func_timeout.func_set_timeout(20)
def ask_input():
    return input('请20秒输入要查询的排名开始数，如排名第一则输入1\n')

def rank_list():

    try:
        willing_rank = ask_input()

        try:
            rank_no = int(willing_rank) - 1
            url = 'https://movie.douban.com/j/chart/top_list'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
            }

            param = {
                'type': '24',
                'interval_id': '100:90',
                'action': '',
                'start': rank_no,
                'limit': '20'
            }

            response = requests.get(url=url, headers=headers, params=param)

            json_list = response.json()

            # 保存到文件中
            file_name = './douban.json'
            with open(file_name, 'w', encoding='utf-8') as fp:
                json.dump(json_list, fp=fp, ensure_ascii=False)

            print('get data already!!!')
        except:
            print('输入错误，只允许输入阿拉伯数字')
            sys.exit(-1)


    except:
        print('超出输入时间，已退出')

    # if not willing_rank:
    #     rank_no = '0'
    # else:
    #     try:
    #         rank_no = int(willing_rank) - 1
    #     except Exception as e:
    #         print('输入的不是数据，请重新输入')



def main():
    rank_list()

if __name__ == '__main__':
    main()