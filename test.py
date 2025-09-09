# import pandas as pd
# import matplotlib.pyplot as plt

# # создадим временной ряд (например, количество пассажиров по годам)
# # сгенерируем случайные даты посадки (условные)
# import numpy as np
# import seaborn as sns 

# titanic_df = pd.read_csv("resources/titanic.csv")



# students_performance = pd.read_csv('resources/StudentsPerformance.csv')

# sns.lmplot(x='math score', y='reading score', data=students_performance)
# plt.savefig("math_vs_reading.png")

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/dataset_209770_6.txt', sep=" ")


plt.scatter(df.iloc[:, 0], df.iloc[:, 1], alpha=0.6)
plt.xlabel(df.columns[0])
plt.ylabel(df.columns[1])
plt.title("Распределение точек по 2 признакам")
plt.show()
