#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


df = pd.read_csv('C:/Users/arthu/OneDrive/Documentos/CAPM_Data.csv', index_col = 0)


# In[3]:


df.head(10)


# In[4]:


sec_returns = np.log(df/df.shift(1))
sec_returns


# In[5]:


cov = sec_returns.cov()*250
cov


# In[6]:


cov_with_market = cov.iloc[0,1]
cov_with_market


# In[7]:


market_var = sec_returns['^GSPC'].var()*250
market_var


# In[8]:


PG_Beta = cov_with_market/market_var
PG_Beta


# In[9]:


#como beta esta entre 0 e 1, PG é considerada uma ação defensiva


# In[10]:


#A fórmula do CAPM consiste em Rpg = Rf - Beta*(Rm - Rf), sendo Rf uma taxa de retorno de um ativo livre de risco (fictício, utilizasse normalmente
#tesouro nacional) e beta seria o retorno esperado do ativo de interesse


# In[12]:


PG_er = 0.0025 + PG_Beta*0.05
PG_er


# In[ ]:


# Sharpe = Rpg - Rf / DPpg


# In[13]:


Sharpe = (PG_er - 0.025)/ (sec_returns['PG'].std()*250**0.5)
Sharpe


# In[ ]:





# In[ ]:




