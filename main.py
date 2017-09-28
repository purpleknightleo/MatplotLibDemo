import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定中文字体
fontset = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

year = [1998, 1999, 2001, 2004, 2005, 2008]
num1 = [920, 3400, 9800, 7022, 1009, 11911]
num2 = [773, 8711, 5400, 8000, 2678, 7777]
num3 = [873, 6666, 4444, 5555, 1111, 17001]
num4 = [1000, 4321, 7888, 6969, 3209, 8888]


# 点状图
def scatter_plot(save):
    plt.scatter(year, num1)
    plt.title('点状图', fontproperties=fontset)  # 图形名称
    plt.xlabel('年份', fontproperties=fontset)  # X轴名称
    plt.ylabel('数量', fontproperties=fontset)  # Y轴名称
    # 通过箭头进行内容标注，xy为被标注的位置，xytext为标注文字的位置点
    plt.annotate('local max', xy=(2008, 11911), xytext=(2005, 10000),
                 arrowprops=dict(facecolor='black', shrink=0.05), )
    fig = plt.gcf()  # 获取当前图表，不然plt.show()就会生成新的图表导致savefig()时一片空白
    plt.show()

    if save:
        fig.savefig('output/scatter_plot_demo.jpg')  # 保存图表
    plt.close()


# 线图（两条线在同一张图中）
def line_plot_in_one():
    # 线条标签、线型、颜色、符号、粗细
    plt.plot(year, num1, label='CH', linestyle='--', color='lightpink', marker='x', linewidth=2)
    # 透明度
    plt.plot(year, num2, label='US', linestyle='-', color='b', marker='v', linewidth=4, alpha=0.4)

    # plt.xlim(1995, 2010)  # x轴的刻度区间
    # plt.ylim(800, 12000)  # y轴的刻度区间
    plt.axis((1995, 2010, 800, 12000))  # 与上面两句话等价

    plt.grid(True)  # 网格
    plt.show()
    plt.close()


# 线图（两条线在同两张图中，手动控制位置）
def line_plot_in_two_with_axes():
    # 定义坐标轴相关位置关系和宽度/长度
    plt.axes([0.08, 0.05, 0.415, 0.9])
    plt.plot(year, num1, color='red')

    # 定义坐标轴相关位置关系和宽度/长度
    plt.axes([0.575, 0.05, 0.415, 0.9])
    plt.plot(year, num2, color='green')

    plt.show()
    plt.close()


# 线图（N条线分别在N张图中，自动控制位置，子图为对称分割）
def line_plot_with_subplot_symmetric():
    # 定义2*2子图，当前活动子图为1
    plt.subplot(2, 2, 1)  # 也可以写成plt.subplot(221)
    plt.plot(year, num1, color='red')

    # 切换当前活动子图为2
    plt.subplot(222)
    plt.plot(year, num2, color='green')

    # 切换当前活动子图为3
    plt.subplot(223)
    plt.plot(year, num2, color='black')

    # 切换当前活动子图为4
    plt.subplot(224)
    plt.plot(year, num2, color='yellow')

    plt.tight_layout()  # 自动调整间距
    plt.show()
    plt.close()


# 线图（N条线分别在N张图中，自动控制位置，子图为非对称分割）
def line_plot_with_subplot_asymmetric():
    # 定义2*2子图，当前活动子图为1
    plt.subplot(2, 2, 1)  # 也可以写成plt.subplot(221)
    plt.plot(year, num1, color='red')

    # 切换当前活动子图为2
    plt.subplot(222)
    plt.plot(year, num2, color='green')

    # 重新定义2*1子图，切换当前活动子图为2
    plt.subplot(212)
    plt.plot(year, num2, color='black')

    plt.tight_layout()  # 自动调整间距
    plt.show()
    plt.close()


# 直方图
def histogram_plot():
    plt.hist(num1, bins=20)
    plt.show()
    plt.close()


# 坐标刻度
def tick_plot():
    plt.scatter(year, num1)
    tick_val = [1000, 10000, 100000]
    tick_lab = ['1k', '10k', '100k']
    plt.yticks(tick_val, tick_lab)
    plt.show()
    plt.close()


if __name__ == '__main__':
    scatter_plot(True)
    # line_plot_in_one()
    # line_plot_in_two()
    # line_plot_with_subplot_symmetric()
    # line_plot_with_subplot_asymmetric()
    # histogram_plot()
    # tick_plot()
