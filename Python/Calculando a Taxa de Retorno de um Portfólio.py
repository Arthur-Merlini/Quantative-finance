#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[2]:


tickers = ['PG', 'MSFT', 'F', 'GE']
new_data = pd.DataFrame()
for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')['close']


# In[3]:


new_data.info()


# In[4]:


new_data.tail()


# In[5]:


new_data.head()


# In[6]:


new_data.iloc[0]


# In[7]:


new_data.loc['2015-01-02']


# In[8]:


#normalizando os dados para a base 100
#a normalização serve para ter um parâmetro de comparação com base em um mesmo ponto de origem
(new_data/new_data.iloc[0]*100).plot(figsize = (15,6))
plt.show()


# In[9]:


returns = (new_data/new_data.shift(1)) - 1
returns.head()


# In[15]:


weights = np.array([0.25, 0.25,0.25, 0.25])


# In[14]:


#dot serve para multiplicação de vetores
np.dot(returns, weights)


# In[17]:


annual_returns = returns.mean()*250
annual_returns


# In[18]:


np.dot(annual_returns, weights)


# In[19]:


pfolio_1 = str(round(np.dot(annual_returns, weights),5)*100) + '%'
pfolio_1


# In[20]:


#Outra carteira com pesos diferentes
weights_2 = np.array([0.4, 0.4,0.15, 0.05])


# In[23]:


pfolio_2 = str(round(np.dot(annual_returns, weights_2),5)*100) + '%'
print (pfolio_2)
print (pfolio_1)


# In[ ]:




