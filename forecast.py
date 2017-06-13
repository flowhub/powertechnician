
# coding: utf-8

# In[1]:

import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

loaded_model = pickle.load(open('lm_model', 'rb'))

def predict_consumption (wdsp,temp,rhum,date_day_code,hour):
    #print (wdsp,temp,rhum,date_day_code)
    input_list = [wdsp,temp,rhum,date_day_code]
    y_pred = loaded_model.predict(input_list)
    return y_pred[0]

# In[ ]:



