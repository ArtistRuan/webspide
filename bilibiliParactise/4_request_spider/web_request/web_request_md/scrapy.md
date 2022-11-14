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

##### 3 写爬虫脚本
```shell script
# 3.1 start_urls最后的反斜线/需要去掉
# 3.2 在items.py中定义需要获取的数据，如src = Field()
# 3.3 xpath解析获取数据
src = response.xpath(//*[@id="component_59"]/li//img/@src).extract_first()
# 3.4 将获取到的数据交给管道pipelines
yeild src
# 3.5 在settings中开启管道，默认优先级是300，可根据需要调整
ITEM_PIPELINES = {
    'scrapy_dangdang.pipelines.ScrapyDangdangPipeline': 300,
}
# 3.6 在pipelinse.py中定义数据处理逻辑，包括保存、下载等操作
def open_spider(self,spider):
    self.fp = open('xxx','w',encoding='utf-8')
def process_item(self, item, spider):
    self.fp.write(str(item))

def close_spider(self,spider):
    self.fp.close()

# 3.7 多管道开启，模仿默认的管道，在settings.py中开启管道，并定义class类，自带def process_item(self, item, spider):..return
def process_item(self, item, spider):
    url = f'http:{item.get("src")}'
    filename = f'./books/{item.get("name")}.jpg'

    urllib.request.urlretrieve(url=url,filename=filename)
    return item
# 3.8 在settings.py中开启管道
ITEM_PIPELINES = {
   'scrapy_dangdang.pipelines.ScrapyDangdangPipeline': 300,
   'scrapy_dangdang.pipelines.DangDangDownloadPipeline': 301,
}

# 3.9 如需开启多页下载，则在逻辑中再次调用parse方法即可
if self.page < 100:
    # scrapy.Request就是scrapy的get请求
    # url就是请求地址
    # callback是要执行的函数parse，注意不要加()
    self.page = self.page + 1
    url = self.base_url + str(self.page) + 'xxx'
    yield scrapy.Request(url=url,callback=parse)
```

##### 4 运行爬虫代码
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
        pipelines   管道  用来处理下载的数据 默认是300优先级，值越小优先级越高（1-1000）
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

### scrapy shell
```shell script
# scrapy shell是一个交互终端，用于未启动spider时进行尝试和调试代码
# 测试xpath或css表达式，免去每次修改后运行spider的麻烦
# 安装ipython，可以智能补全和高亮输出等特性
pip install ipython

# 使用scrapy shell：scrapy shell url
scrapy shell http://category.dangdang.com

# response对象
response.body
response.text
response.url
response.status

# response解析
response.xpath() 
```

### 反爬懒加载
```shell script
# 对于获取到的数据，如果发现url都一样，那么基本判定为懒加载的原因
# 解决方式：将对应标签如li标签拉到最后一个，查看对应属性是否有类似data-original="..."，那么这个属性才是真正想要获取的
# 具体实例如下：
```
![](反爬懒加载正确数据获取.png)
```shell script
# 1 如上图：懒加载状态下，src为：images/model/guan/url_none.png
# 2 如下图：页面和标桩都拉到最后时，数据正式加载，src变成与data-orginal一样
# 3 真正src的属性是data-orginal
# 4 注意项：对于第一个标签数据，因为不含懒加载，没有data-original，所以还是src
```
![](懒加载验证识别.png)

### CrawlSpider基本概念和方法
```shell script
# 1.继承scrapy.Spider，可以定义规则，再解析html内容的时候，可以根据链接规则提取出指定的链接，然后再向这些链接发送请求
# 2.所以如果有需要跟进链接的需求，意思就是爬取了网页之后，需要提取链接再次爬取，使用CrawlSpider是非常合适的
# 3.提取链接，在这里就可以写规则提取指定链接
# 3.1 导包
from scrapy.linkextractors import LinkExtractor
# 3.2 正则表达式，提取符合正则的链接
scrapy.linkextractors.LinkExtractor(allow=())
# 3.3 提取符合xpath规则的链接
scrapy.linkextractors.LinkExtractor(restrict_xpath=())
# 3.4 提取符合选择器规则的链接
scrapy.linkextractors.LinkExtractor(retrict_css=())
# 3.5 正则表达式，不提取符合正则的链接（该方法不用，仅了解）
scrapy.linkextractors.LinkExtractor(deny=())
# 3.6 允许的域名（该方法不用，仅了解）
scrapy.linkextractors.LinkExtractor(allow_domains=())
# 3.7 不允许的域名（该方法不用，仅了解）
scrapy.linkextractors.LinkExtractor(deny_domains=())

# 比如1：
# 指定规则
link = LinkExtractor(allow=r'/book/1188_\d+\.html')
# 提取链接
link.extract_links(response)
# 比如2：
# 指定规则
link1 = LinkExtractor(restrict_xpaths=r'//div[@class="pages"]/a')
# 提取链接
link1.extract_links(response)
```

### CrawlSpider的使用
```shell script
# 1 创建项目：
scrapy startproject dushuwebsite
# 2 跳转到spider路径
cd \dushuprojct\dushuprojct\spiders
# 3 创建爬虫类，比之前多了-t crawl，表示用crawl默认模板
# 命令：scrapy genspider -t crawl 爬虫文件名 网站域名
scrapy genspider -t crawl readbooks www.dushu.com
# 4 执行等操作与上述scrapy一致
# 5 爬取到的数据需要入数据库，就要到setting中添加数据库的配置，如mysql配置：
DB_HOST = 'localhost'
# 端口号是一个整数
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_NAME = 'spider'
DB_CHARSET = 'utf-8'
# 6 在pipelines.py中定义处理数据入库的类
class MysqlPipeline:

    def open_spider(self,spider):

        settings = get_project_settings()
        self.host = settings["DB_HOST"]
        self.port = settings["DB_PORT"]
        self.user = settings["DB_USER"]
        self.password = settings["DB_PASSWORD"]
        self.name = settings["DB_NAME"]
        self.charset = settings["DB_CHARSET"]

        self.connect()

    # 为了使用清晰，connect()额外定义
    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            db=self.name,
            charset=self.charset
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        sql = 'insert into book(name,src) values ("{}","{}")'.format(item['name'],item['src'])
        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.conn.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
```
### 日志信息和日志等级 

##### 1 日志级别
- CRITICAL: 严重错误
- ERRO:     一般错误
- WARNING:  警告
- INFO:     一般信息
- DEBUG:    调试信息

默认的日志等级是DEBUG，只要出现了DEBUG或者DEBUG以上的日志，那么这些日志都会打印

##### 2 日志级别设置

在配置文件settings.py中，添加日志等级的配置

LOG_FILE:将屏幕显示的信息全部记录到文件中，屏幕不再显示，注意文件后缀一定是.log。一般建议

LOG_LEVEL:设置日志显示等级，显示哪些，不显示哪些。一般不建议
```python
LOG_LEVEL='WARNING'
LOG_FILE='logdemo.log'
```

### post请求的scrapy方法
```python
# 对于Post请求需要携带参数的，start_urls及默认的parse(self,response)无法处理
# 需要额外定义start_requests来处理请求
import scrapy
import json
def start_requests(self):
    # 起始url
    url = 'https://fanyi.baidu.com/sug'
    data = {'kw':'final'}
    yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)
def parse_second(self,response):
    content = response.text
    obj = json.loads(content,encoding='utf-8')
    print(obj)
```