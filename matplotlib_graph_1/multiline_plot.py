'''
Draw multiline plot between Reg.No and all assignment marks with following styles.
• Assignment 0 marks – Red Dotted
• Assignment 1 marks – Green Dashed dot
• Assignment 2 marks – Blue Solid
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mp.csv")
regNo = df['reg_no'].tolist()
regNo = list(map(str, regNo))
week0 = df['week_0'].tolist()
week1 = df['week_1'].tolist()
week2 = df['week_2'].tolist()
total = df['total'].tolist()
fig = plt.figure()
plt.plot(regNo, week0, label = 'Week 0 Marks', marker='o', linestyle='dotted', color='r', linewidth=2)
plt.plot(regNo, week1, label = 'Week 1 Marks', marker='o', linestyle='dashdot', color='g', linewidth=2)
plt.plot(regNo, week2, label = 'Week 2 Marks', marker='o', linestyle='solid', color = 'b', linewidth=2)

plt.xlabel('Register No.')
plt.ylabel('Marks')
plt.legend(bbox_to_anchor=(1.05, 1))
plt.xticks(regNo, rotation=90)
plt.yticks([0, 20, 40, 60, 80, 100])
plt.title('Weekly Marks')
plt.savefig('multiline.png')
