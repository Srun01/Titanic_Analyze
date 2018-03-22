import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = pd.read_csv("titanic-data.csv")


# data = data.dropna()
# print(data.head())


# print(data.groupby("Survived")["Age"].mean())
# male = data[data["Sex"] == "male"]
# male_survived = male[male["Survived"] == 1]
# print(len(male_survived) / len(male))
#
# female = data[data["Sex"] == "female"]
# female_survived = female[female["Survived"] == 1]
# print(len(female_survived) / len(female))
#
# plt.hist(data["Age"])
# plt.show()

#
#
# is_embarked_C = data[data["Embarked"] == "C"]
# c_and_female = is_embarked_C[is_embarked_C["Sex"] == "female"]
# age_above_15 = c_and_female[c_and_female["Age"] < 15]
#
# print(survive_rate(c_and_female))

# print(len(data[data["Survived"] == np.nan]))


# print(data.groupby("Pclass")["Survived"].mean())
#
# group_by_sur_emb = data.groupby(["Pclass", "Survived"]).size().unstack()
# print(group_by_sur_emb)
# group_by_sur_emb.plot(kind="bar")
# plt.show()


# sex_with_survived = data.groupby("Sex")["Survived"].mean()
#
# data.groupby(["Sex", "Survived"])["Survived"].count().unstack().plot(kind="bar")
# plt.show()

def is_family(row):
    return row["SibSp"] > 0 and row["Parch"] > 0


data["Family"] = data.apply(is_family, axis=1)

data.groupby("Family").size().plot(kind="bar")
plt.show()
