
from wordcloud import WordCloud

if __name__ == '__main__':
    wc = WordCloud()  # 创建词云对象
    wc.generate('Do not go gentle into that good night')  # 生成词云
    wc.to_file('wc.png')  # 保存词云

