'''
Create an array of employees and store emp id, basic salary, age and experience
details of each employee. Perform the following tasks:
i) Find the youngest employee
ii) Find the most experienced employee
iii) List the details of the employees on the basis of their salary
iv) Find the average salary of the employees whose age is between 30 to 40
'''

import numpy as np
emp = [[101, "A", 20000, 23, 2],
       [102, "B", 30000, 31, 7],
       [103, "C", 25000, 32, 8],
       [104, "D", 45000, 38, 11],
       [105, "E", 65000, 37, 6],
       [106, "F", 34000, 27, 4],]
print("The details of the employees are: ")
print(emp)
age = []
for i in range(0,len(emp)):
    temp=emp[i]
    age.append(temp[3])
print("\nThe age of the youngest employee is: ",np.min(age))
experience = []
for i in range(0, len(emp)):
    temp=emp[i]
    experience.append(temp[4])
print("\nThe maximum years of experience among these employees are: ",np.max(experience))
print("\nArranging the list of employees in ascending order according to their basic salary: ")
salary = []
for i in range(0, len(emp)):
    temp = emp[i]
    salary.append(temp[2])
salary = np.sort(salary)
for i in range (0, len(salary)):
    for j in range(0, len(emp)):
        temp = emp[j]
        if(salary[i] == temp[2]):
            print(emp[j])

sal = [] 
for i in range(0, len(emp)):
    temp=emp[i]
    if(temp[3]>=30 and temp[3]<=40):
        sal.append(temp[2])
print("\nThe average salary of all the employees within age range of 30 to 40 is ", np.mean(sal))
