'''
Draw lineplot between Reg.No and their maximum mark from all assignments.
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mp.csv")
regNo = df['reg_no'].tolist()
regNo = list(map(str, regNo))
week0 = df['week_0'].tolist()
week1 = df['week_1'].tolist()
week2 = df['week_2'].tolist()
maximum = []
for i in range(0, len(regNo)):
    a = max(week0[i], week1[i], week2[i])
    maximum.append(a)
plt.plot(regNo, maximum, label = 'Maximum marks', color='b', marker='o', linestyle='--', linewidth = 3)
plt.xlabel('Register No')
plt.ylabel('Maximum Marks')
plt.xticks(regNo, rotation=90)
plt.yticks([0, 20, 40, 60, 80, 100])
plt.legend(bbox_to_anchor=(1.05,1))
plt.title("Maximum marks - Python for Data Science")
plt.savefig('lineplot.png')
