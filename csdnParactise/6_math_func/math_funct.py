
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    x = np.arange(0, 11)  # x轴数据
    # y = x * x + 5  # 函数关系
    y = x * x # 函数关系
    # plt.title("y=x*x+5")  # 图像标题
    plt.title("y=x*x")  # 图像标题
    plt.xlabel("x")  # x轴标签
    plt.ylabel("y")  # y轴标签
    plt.plot(x, y)  # 生成图像
    plt.show()  # 显示图像