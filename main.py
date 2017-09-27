import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 指定中文字体
fontset = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

year = [1, 2, 3, 4, 5, 6]
num1 = [920, 3400, 9800, 7022, 1009, 11911]
num2 = [673, 8711, 5400, 8000, 2678, 7777]


# 点状图
def scatter_plot():
    plt.scatter(year, num1)
    plt.title('点状图', fontproperties=fontset)  # 图形名称
    plt.xlabel('年份', fontproperties=fontset)  # X轴名称
    plt.ylabel('数量', fontproperties=fontset)  # Y轴名称
    plt.show()
    plt.close()


# 线图
def line_plot():
    # 线条标签、线型、颜色、符号、粗细
    plt.plot(year, num1, label='CH', linestyle='--', color='lightpink', marker='x', linewidth=2)
    # 透明度
    plt.plot(year, num2, label='US', linestyle='-', color='b', marker='v', linewidth=4, alpha=0.4)
    plt.grid(True)  # 网格
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
    # scatter_plot()
    line_plot()
    # histogram_plot()
    # tick_plot()
