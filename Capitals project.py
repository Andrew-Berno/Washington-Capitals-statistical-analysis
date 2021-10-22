#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[1]:


caps_1920_all = pd.read_csv('capitals_1920_all.csv')
caps_2021_all = pd.read_csv('capitals_2021_all.csv')
caps_1920_pp = pd.read_csv('capitals_1920_pp.csv')
caps_2021_pp = pd.read_csv('capitals_2021_pp.csv')
caps_all = pd.concat([caps_1920_all, caps_2021_all])
caps_pp = pd.concat([caps_1920_pp, caps_2021_pp])
caps_all = caps_all.set_index('Season')
caps_pp = caps_pp.set_index('Season')
print(caps_all.head())


# In[6]:


# an overview of significant metrics comparing the two seasons
fig,axes = plt.subplots(nrows=2,ncols=2,figsize=(6,6))
caps_all['GF%'].plot(kind='bar',ax=axes[0,0],yticks=[10,20,30,40,50])
caps_all['GF/60'].plot(kind='bar',ax=axes[0,1],yticks=[0,1,2,3,4])
caps_all['GA/60'].plot(kind='bar',ax=axes[1,0],yticks=[0,1,2,3,4])
caps_all['CF/60'].plot(kind='bar',ax=axes[1,1],yticks=[0,15,30,45,60])
plt.subplots_adjust(hspace=0.75,wspace=0.5)
axes[0,0].set_ylabel('Goals For %')
axes[0,1].set_ylabel('Goals For/60')
axes[1,0].set_ylabel('Goals Against/60')
axes[1,1].set_ylabel('Corsi For/60')
plt.show()


# In[ ]:





# In[ ]:





# In[7]:


caps_sh_1920 = pd.read_csv('caps_sh_1920.csv')
caps_sh_2021 = pd.read_csv('caps_sh_2021.csv')
caps_sh = pd.concat([caps_sh_1920, caps_sh_2021])
caps_sh = caps_sh.set_index('Season')
print(caps_sh.head())


# In[137]:


# compare the effectiveness of the power play and penalty kill
fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(6,4))
caps_pp['GF/60'].plot(kind='bar',ax=axes[0])
caps_sh['GA/60'].plot(kind='bar',ax=axes[1],yticks=[0,2,4,6])
axes[0].set_ylabel('PP Goals/60')
axes[1].set_ylabel('SH GA/60')
plt.subplots_adjust(wspace=0.3)
plt.show()


# In[26]:


caps_skaters_1920_all = pd.read_csv('caps_skaters_1920_all.csv')
caps_skaters_1920_all = caps_skaters_1920_all.set_index('Player')
caps_skaters_2021_all = pd.read_csv('caps_skaters_2021_all.csv')
caps_skaters_2021_all = caps_skaters_2021_all.set_index('Player')
caps_skaters_all = pd.concat([caps_skaters_1920_all,caps_skaters_2021_all])
big_six_1920 = caps_skaters_1920_all.loc[['Alex Ovechkin','Nicklas Backstrom','Evgeny Kuznetsov','T.J. Oshie','Tom Wilson','John Carlson'],['GP','Points']]
big_six_2021 = caps_skaters_2021_all.loc[['Alex Ovechkin','Nicklas Backstrom','Evgeny Kuznetsov','T.J. Oshie','Tom Wilson','John Carlson'],['GP','Points']]
big_six_1920['Points'].sum()
print(big_six_2021['Points'].sum())


# In[13]:


caps_skaters_all[['GP','Points']]


# In[ ]:




