'''
Lineplot between YearsExper and Salary
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("salary_dataset.csv")

yearExp = df['YearsExperience'].tolist()
salary = df['Salary'].tolist()

plt.plot(yearExp, salary, label = "Salary vs Years of Experience", 
         color = 'b', marker='o', markerfacecolor = 'k', linestyle = '--', linewidth = 3)

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend(bbox_to_anchor=(1.5,1))
plt.title('Salary according to years of experience')
plt.xticks([2, 4, 6, 8, 10, 12])
plt.yticks([20000, 40000, 60000, 80000, 100000, 120000, 140000])
plt.savefig('lineplot.png')
