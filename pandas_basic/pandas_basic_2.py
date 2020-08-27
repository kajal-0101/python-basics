'''
Name of the person who is getting salary close to average.
'''

import numpy as np
import pandas as pd

df = pd.read_csv("salary_dataset.csv")
name = df['Name'].tolist()
yearExp = df['YearsExperience'].tolist()
salary = df['Salary'].tolist()

avg_salary = np.mean(salary)
print("The average salary of the employee is ", avg_salary)
avg_diff = []
for i in range(0, len(salary)):
    avg_diff.append(abs(salary[i] - avg_salary))
avg_sal_dict = {name[i]:avg_diff[i] for i in range(0, len(name))}
avg_name = min(avg_sal_dict, key = avg_sal_dict.get)
name_sal = avg_sal_dict.get(avg_name, "")
print("The person having salary close to the average salary is ", avg_name)
print("His salary is ", (name_sal+avg_salary))
