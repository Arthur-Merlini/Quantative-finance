#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importando bibliotecas 
import numpy as np
import pandas as pd


# In[ ]:


#criando uma coluna com numeros aleatórios
ser = pd.Series(np.random.random(5), name = 'Column 01')


# In[ ]:


ser


# In[ ]:


ser[2]


# In[ ]:


#criando/lidando com um dataframe
from pandas_datareader import data as wb
import os
from datetime import datetime


# In[ ]:


#problema de acesso premium 
Apple = wb.DataReader('AAPL', 'av-daily', start = datetime(2017, 2, 9), end = datetime(2017, 2, 11), api_key = '8OTFNR12KP38EXUU')


# In[ ]:


PG = wb.DataReader('PG', data_source='iex', start='2015-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')


# In[ ]:


#relatório do ativo desde 2015-1-1
PG


# In[ ]:


#serie temboral com o preço de fechamento de ativo de 5 empresas
tickers = ['PG', 'MSFT', 'F', 'T', 'GE']
new_data = pd.DataFrame()


# In[ ]:


for t in tickers:
    new_data[t] = wb.DataReader(t, data_source='iex', start='2015-1-1', api_key = 'pk_09adddafbb16416a908664ee4e93ae8f')['close']


# In[ ]:


new_data.tail(20)


# In[ ]:


#Outras formas de extrair dados financeiros
import quandl


# In[ ]:


mydata_01 = quandl.get('FRED/GDP')


# In[ ]:


mydata_01.head()


# In[ ]:


#salvando em arquivo de formatos csv e excel 
mydata_01.to_csv('C:/Users/arthu/OneDrive/Documentos/exemplo.csv')
mydata_01.to_excel('C:/Users/arthu/OneDrive/Documentos/exemplo.xlsx')


# In[ ]:


#importando bases da maquina 
mydata_02 = pd.read_csv('Downloads\Data_02.csv', index_col = 'Date')
mydata_03 = pd.read_excel('Downloads\Data_03.xlsx')


# In[ ]:


mydata_02.head(8)


# In[ ]:


mydata_03.head(8)


# In[ ]:


#index 
mydata_03.set_index('Year')


# In[ ]:


mydata_03


# In[ ]:


#método de set index
mydata_03 = mydata_03.set_index('Year')
mydata_03


# In[ ]:




