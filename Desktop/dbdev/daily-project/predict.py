import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


db = pd.read_csv("daily-project/covid_data.csv")
print (db.columns)


plt.xlabel('day')
plt.ylabel('cases')
plt.scatter(db.day, db.cases, color ='red', marker ='+')


reg = linear_model.LinearRegression()
reg.fit(db[['day']], db.cases)

print (int(reg.predict([[18]])))