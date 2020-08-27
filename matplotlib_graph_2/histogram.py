'''
Histogram for YearExpr and Salary
'''

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("salary_dataset.csv")

yearExp = df['YearsExperience'].tolist()
salary = df['Salary'].tolist()
plt.hist(yearExp, color='b')
plt.grid(axis='y', alpha = 0.75)
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
plt.savefig('yearExp-hist.png')  

plt.hist(salary, color='r')
plt.grid(axis='y', alpha = 0.75)
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.savefig('salary-hist.png')
