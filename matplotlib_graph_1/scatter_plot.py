'''
Draw scatterplot between Reg.No and average of all assignments.
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mp.csv")
regNo = df['reg_no'].tolist()
regNo = list(map(str, regNo))
total = df['total'].tolist()
avg = []
for i in range(0, len(total)):
    avg.append(total[i]/3)
plt.scatter(regNo, avg, label = 'Average marks')
plt.xlabel('Register No')
plt.ylabel('Average marks')
plt.title('Scatter plot of Average Marks')
plt.legend(bbox_to_anchor=(1.35,1))
plt.xticks(regNo, rotation=90)
plt.yticks([0, 20, 40, 60, 80, 100])
plt.grid(True, linewidth=1, linestyle="--")
plt.savefig('scatter.png')
