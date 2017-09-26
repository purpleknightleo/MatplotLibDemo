import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定中文字体
fontset = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

year = [1, 2, 3, 4, 5, 6]
num = [92, 34, 98, 72, 109, 111]


# 点状图
def scatter_plot():
    plt.scatter(year, num)
    plt.title('点状图表', fontproperties=fontset)
    plt.xlabel('年份', fontproperties=fontset)
    plt.ylabel('数量', fontproperties=fontset)
    plt.show()


# 线图
def line_plot():
    plt.plot(year, num)
    plt.show()


# 直方图
def histogram_plot():
    plt.hist(num, bins=20)
    plt.show()


if __name__ == '__main__':
    # scatter_plot()
    # line_plot()
    histogram_plot()
