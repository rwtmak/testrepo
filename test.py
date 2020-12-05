#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt


# # Import / Export Data

# In[ ]:


# IMPORT DATA (DIRECTION OF SLASHES MAKES A DIFF)
Data = read_csv('E:/FOLDER NAME/FILE.csv')


# In[ ]:


# EXPORT DATA
Title = "E:/Folder/Filename"
df.to_csv('%s.csv' % Title)


# # Understand Data

# In[ ]:


# SHOW FIRST FEW COLUMNS - put a number in the brackets to define number of rows.. if empty it shows 5
df.head()


# In[ ]:


# SHOW BOTTOM FEW COLUMNS
df.tail()


# In[ ]:


# UNDERSTAND DATA TYPE
df.info()


# In[ ]:


# DATA NUMBER OF COLUMNS / ROWS
df.shape


# In[ ]:


# DATA PROFILE
df.describe()


# In[ ]:


# VALUE COUNTS
df.value_counts()


# In[ ]:


# DATA UNIQUE FIELDS
df['column'].unique()
df['column'].nunique()


# # Data Transfomration

# In[ ]:


# MERGING DATA
df3 = df1.merge(df2, on='column', how='left')


# In[ ]:


# CONCAT DATAFRAMES
df3 = pd.concat([df1, df2])


# In[ ]:


# AGGREGATE DATA
df_agg = df.groupby(['Column1','Column2'], as_index=False).agg({'Column3':'nunique','Column4':'sum','Column5':'count'})


# In[ ]:


# AGGREGATE DATA - APPROACH 2
df_agg = df.groupby(['Column1', 'Column2'], as_index=False).agg({'Column3':['sum', 'count']})
df_agg.columns = df_agg.columns.map('_'.join)


# In[ ]:


# SORT
df.sort_values(by = 'SKU',ascending = False, inplace = True)


# In[ ]:


# DELETE COLUMN
df.drop(['COLUMN'], inplace = True)


# In[ ]:


# RENAME COLUMN
df.rename(columns={"OldName": "NewName"}, inplace=True)


# In[ ]:


# RESET INDEX
df.reset_index(drop=True, axis = 1, inplace = True)


# In[ ]:


# CONVERT TO DATETIME
df['Date_Columns'] = pd.to_datetime(df['Date_Columns'])


# In[ ]:


# CREATE DATETIME FEATURES
df['Year'] = df['ActivityDate'].dt.year
df['Month'] = df['ActivityDate'].dt.month
df['Week'] = df['ActivityDate'].dt.week
df['Day'] = df['ActivityDate'].dt.day
df['WeekDay'] = df['ActivityDate'].dt.weekday
df['YearWeek'] = df['Year']*100 + df['Week']
df['YearMonth'] = df['Year']*100 + df['Month']


# In[ ]:


# QUERY
test = df.query('Column1 == "whatyouwanttofind"')


# # SIMPLE PLOTS

# In[ ]:


# SCATTER PLOTS
df.plot(kind = "scatter", x="column1", y ="column2", figsize=(20,5))
plt.show()


# In[ ]:


# SCATTER PLOTS WITH TRANSPARENT MARKERS DUE TO MANY OVERLAPS
df.plot(kind = "scatter", x="column1", y ="column2", alpha=0.1, figsize=(20,5))
plt.show()

