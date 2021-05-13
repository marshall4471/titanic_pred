# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/181qvB66-DMvoz9JzH3YreXujoHAq4WjD
"""

import pandas as pd

df1 = pd.read_csv('/content/train.csv')

df2 = pd.read_csv('/content/test.csv')

df1.head()

df2.head()

import numpy as np

df1.dropna(inplace = True)

from sklearn.preprocessing import LabelEncoder

le =  LabelEncoder()
for i in df1:
    if df1[i].dtype=='object':
        df1[i] = le.fit_transform(df1[i])
    else:
        continue

df1



X = df1.drop(['Survived', 'PassengerId', 'Name', 'Ticket'],axis=1)
y = df1['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import f1_score

model = AdaBoostClassifier()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(y_pred[:65])

from sklearn.metrics import  recall_score, accuracy_score, classification_report





accuracy = accuracy_score(y_pred, y_test)





print(accuracy)

print(classification_report(y_test,y_pred))
print('F1 Score: ',f1_score(y_test,y_pred))

df2



test_df = pd.read_csv('/content/test.csv')

test_df = test_df.drop(columns=['Name', 'Ticket', 'Cabin'])

li =  LabelEncoder()
for i in test_df:
    if test_df[i].dtype=='object':
       test_df[i] = li.fit_transform(test_df[i].astype(str))
    else:
        continue

sc.fit_transform(test_df)

test_df.fillna(0, inplace=True)

prediction = model.predict(test_df)

print(prediction)

submission = pd.read_csv('/content/submission.csv')
submission_df = pd.DataFrame({"PassengerId": test_df["PassengerId"],
                'Survived': prediction.astype(int)})
submission_df.tail()

submission_df.to_csv('submission9.csv', index=False)