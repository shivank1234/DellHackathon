# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:05:01 2019

@author: HP
"""

from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
def predict_warranty(test_list):


    df = pd.read_csv('delldata_final.csv')
    test_frame = pd.read_csv('testcases.csv')

    df2 = df.iloc[:, 0:6]

    matrix_X = []
    for index, rows in df2.iterrows():
        row = list(rows)
        matrix_X.append(row)
    matrix_X
    y_train = df['Warranty Recommended']
    list(y_train)
    y_train = np.array(y_train)

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(matrix_X, y_train)
    predicted_value = neigh.predict([test_list])
    return predicted_value
