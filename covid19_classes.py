#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 09:18:57 2022

@author: anne
"""

import os
import datetime
import matplotlib.pyplot as plt
from tensorflow.keras import Input,Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import mean_absolute_error,accuracy_score

#%%
CSV_PATH_TRAIN = os.path.join(os.getcwd(),'Dataset','Covid19_train.csv')
CSV_PATH_TEST = os.path.join(os.getcwd(),'Dataset','Covid19_test.csv')
MMS_PATH = os.path.join(os.getcwd(),'models', 'mms.pkl')
MODEL_PATH = os.path.join(os.getcwd(),'models', 'model.h5')
LOGS_PATH = os.path.join(os.getcwd(),'logs',datetime.datetime.now().
                         strftime('%Y%m%d-%H%M%S'))

#%%
        
class ModelDevelopment:
    def lstm_model(self,input_shape,nb_class,nodes=64,dropout=0.3):
        model = Sequential()
        model.add(Input(shape=(input_shape))) #LSTM,RNN, GRU only accepts 3D array
        model.add(LSTM(nodes,return_sequences=(True)))
        model.add(Dropout(dropout))
        model.add(LSTM(nodes,return_sequences=(True)))
        model.add(Dropout(dropout))
        model.add(LSTM(nodes))
        model.add(Dropout(dropout))
        model.add(Dense(1,activation='relu'))
        model.summary()
        return model

class ModelEvaluation():
    
    def cr(self, y_true, y_pred):
        print(classification_report(y_true, y_pred))
        print(confusion_matrix(y_true, y_pred))
        print(accuracy_score(y_true, y_pred))


    def plot_hist_graph(self,hist):
        plt.figure()
        plt.plot(hist.history['mse'])
        plt.plot(hist.history['val_mse'])
        plt.xlabel('epoch')
        plt.legend(['Training MSE','Validation MSE'])
        plt.show()

    def model_graph(self,y,x):
        plt.figure()
        plt.plot(y,color='red')
        plt.plot(x,color='blue')
        plt.xlabel('Day')
        plt.ylabel('Covid19 Cases')
        plt.legend(['Actual','Predicted'])
        plt.show()

class Performance():
        
    def mape(self, y_true, y_pred):
        print(f"MAPE prediction is: {(mean_absolute_error(y_true, y_pred)/sum(abs(y_true))) * 100}%")


