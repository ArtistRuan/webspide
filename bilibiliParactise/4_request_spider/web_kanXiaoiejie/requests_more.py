# coding:utf-8

import requests # 第三方模块 pip install requests
import re # 正则表达式模块 内置模块
import time
import concurrent.futures
import os
import parsel

# 发送请求
def get_response(html_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    # 为什么这里要 requests.get()  post() 请求会更安全...
    response = requests.get(url=html_url, headers=headers)
    return response

# 保存数据
def save(title, img_url):
    img_data = requests.get(img_url).content
    img_name = img_url.split('/')[-1]
    with open("img\\" + title + '\\' + img_name, mode='wb') as f:
        f.write(img_data)

# 解析数据 获取图片url地址以及标题
def parse_1(data_html):
    zip_data = re.findall('<a href="(.*?)" target="_blank"rel="bookmark">(.*?)</a>', data_html, re.S)
    return zip_data

# 解析数据 获取图片url地址以及标题
def parse_2(html_data):
    selector = parsel.Selector(html_data)
    img_list = selector.css('p>img::attr(src)').getall()
    return img_list

# 创建文件夹
def mkdir_img(title):
    if not os.path.exists('img\\' + title):
        os.mkdir('img\\' + title)

# 主函数
def main(html_url):
    html_data = requests.get(html_url).text
    zip_data = parse_1(html_data)
    for url, title in zip_data:
        mkdir_img(title)
        html_data_2 = get_response(url).text
        img_list = parse_2(html_data_2)
        for img in img_list:
            save(title, img)
        print(title, '爬取成功！！！')


# 程序入口
if __name__ == '__main__':
    time_1 = time.time()
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    for page in range(1, 11):
        url = f'https://www.kanxiaojiejie.com/page/{page}'
        exe.submit(main, url)
    exe.shutdown()
    time_2 = time.time()
    use_time = int(time_2) - int(time_1)
    print(f'总计耗时:{use_time}秒')