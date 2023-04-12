#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import data as wb
import numpy as np
from scipy.stats import norm
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


receita_esperada = 170
desvio_esperado = 20
repeticoes = 1000


# In[7]:


receita = np.random.normal(receita_esperada,desvio_esperado,repeticoes)
receita


# In[8]:


plt.figure(figsize =(15,6))
plt.plot(receita)
plt.show()


# In[9]:


cmv = - (receita*np.random.normal(0.6,0.1))

plt.figure(figsize =(15,6))
plt.plot(cmv)
plt.show()


# In[10]:


#cmv = custo da mercadoria vendida
#Foi suposto que 60% da receita anual da empresa é gasto para produzir a mercadoria vendida
cmv.mean()


# In[11]:


cmv.std()


# In[12]:


lucro_bruto = receita + cmv
lucro_bruto


# In[13]:


plt.figure(figsize =(15,6))
plt.plot(lucro_bruto)
plt.show()


# In[14]:


#O valor médio encontrado é igual a diferença das médias das receita e do cmv
max(lucro_bruto)


# In[16]:


min(lucro_bruto)


# In[17]:


lucro_bruto.mean()


# In[18]:


lucro_bruto.std()


# In[19]:


#plotando os resultados em um histograma 
plt.figure(figsize =(15,6))
plt.hist(lucro_bruto, bins = 20)
plt.show()


# Previsão do preço de ações 

# In[22]:


df = pd.read_csv('C:/Users/arthu/OneDrive/Área de Trabalho/Pessoal/PG_2007_2017.csv', index_col = 0)
df


# In[24]:


log_returns = np.log(1 + df.pct_change())
log_returns


# In[25]:


log_returns.tail()


# In[26]:


df.plot(figsize=(15,6));


# In[27]:


log_returns.plot(figsize=(15,6));


# In[28]:


u = log_returns.mean()
u


# In[29]:


var = log_returns.var()
var


# In[31]:


drift = u - (var*0.5)
drift


# In[32]:


stdev = log_returns.std()
stdev


# In[33]:


type(drift)


# In[35]:


type(stdev)


# In[36]:


# values tem a mesma função do que o np.array
drift.values


# In[37]:


stdev.values


# In[38]:


# z é a distancia entre os desvios padrão e a média
norm.ppf(0.95)


# In[39]:


x = np.random.rand(10, 2)
x


# In[40]:


norm.ppf(x)


# In[41]:


Z = norm.ppf(np.random.rand(10,2))
Z


# In[42]:


t_intervals = 1000
iterations = 10


# In[44]:


daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
daily_returns


# In[45]:


S0 = df.iloc[-1]
S0


# In[46]:


price_list = np.zeros_like(daily_returns)
price_list


# In[47]:


price_list[0]


# In[48]:


price_list[0] = S0
price_list


# In[49]:


for t in range(1, t_intervals):
    price_list[t] = price_list[t - 1] * daily_returns[t]


# In[50]:


price_list


# In[51]:


plt.figure(figsize=(10,6))
plt.plot(price_list);


# In[ ]:




