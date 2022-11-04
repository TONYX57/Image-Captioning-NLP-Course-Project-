import random


import numpy as np
import matplotlib.pyplot as plt

colors = ['#1f77b4']
labels = [1,2,3,4,5,6]
data = [19.81, 21.64, 22.90, 21.76, 21.95, 21.90]

fig, ax = plt.subplots(figsize=(8,5))
bars1=plt.bar(np.arange(0,12,2), data, align='center', alpha=0.7, color=colors, tick_label=labels)
plt.ylabel('Evaluation BLEU-4 scores')
plt.xlabel("Beam sizes")
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
plt.yticks(np.arange(0,28,2))

#展示结果
plt.show()
