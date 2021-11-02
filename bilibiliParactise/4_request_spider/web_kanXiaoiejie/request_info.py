
import requests
import parsel
import re
import os

def request_test():
    page_html = requests.get('https://www.kanxiaojiejie.com/page/1').text

    print(page_html)

def request_spider_pic():
    page_html = requests.get('https://www.kanxiaojiejie.com/page/1').text
    pages = parsel.Selector(page_html).css('.last::attr(href)').get().split('/')[-1]
    for page in range(1, int(pages) + 1):
        print(f'==================正在爬取第{page}页==================')
        response = requests.get(f'https://www.kanxiaojiejie.com/page/{page}')
        data_html = response.text
        # 提取详情页
        zip_data = re.findall('<a href="(.*?)" target="_blank"rel="bookmark">(.*?)</a>', data_html)
        for url, title in zip_data:
            print(f'----------------正在爬取{title}----------------')
            if not os.path.exists('img/' + title):
                os.mkdir('img/' + title)
            resp = requests.get(url)
            url_data = resp.text
            selector = parsel.Selector(url_data)
            img_list = selector.css('p>img::attr(src)').getall()

            for img in img_list:
                img_data = requests.get(img).content
                img_name = img.split('/')[-1]
                with open(f"img/{title}/{img_name}", mode='wb') as f:
                    f.write(img_data)
                print(img_name, '爬取成功！！！')
            print(title, '爬取成功！！！')

def requests_spider():
    # 这个报错
    page_html = requests.get('https://meinv.woaikanmeinv.xyz/P/3851').text
    pages = parsel.Selector(page_html).css('.last::attr(href)').get().split('/')[-1]
    for page in range(1, int(pages) + 1):
        print(f'==================正在爬取第{page}页==================')
        response = requests.get(f'https://meinv.woaikanmeinv.xyz/P/{page}')
        data_html = response.text
        # 提取详情页
        zip_data = re.findall('<a href="(.*?)" target="_blank"rel="bookmark">(.*?)</a>', data_html)
        for url, title in zip_data:
            print(f'----------------正在爬取{title}----------------')
            if not os.path.exists('img/' + title):
                os.mkdir('img/' + title)
            resp = requests.get(url)
            url_data = resp.text
            selector = parsel.Selector(url_data)
            img_list = selector.css('p>img::attr(src)').getall()

            for img in img_list:
                img_data = requests.get(img).content
                img_name = img.split('/')[-1]
                with open(f"img/{title}/{img_name}", mode='wb') as f:
                    f.write(img_data)
                print(img_name, '爬取成功！！！')
            print(title, '爬取成功！！！')

def main():
    # request_test()
    request_spider_pic()
    # requests_spider()

if __name__ == '__main__':
    main()