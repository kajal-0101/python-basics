'''
Lineplot between Name and YearsExper
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("salary_dataset.csv")

name = df['Name'].tolist()
salary = df['Salary'].tolist()
plt.plot(name, salary, label = "Peoples' Salary", color = 'm', marker = 'o',
         markerfacecolor = 'k', linestyle = '--', linewidth = 3)
plt.legend(bbox_to_anchor=(1.05,1))
plt.xlabel('People')
plt.ylabel('Salary')
plt.xticks(name, rotation=90)
plt.grid(axis = 'x', alpha = 0.75)
plt.title('Salary- line plot')
plt.savefig('lineplot-name.png')
