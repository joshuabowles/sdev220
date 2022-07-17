#!/usr/bin/env python
# coding: utf-8

# In[47]:


#13.1

import datetime
from datetime import date
now = date.today()
todaysDate = now.isoformat()
todaysDate


# In[48]:


with open("today.txt", "w") as file:
    file.write(todaysDate)


# In[49]:


#13.2
with open("today.txt", "r") as file:
    today_string = file.read()
today_string


# In[44]:


#13.3

with open("today.txt", "r") as file:
    today_string = file.read()
today_string


# In[51]:


#13.3

from datetime import datetime
fmt = "%Y-%m-%d"
datetime.strptime(today_string, fmt)


# In[ ]:




