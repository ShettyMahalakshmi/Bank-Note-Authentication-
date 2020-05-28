# -*- coding: utf-8 -*-
"""
Created on Thu May 28 12:50:36 2020

@author: Mahalakshmi

"""
import numpy as np
import pandas as pd


df = pd.read_csv("BankNote_Authentication.csv")
df.head()
 
x = df.iloc[:,:-1]
y = df.iloc[:,-1]

y.head()

from sklearn.model_selection  import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
 from sklearn.ensemble import RandomForestClassifier
 Classifier = RandomForestClassifier()
 Classifier.fit(x_train, y_train)
 
 y_pred= Classifier.predict(x_test)
 
 from sklearn.metrics import accuracy_score
 score=accuracy_score(y_test, y_pred)
 
 import pickle
 pickle_out = open("Classifier.pkl" , "wb")
 pickle.dump(Classifier, pickle_out)
 pickle_out.close()