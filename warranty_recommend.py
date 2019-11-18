# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:05:01 2019

@author: HP
"""

def predict_warranty(test_list):
    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set()
    
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

    from sklearn.neighbors import KNeighborsClassifier
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(matrix_X, y_train)
    predicted_value = neigh.predict([test_list])
    return predicted_value

predict_warranty([1,1,0,0,0,0])