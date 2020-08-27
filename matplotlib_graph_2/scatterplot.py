'''
Scatterplot between name and AvgDifference of salary
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("salary_dataset.csv")

name = df['Name'].tolist()
salary = df['Salary'].tolist()
sal = np.mean(salary)
print("The average salary is ", sal)
avgDiff = []
for i in range(0, len(salary)):
    avgDiff.append(abs(salary[i] - sal))

plt.scatter(name, avgDiff, label = "Average Difference" , color = 'g')
plt.grid(axis = 'y', alpha = 0.75)
plt.legend(bbox_to_anchor=(1.05,1))
plt.xticks(name,rotation=90)
plt.xlabel('People')
plt.ylabel('Average salary difference')
plt.title('Average difference of peoples salary')
plt.savefig('avgdiff-scatter.png')
