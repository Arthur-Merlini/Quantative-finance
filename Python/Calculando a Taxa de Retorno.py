#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[3]:


PG = wb.DataReader('PG', data_source='iex', start='2008-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')


# In[12]:


PG


# In[13]:


#Calculando o taxa de retorno simples 
PG['simple_return'] = (PG['close']/PG['close'].shift(1)) - 1


# In[14]:


PG


# In[15]:


#criando um gráfico 
PG['simple_return'].plot(figsize=(16,5))


# In[16]:


#taxa media de retorno diaria 
avg_returns_d = PG['simple_return'].mean()
avg_returns_d


# In[17]:


#taxa media de retorno anual
avg_returns_a = (PG['simple_return'].mean())*250
avg_returns_a


# In[18]:


#arredondando para um valor significativo
str(round(avg_returns_a,5)*100) + '%'

Retornos Logarítimicos
# In[4]:


#Esse cálculo normalmente é feito quando se trabalha com apenas um ativo em vários períodos de tempo
PG.head()


# In[5]:


PG['log_return'] = np.log(PG['close']/PG['close'].shift(1))
PG['log_return']


# In[8]:


PG['log_return'].plot(figsize = (20,10))
plt.show()


# In[9]:


log_return_d = PG['log_return'].mean()
log_return_d


# In[10]:


log_return_a = log_return_d*250
log_return_a


# In[11]:


str(round(log_return_a, 5)*100)+'%'


# In[ ]:




