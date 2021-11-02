
import datetime
import time
import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
# }
#
# for page_num in range(1, 78):  # 获取阳东数据
#     # time.sleep(2)
#     print('正在获取第', page_num, '页10个详情页信息')
#     url = 'http://219.129.189.10:9168/api/GzymApi/GetIndexSearchData?Jgid=d9602e29-1374-4860-8ad5-f259d239e446&PageIndex=' + str(page_num) + '&PageSize=10&Ysxmmc=&Ysxkzh=&Kfsmc=&Kfxmmc='
#     json_response = requests.get(url=url, headers=headers).json()
#
#     for data in json_response['Data']:
#         # print(data['YSXMID'])
#         # print(data['DJJG'])
#         new_url = 'http://219.129.189.10:9168/public/web/ysxm?ysxmid=' + data['YSXMID'] + '&jgid=' + data['DJJG']
#
#
#         print('new_url:',new_url)

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    print('开始时间：',start_time)

    time.sleep(61)
    end_time = datetime.datetime.now()
    print('完成时间',end_time)

    t = end_time - start_time
    print('时间差(单位：秒)',t)