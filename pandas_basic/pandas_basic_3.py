'''
Who is having less experience.
'''

import numpy as np
import pandas as pd

df = pd.read_csv("salary_dataset.csv")
name = df['Name'].tolist()
yearExp = df['YearsExperience'].tolist()
salary = df['Salary'].tolist()

res = {name[i] : yearExp[i] for i in range(0, len(name))}
name_min_exp = min(res, key = res.get)
print("The person having the minimum years of experience is ", name_min_exp)
