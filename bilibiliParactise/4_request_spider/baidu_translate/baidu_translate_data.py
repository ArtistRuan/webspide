"""
需求描述：
模拟百度翻译，在网页中输入要翻译的内容，即可翻译到想要的内容
"""
import  requests
import func_timeout
import json

@func_timeout.func_set_timeout(20)
def askInput():
    return input('请20秒内输入要翻译的关键字/语句：\n')

def translate_bd():
    # 百度翻译url
    url = 'https://fanyi.baidu.com/sug'
    #ua
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    exit_code = False
    while not exit_code:
        try:
            print('')
            kw = askInput()
            exit_code = False
            param = {
                'kw': kw
            }

            response = requests.post(url=url, data=param, headers=headers)
            list_data = response.json()['data']
            # print(list_data)
            print('==============关键字/语句**"',kw,'"**的翻译结果 ==============')
            # 解析list数据，获取翻译结果
            for data in list_data:
                print('翻译结果', data['v'])
        except:
            exit_code = True
            print('输入超时，已退出!!!')

def main():
    translate_bd()

if __name__ == '__main__':
    main()

