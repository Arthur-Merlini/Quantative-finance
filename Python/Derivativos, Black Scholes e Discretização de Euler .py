#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from scipy.stats import norm
import matplotlib.pyplot as plt  
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


def d1(S, K, r, stdev, T):
    return (np.log(S / K) + (r + stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))
 
def d2(S, K, r, stdev, T):
    return (np.log(S / K) + (r - stdev ** 2 / 2) * T) / (stdev * np.sqrt(T))


# In[3]:


norm.cdf(0)


# In[5]:


norm.cdf(0.25)


# In[6]:


norm.cdf(0.75)


# In[7]:


norm.cdf(9)


# In[8]:


def BSM(S, K, r, stdev, T):
        return (S * norm.cdf(d1(S, K, r, stdev, T))) - (K * np.exp(-r * T) * norm.cdf(d2(S, K, r, stdev, T)))


# In[10]:


data = pd.read_csv('C:/Users/arthu/OneDrive/Área de Trabalho/Pessoal/PG_2007_2017.csv', index_col = 0)


# In[11]:


S = data.iloc[-1]
S


# In[12]:


log_returns = np.log(1 + data.pct_change())


# In[13]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[14]:


#r é a tx livre de risco, k é o preço de exercício e t é a quantidade de tempo
r = 0.025
K = 110.0
T = 1


# In[15]:


d1(S, K, r, stdev, T)


# In[16]:


d2(S, K, r, stdev, T)


# In[17]:


BSM(S, K, r, stdev, T)


# Discretização de Euler para opções

# In[18]:


log_returns = np.log(1 + data.pct_change())


# In[19]:


r = 0.025


# In[20]:


stdev = log_returns.std() * 250 ** 0.5
stdev


# In[21]:


type(stdev)


# In[22]:


#como trata-se de uma série, devemos transformar em um array
type(stdev)


# In[23]:


stdev = stdev.values
stdev


# In[24]:


T = 1.0 
t_intervals = 250 
delta_t = T / t_intervals 

iterations = 10000 


# In[25]:


Z = np.random.standard_normal((t_intervals + 1, iterations))  
S = np.zeros_like(Z) 
S0 = data.iloc[-1]  
S[0] = S0


# In[26]:


for t in range(1, t_intervals + 1):
    S[t] = S[t-1] * np.exp((r - 0.5 * stdev ** 2) * delta_t + stdev * delta_t ** 0.5 * Z[t])


# In[27]:


S


# In[28]:


S.shape


# In[31]:


plt.figure(figsize=(10, 6))
plt.plot(S[:, :10]);


# In[32]:


p = np.maximum(S[-1] - 110, 0)
p


# In[33]:


p.shape


# In[34]:


#p seria o preço de payoff da opção
C = np.exp(-r * T) * np.sum(p) / iterations
C  


# In[ ]:




