#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas
import seaborn


# # Load CSV file into memory 
# 

# In[2]:


data=pandas.read_csv('Desktop/uber-raw-data-apr14.csv')
data.head()


# # Convert DateTime and add some useful columns 
# 

# In[ ]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[5]:


data.tail()


# In[6]:


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)

data.tail()


# In[8]:


def get_weekday(dt):
    return dt.weekday()
data['weekday'] = data['Date/Time'].map(get_weekday)
data.tail()


# In[9]:


def get_hour(dt):
    return dt.hour
data['hour'] = data['Date/Time'].map(get_hour)
data.tail()


# # Let's start the analysis 

# ## Analyze the Date of Month(DoM)

# In[15]:


hist(data.dom, bins=30, rwidth=.8 ,range=(0.5,30.5), color=('salmon'), alpha=(0.5))
xlabel('Date of the month')
ylabel('Frequency')
title('Uber - Frequency by Date of the month(DoM) April 2014')


# In[16]:


def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date


# In[20]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[89]:


bar(range(1,31),by_date_sorted)
seaborn.set(font_scale=0.7)
xticks(range(1,31), by_date_sorted.index)
xlabel('Day of the month')
ylabel('Frequency')
title('Uber - Frequency by date of month April 2014')
("")


# ## Analyze the Hour 

# In[134]:


hist(data.hour,bins=24,range=(0.5,24),color=('indianred'), alpha=0.85)
xticks(range (0,24))
xlabel('hour of the day')
ylabel('Frequency')
title('Uber - Frequency by hour of the day April 2014')
("")


# ## Analyze the weekday 

# In[102]:


hist(data.weekday,bins=7, range=(-.5,6.5), rwidth=.8, color='palevioletred', alpha=0.8)
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
xlabel('Weekday')
ylabel('Frequency')
title('Uber - Frequency by weekday April 2014')
("")


# ## Cross analysis (hour, day of the week)

# In[104]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[106]:


seaborn.heatmap(by_cross)
("")


# ## Latitude and longitude analysis

# In[126]:


hist(data['Lat'], bins=100, range=(40.6,40.9), color='firebrick');


# In[125]:


hist(data['Lon'], bins=100, range=(-74.1,-73.9), color='sienna');


# In[136]:


hist(data['Lat'], bins=100, range=(40.6,40.9), color='darkorchid', alpha=0.5, label='latitude')
grid()
legend(loc='best')
twiny()
hist(data['Lon'], bins=100, range=(-74.1,-73.9), color='darkcyan', alpha=0.5, label='longitude')
grid()
legend(loc='upper left')
("")


# In[144]:


figure(figsize(20,20))
plot(data['Lon'], data['Lat'], '.', ms=1, alpha=.5)
xlim(-74.2,-73.7)
ylim(40.7,41)


# In[ ]:




