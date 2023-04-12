#!/usr/bin/env python
# coding: utf-8

# In[2]:


#risco de um portfolio de ações = variância das ações e da correlação entre elas 
import numpy as np
import pandas as pd
from pandas_datareader import data as wb


# In[3]:


tickers = ['PG', 'UL']

sec_data = pd.DataFrame()

for t in tickers:
    sec_data[t] = wb.DataReader(t, data_source = 'iex', start = '2008-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')['close']


# In[4]:


sec_returns = np.log(sec_data/sec_data.shift(1))
sec_returns


# In[5]:


weights = np.array([0.5,0.5])


# In[7]:


#variancia de um portfolio com duas ações é (wa + w'a')**2, sendo w o peso e a o desvio padrão
#multiplicação de matrizes, cov = matriz = B, w.B = wT*B*w
pfolio_var = np.dot(weights.T, np.dot(sec_returns.cov()*250, weights))
pfolio_var


# In[10]:


#calculando a volatilidade da carteira
pfolio_vol = (np.dot(weights.T, np.dot(sec_returns.cov()*250, weights)))**0.5
pfolio_vol


# In[13]:


print(str(round(pfolio_vol, 4)*100)+'%')


# In[14]:


#aumentar/diversificar o número de ações com pouca correlação pode ajudar a diminui o risco não sistemático 
#risco sistemático é aquele qu esta associado a fatores exógenos da carteira
pesos_pfolio = np.array([0.5,0.5])


# In[15]:


pesos_pfolio[0]


# In[16]:


pesos_pfolio[1]


# In[18]:


#risco não sistematico = variancia do portfolio - variancia anual ponderada
#[[]] indica uma matriz bidimensional
PG_var_a = sec_returns[['PG']].var()*250
PG_var_a


# In[19]:


UL_var_a = sec_returns[['UL']].var()*250
UL_var_a


# In[21]:


dr = pfolio_var - (pesos_pfolio[0]**2*PG_var_a) - (pesos_pfolio[1]**2*UL_var_a)
dr


# In[23]:


#isso aconetece porque a matriz tem que ser unidimensional
float(PG_var_a)


# In[24]:


PG_var_a = sec_returns['PG'].var()*250
PG_var_a


# In[25]:


UL_var_a = sec_returns['UL'].var()*250
UL_var_a


# In[26]:


dr = pfolio_var - (pesos_pfolio[0]**2*PG_var_a) - (pesos_pfolio[1]**2*UL_var_a)
dr


# In[27]:


print(str(round(dr, 4)*100) + '%')


# In[28]:


#calculando risco sistematico
#duas maneiras:
n_dr_1 = pfolio_var - dr
n_dr_1


# In[29]:


n_dr_2 = (pesos_pfolio[0]**2*PG_var_a) + (pesos_pfolio[1]**2*UL_var_a)
n_dr_2


# In[32]:


#teste booleano
n_dr_1 == n_dr_2

