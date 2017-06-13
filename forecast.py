
# coding: utf-8

# In[237]:

import pandas as pd
import seaborn as sns


# In[238]:

get_ipython().magic('matplotlib inline')


# In[239]:

df_new=pd.read_csv(r'C:\Users\Gershon Celniker\Desktop\ipython_notebooks\GE_hackathon\minds-machines-europe-master\Electrification Challenge\Grid Timeseries Dataset\LoadForecasting\WeatherData\hly1043_clean_from_2016.csv')


# In[240]:

df_new.describe()


# In[241]:

df_new.head(2)


# In[242]:

df=df_new


# In[243]:

df['temp'].hist()


# In[12]:

df['temp'].describe()


# In[13]:

df['temp'].hist(bins=30)


# In[14]:

df['wdsp'].hist()


# In[17]:

df['rhum'].hist()


# ## Now the electricity consumption

# In[244]:

df_elec=pd.read_csv(r'C:\Users\Gershon Celniker\Desktop\ipython_notebooks\GE_hackathon\minds-machines-europe-master\Electrification Challenge\Grid Timeseries Dataset\LoadForecasting\LoadData\ge_from_2016.csv')    


# In[245]:

df_elec.count()


# In[246]:

df.count()


# In[21]:

df.columns


# In[22]:

df_elec.columns


# In[23]:

df_elec.head()


# In[24]:

df.head()


# In[25]:

df_elec['Residential'].hist()


# In[26]:

df_elec['Mixed'].hist()


# In[247]:

df_elec.rename(columns={'Period': 'date' }, inplace=True)


# In[248]:

df_elec.rename(columns={'date': 'date_all' }, inplace=True)


# In[249]:

df.rename(columns={'date': 'date_all' }, inplace=True)


# In[250]:

df.head(1)


# In[251]:

df['date_all']  = pd.to_datetime(df['date_all'])  
df_elec['date_all'] = pd.to_datetime(df_elec['date_all'])  
df_daily=df.groupby(df['date_all']).mean()
df_elec_daily=df_elec.groupby(df_elec['date_all']).mean()


# In[253]:

df_elec.head(1)


# In[254]:

df.head(1)


# In[257]:

print (df_daily.count(), df_elec_daily.count())


# In[258]:

df_daily['date_all']=df_daily.index
df_elec_daily['date_all']=df_elec_daily.index


# #df_merged2=pd.merge(df, df_elec, on='date_all',how='inner')

# In[259]:

df_merged2=pd.merge(df_daily, df_elec_daily, on='date_all',how='inner')


# In[261]:

df_merged2.head(5)


# In[262]:

df_merged2.temp.count()


# In[265]:

df_merged2['Total_consumption']=df_merged2['Mixed']+df_merged2['Commercial']+df_merged2['Residential']


# In[266]:

df_merged2.head(5)


# In[268]:

df_merged=df_merged2


# In[272]:

df_merged['Total_consumption_int']=df_merged['Total_consumption'].astype(int)


# In[279]:

sns.jointplot("temp", "Total_consumption", data=df_merged, kind="reg")


# In[135]:

df_merged['temp_new']=df_merged['temp'].astype(int)


# In[136]:

df_merged['rhum_new']=df_merged['rhum'].astype(int)


# In[137]:

df_merged['mixed_new']=df_merged['Mixed'].astype(int)


# In[138]:

df_merged['wdsp_new']=df_merged['wdsp'].astype(int)


# In[551]:

sns.jointplot("temp_new", "mixed_new", data=df_merged2, kind="reg")


# In[209]:

sns.jointplot("temp_new", "rhum", data=df_merged, kind="reg")


# In[216]:

sns.jointplot("Mixed", "Commercial", data=df_merged, kind="reg")


# In[142]:

sns.jointplot("wdsp_new", "mixed_new", data=df_merged, kind="reg")


# In[286]:

#df_merged['date_all'][1].weekday()
df_merged['date_day']=df_merged['date_all'].dt.weekday_name
df_merged['date_day_code']=df_merged['date_all'].dt.weekday.astype(int)


# In[305]:

g = sns.pairplot(df_merged[["date_day_code", "Total_consumption_int", "temp", "wdsp"]],  diag_kind="hist")
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)


# In[288]:

sns.jointplot("date_day_code", "Total_consumption_int", data=df_merged, kind="reg")


# In[143]:

df_merged['data_str']=df_merged['date_all'].astype(str)


# In[154]:

df_merged['data_str'].weekday()


