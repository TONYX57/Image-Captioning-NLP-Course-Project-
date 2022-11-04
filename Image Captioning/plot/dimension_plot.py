#Group Bar chart

import random
import numpy as np
import matplotlib.pyplot as plt
#生成信息
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', 'r', 'b']
labels = ['256 / 256','256 / 512','256 / 1024','512 / 256','512 / 512','512 / 1024','1024 / 256','1024 / 512','1024 / 1024']
data1 = [15.82, 16.60, 16.33, 15.97, 16.22, 16.00, 15.51,16.34,16.61]
data2 = [21.66,  21.79, 22.04, 21.53,22.25,21.57,21.20,22.90,22.18]
width = 0.7
xpos = np.arange(0,18,2)

#生成柱状图
fig, ax = plt.subplots(figsize=(15,8))
bars1 = plt.bar(xpos-width/2, data1, align='center', width=width, alpha=0.9, color='#1f77b4', label = 'Training')
bars2 = plt.bar(xpos+width/2, data2, align='center', width=width, alpha=0.9, color='#ff7f0e', label = 'Evaluation')
plt.xlabel("Attention layer dimensions / Decoder layer dimensions")
plt.ylabel("BLEU-4 scores")
ax.get_xticklabels()[-3].set_color("red")
plt.yticks(np.arange(0,30,2))

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
