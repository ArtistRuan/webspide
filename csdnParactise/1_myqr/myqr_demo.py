
# 注意大小写
from MyQR import myqr

if __name__ == '__main__':
    # 如果为网站则会自动跳转，文本直接显示，不支持中文
    myqr.run(
        words='http://www.baidu.com',  # 包含信息
        picture='we.jpg',  # 背景图片
        colorized=True,  # 是否有颜色，如果为False则为黑白
        save_name='wecode.png'  # 输出文件名
    )