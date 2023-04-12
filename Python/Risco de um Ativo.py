#!/usr/bin/env python
# coding: utf-8

# In[1]:


#desvio padrão dos retornos de um ativo = risco/volatilidade
#importando bibliotecas 
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[6]:


tickers = ['PG', 'UL']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source = 'iex', start = '2008-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')['close']


# In[7]:


sec_data.head()


# In[8]:


sec_returns = np.log(sec_data/sec_data.shift(1))


# In[9]:


sec_returns


# PG

# In[10]:


#retorno medio anual da PG
sec_returns['PG'].mean()*250


# In[11]:


#calculando o desvio padrão
sec_returns['PG'].std()


# In[13]:


#desvio padrão anualizado
sec_returns['PG'].std()*250**0.5


# UL

# In[14]:


sec_returns['UL'].mean()*250


# In[15]:


sec_returns['UL'].std()


# In[16]:


sec_returns['UL'].std()*250**0.5


# Comparação

# In[17]:


print(sec_returns['UL'].mean()*250)
print(sec_returns['PG'].mean()*250)


# In[19]:


#transformando para matriz bidimensional
sec_returns[['UL', 'PG']].mean()*250


# In[21]:


sec_returns[['UL', 'PG']].std()*250**0.5


# In[ ]:




