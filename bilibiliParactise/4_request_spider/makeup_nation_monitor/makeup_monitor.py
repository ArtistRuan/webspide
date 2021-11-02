
"""
需求描述：
获取国家化妆品监督管理总局化妆品信息
URL：http://scxk.nmpa.gov.cn:81/xk/
"""


import requests
import json

def get_data():
    # 获取所有的id，保存到list
    id_list = []  # 保存所有id
    all_detail_list = []  # 保存所有详情数据
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        # 通过在页面中右键【检查】，然后找到【Network】，接着在【web?...】中找到User-Agent信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
    }

    for page in range(1,50):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }

        # response = requests.post(url=url,data=data,headers=headers).text
        response = requests.post(url=url, data=data, headers=headers).json()

        # 保存文件
        # file_name = './makeup.html'
        # fp = open(file_name,'w',encoding='utf-8')
        # json.dump(response,fp=fp,ensure_ascii=False)
        # fp.close()

        # print(response['list'])
        for data in response['list']:
            # print(data['ID'])
            id_list.append(data['ID'])
    print('获取到的数据条数:',len(id_list))

    # 详情信息所在url
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    #遍历id_list，用于做参数
    for id in id_list:
        data = {
            'id': id
        }
        # print(id)
        detail_json = requests.post(url=post_url,data=data,headers=headers).json()
        # detail_data_file = './detail_data_file.json'
        # fp = open(detail_data_file,'a+',encoding='utf-8')
        # json.dump(detail_json,fp=fp,ensure_ascii=False)
        # print(detail_json)
        all_detail_list.append(detail_json)
    # print(all_detail_list)
    #  持久化保存所有的详情数据
    detail_data_file = './detail_data_file.json'
    fp = open(detail_data_file,'w',encoding='utf-8')
    json.dump(all_detail_list,fp=fp,ensure_ascii=False)
    print('done')



def main():
    get_data()

if __name__ == '__main__':
    '''
    # url = 'http://scxk.nmpa.gov.cn:81/xk/'
    1、在网页的response找不到页内的内容，故这个是动态加载网站数据，所以用这个网站无法获取到数据，
    2、在原始网页 http://scxk.nmpa.gov.cn:81/xk/ 中，通过ajax查看了加载的数据返回的id
    3、然后通过点击网页数据进入到对应数据页面，循环第一步检查是否是数据页面，
       1）如果不是则循环第一步找真正的数据页面；
       2）如果是，则记录真正的url及参数，发现数据真正存在的网页是：http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById + id
    '''
    main()