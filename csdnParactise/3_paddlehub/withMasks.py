
import paddlehub as hub
# import paddle


if __name__ == '__main__':
    '''
    识别是否带了口罩
    '''

    # 加载模型
    module = hub.Module(name='pyramidbox_lite_mobile_mask')
    # 图片列表
    image_list = ['G:\desktop\pythonProject\csdnParactise\1_myqr\we.jpg']
    # 获取图片字典
    input_dict = {'image': image_list}
    # 检测是否带了口罩
    module.face_detection(data=input_dict)