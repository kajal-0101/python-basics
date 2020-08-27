'''
Name of the person who is getting maximum salary.
'''

import numpy as np
import pandas as pd

df = pd.read_csv("salary_dataset.csv")
name = df['Name'].tolist()
yearExp = df['YearsExperience'].tolist()
salary = df['Salary'].tolist()

res = {name[i]: salary[i] for i in range(0, len(name))}
name_max_ex = max(res, key = res.get)
print("The person having maximum years of experience: ", name_max_ex)
