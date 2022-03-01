
# 注意大小写
from MyQR import myqr

if __name__ == '__main__':
    # 如果为网站则会自动跳转，文本直接显示，不支持中文
    myqr.run(
        # words='http://www.baidu.com',  # 包含信息
        words='https://mp.weixin.qq.com/s?__biz=MjM5NDIzMTk1Nw==&tempkey=MTE0Nl9hdGNMVVN5OXNDWkMrTjN5T0tfN05VeVg5UEo1RUxHbTJxVVhadmpyb0FCcy15OC1IY212ZDBIYnZ1TEQ3WUFxNEpicGgtd2JDQ0haNG9DMGZ6TkhVR2pFTC12MWZVeE1JQTFBVlJrdFpEMGxENmVaLUxCaTBCZEV1SzRXWTRFN1dVTHJmdkp1STdKODcweXRjeHRKWmw1TVNSdFlYckFQNkdReFl3fn4%3D&chksm=3123a46306542d7508562d18db0d60ab324e8a66b8ce4a62ec51c587b679810e7974578134f2&scene=0&xtrack=1&previewkey=V%252BBC%252BPbvUlqJDjKwnYf%252BaMNS9bJajjJKzz%252F0By7ITJA%253D&clicktime=1640924072#wechat_redirect',  # 包含信息
        # picture='we.jpg',  # 背景图片
        colorized=True,  # 是否有颜色，如果为False则为黑白
        save_name='c.png'  # 输出文件名
    )