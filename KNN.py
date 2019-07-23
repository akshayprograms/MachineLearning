# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:02:14 2019

@author: admin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

A=pd.read_csv("C:/Users/admin/Desktop/Python Programs/iris.csv")

A=A.drop(A.columns[[0]],axis=1)

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
B=A.apply(le.fit_transform)

#X = B.iloc[:,:-9]
#Y = B.iloc[:,-1]

X=B[B.columns[~B.columns.isin(['Species'])]]

Y=B['Species']


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.40,random_state=20) 

from sklearn.preprocessing import StandardScaler 
scaler = StandardScaler() 
scaler.fit(X_train) 
X_train = scaler.transform(X_train) 
X_test = scaler.transform(X_test) 

from sklearn.neighbors import KNeighborsClassifier 
model = KNeighborsClassifier(n_neighbors=5) 
model.fit(X_train, Y_train) 
predicted = model.predict(X_test)
#X_test['predicted'] = predicted
#X_test['Actual'] = Y_test
cm = confusion_matrix(Y_test, predicted)
#classification_report(Y_test, predicted)
#All Accuracy metrics for Classification
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
print("F1 score",f1_score(Y_test,predicted, average="macro"))
print("Precision",precision_score(Y_test,predicted, average="macro"))
print("Recall",recall_score(Y_test,predicted, average="macro"))
print ("Accuracy : ",accuracy_score(Y_test,predicted)*100)
dir(model)