## 企业级数据挖掘爬虫scrapy

### 安装scrapy

在cmd执行
~~~shell
pip install scrapy -i https://pypi.douban.com/simple
~~~

### 使用scrapy
##### 1 创建scrapy项目
~~~shell
# scrapy startproject （当前路径下）项目名
# 注意：项目的名字不允许使用数字开头、不能包含中文
scrapy startproject scrapy_spider
~~~

##### 2 创建爬虫文件
~~~shell script
# 要在spiders文件夹中创建爬虫文件
# cd 项目名\项目名\spiders
cd scrapy_spider\scrapy_spider\spiders
# 创建爬虫文件
# scrapy genspider 爬虫文件名 爬取网页（不加http协议）
scrapy genspider baidu www.baidu.com
~~~

##### 3 运行爬虫代码
```shell script
# scrapy crawl 爬虫文件名
scrapy crawl baidu
# 注意：如果将setting.py中的“ROBOTSTXT_OBEY = True”注释掉后，会将robot.txt不允许爬取的协议忽略掉
```

### scrapy项目结构
```text
项目名称
    项目名称
        spiders文件夹（存储爬虫文件）
            init
            自定义爬虫文件 核心功能文件
        init
        items   定义数据结构的地方，爬取的数据都包含哪些
        middleware  中间件 代理
        pipelines   管道  用来处理下载的数据
        settings    配置文件    robots协议 ua定义等

```

### response返回对象的属性和方法
```text
response.text   获取响应的字符串
response.body   获取的是二进制数据
response.xpath  直接使用xpath来解析response的内容
response.extract()  提取seletor对象的data属性值
response.extract_first() 提取seletor列表的第一个数据
```

