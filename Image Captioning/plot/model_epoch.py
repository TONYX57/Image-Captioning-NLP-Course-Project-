import random


import numpy as np
import matplotlib.pyplot as plt

colors = ['#1f77b4']
labels = ['VGG','ResNet101','ResNet50','Wide-ResNet50','Wide-ResNet101']
data=[5,10,5,8,7]

fig, ax = plt.subplots(figsize=(7,5))
bars1=plt.bar(np.arange(0,10,2), data, align='center', alpha=0.7, color=colors, tick_label=labels)
plt.ylabel('#Training epochs (best BLEU-4 score)')
plt.xlabel("Image models")
ax.get_xticklabels()[2].set_color("red")
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
#控制y轴的刻度
plt.yticks(np.arange(0,12,1))

#展示结果
plt.show()
