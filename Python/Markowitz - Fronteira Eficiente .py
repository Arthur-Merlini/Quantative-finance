#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
#facilita a plotagem de gráficos no jupyter como também seu armazenamento
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


assets = ['PG', 'AAPL']
pf_data = pd.DataFrame()

for a in assets:
    pf_data[a] = wb.DataReader(a, data_source = 'iex', start = '2010-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')['close']


# In[4]:


pf_data


# In[5]:


(pf_data / pf_data.iloc[0] * 100).plot(figsize=(10,5))


# In[6]:


log_returns = np.log(pf_data / pf_data.shift(1))


# In[7]:


log_returns


# In[8]:


log_returns.mean()*250


# In[9]:


log_returns.cov()*250


# In[10]:


log_returns.corr()*250


# In[19]:


#correlação muito alta dos dois ativos. Na regra de Markowitz, o ideal é trabalhar com ativos de baixa correlação
num_assets = len(assets)


# In[20]:


num_assets


# In[15]:


arr = np.random.random(2)
arr


# In[16]:


#A ideia é que a soma dos dois numeros aleatorios de 1
arr[0] + arr[1]


# In[26]:


#o jeito mais fácil de conseguir esse resultado é fazendo o seguinte:
weights = np.random.random(num_assets)
weights_2 = weights / np.sum(weights)
weights_2


# In[27]:


weights_2[0] + weights_2[1]

Retorno Esperado do Portfolio 
# In[28]:


np.sum(weights_2*log_returns.mean())*250


# Variância Esperada do Portfolio

# In[29]:


np.dot(weights_2.T, np.dot(log_returns.cov() * 250, weights))


# Volatilidade Esperada do Portfolio

# In[30]:


np.sqrt(np.dot(weights_2.T, np.dot(log_returns.cov() * 250, weights)))


# In[31]:


#são 1000 combinações dos mesmos 2 ativos 
# 2 listas com retorno e volatilidade 
pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights_2 = weights / np.sum(weights)
    pfolio_returns.append(np.sum(weights_2 * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights_2.T,np.dot(log_returns.cov() * 250, weights_2))))

pfolio_returns, pfolio_volatilities


# In[32]:


#organizando tudo em um mesmo array (matriz)
pfolio_returns = []
pfolio_volatilities = []

for x in range (1000):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    pfolio_returns.append(np.sum(weights * log_returns.mean()) * 250)
    pfolio_volatilities.append(np.sqrt(np.dot(weights.T,np.dot(log_returns.cov() * 250, weights))))
    
pfolio_returns = np.array(pfolio_returns)
pfolio_volatilities = np.array(pfolio_volatilities)

pfolio_returns, pfolio_volatilities


# In[33]:


portfolios = pd.DataFrame({'Return': pfolio_returns, 'Volatility': pfolio_volatilities})


# In[34]:


portfolios.head()


# In[35]:


#curva de fronteira eficiente de Markowitz
portfolios.plot(x = 'Volatility', y = 'Return', kind = 'scatter', figsize=(10,6))
plt.xlabel('Volatilidade Esperada')
plt.ylabel('Retorno Esperado')


# In[ ]:




