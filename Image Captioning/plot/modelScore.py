#Group Bar chart

import random
import numpy as np
import matplotlib.pyplot as plt
#生成信息
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', 'r', 'b']
labels = ['VGG','ResNet101','ResNet50','Wide-ResNet50','Wide-ResNet101']
data1 = [15.00,16.17, 16.22, 15.75, 15.83]
data2 = [20.50,22.32,  22.25, 21.02, 21.19]
width = 0.7
xpos = np.arange(0,10,2)

#生成柱状图
fig, ax = plt.subplots(figsize=(10,8))
bars1 = plt.bar(xpos-width/2, data1, align='center', width=width, alpha=0.9, color='#1f77b4', label = 'Training')
bars2 = plt.bar(xpos+width/2, data2, align='center', width=width, alpha=0.9, color='#ff7f0e', label = 'Evaluation')
plt.xlabel("Image models")
plt.ylabel("BLEU-4 scores")
ax.get_xticklabels()[2].set_color("red")
plt.yticks(np.arange(0,30,5))

#设置每个柱子下面的记号
ax.set_xticks(xpos) #确定每个记号的位置
ax.set_xticklabels(labels)  #确定每个记号的内容

#给每个柱子上面添加标注
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
              xy=(rect.get_x() + rect.get_width() / 2, height),
              xytext=(0, 3),  # 3 points vertical offset
              textcoords="offset points",
              ha='center', va='bottom'
              )
autolabel(bars1)
autolabel(bars2)

#展示结果
plt.legend()
plt.show()