# In[174]:

df_merged['Mixed'][1:30].plot()         # ^^^
plt.xticks(df_merged.index[1:30]) # change the x tick labels


# In[168]:

#df = df.sort_values('date', ascending=True)
plt.plot(df_merged['date_all'][1:30], df_merged['Residential'][1:30])
plt.xticks(rotation='vertical')


# In[150]:

"""
import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# build the figure
fig, ax = plt.subplots()
#sns.tsplot(df_merged[1:7], time='date_all', value='Mixed', unit='Unit', ax=ax)
sns.tsplot(df_merged[1:7], time='date_all', value='Mixed', ax=ax)


# assign locator and formatter for the xaxis ticks.
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y.%m.%d'))

# put the labels at 45deg since they tend to be too long
fig.autofmt_xdate()
plt.show()


# In[221]:

# Read in the data from the stackoverflow question
"""
df = pd.read_clipboard().iloc[1:]

# Convert it to "long-form" or "tidy" representation
df = pd.melt(df, id_vars=["date"], var_name="condition")

# Plot the average value by condition and date
ax = df.groupby(["condition", "date"]).mean().unstack("condition").plot()

# Get a reference to the x-points corresponding to the dates and the the colors
x = np.arange(len(df.date.unique()))
palette = sns.color_palette()

# Calculate the 25th and 75th percentiles of the data
# and plot a translucent band between them
for cond, cond_df in df.groupby("condition"):
    low = cond_df.groupby("date").value.apply(np.percentile, 25)
    high = cond_df.groupby("date").value.apply(np.percentile, 75)
    ax.fill_between(x, low, high, alpha=.2, color=palette.pop(0))


# In[489]:

sns.factorplot(data=df_merged[1:300], x="date_all", y="Residential",size=5, aspect=3)


# In[393]:

sns.factorplot(data=df_merged[1:30], x="date_all", y="Mixed",size=5, aspect=3)


# In[392]:

sns.factorplot(data=df_merged[1:30], x="date_all", y="Commercial",size=5, aspect=3)


# In[303]:

df_merged.columns


# In[312]:

import statsmodels.formula.api as sm

result = sm.ols(formula="Total_consumption ~ temp + wdsp + rhum+date_day_code ", data=df_merged).fit()
print (result.params)


# In[313]:

print (result.summary())


# In[230]:

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#sales = pd.read_csv("home_data.csv")
train_data, test_data = train_test_split(df_merged,train_size=0.8)

# Train the model
X = train_data[['wdsp','temp','rhum']]
y = train_data.Mixed
lm = LinearRegression()
lm.fit(X, y)

# Predict on the test data
X_test = test_data[['wdsp','temp','rhum']]
y_test = test_data.Mixed
y_pred = lm.predict(X_test)

# Compute the root-mean-square
rms = np.sqrt(mean_squared_error(y_test, y_pred))
print(rms)
# 260435.511036


# In[402]:

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#sales = pd.read_csv("home_data.csv")
train_data, test_data = train_test_split(df_merged,train_size=0.8)

# Train the model
X = train_data[['wdsp','temp','rhum']]
y = train_data.Commercial
lm = LinearRegression(n_jobs=5)
lm.fit(X, y)

# Predict on the test data
X_test = test_data[['wdsp','temp','rhum']]
y_test = test_data.Commercial
y_pred = lm.predict(X_test)

# Compute the root-mean-square
rms = np.sqrt(mean_squared_error(y_test, y_pred))
print(rms)
# 260435.511036


# In[403]:

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split

#sales = pd.read_csv("home_data.csv")
train_data, test_data = train_test_split(df_merged,train_size=0.8)

# Train the model
X = train_data[['wdsp','temp','rhum','date_day_code']]
y = train_data.Residential
lm = LinearRegression()
lm.fit(X, y)

# Predict on the test data
X_test = test_data[['wdsp','temp','rhum','date_day_code']]
y_test = test_data.Residential
y_pred = lm.predict(X_test)

# Compute the root-mean-square
rms = np.sqrt(mean_squared_error(y_test, y_pred))
print(rms)
# 260435.511036


# In[552]:

def predict_consumption (wdsp,temp,rhum,date_day_code,hour):
    #print (wdsp,temp,rhum,date_day_code)
    input_list = [wdsp,temp,rhum,date_day_code]
    y_pred = lm1.predict(input_list)
    return y_pred[0]

print (predict_consumption(5.541667,8.691667,78.666667,3,3))
    
    


# In[ ]:



