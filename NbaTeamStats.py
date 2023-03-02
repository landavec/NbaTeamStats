#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd
import matplotlib as plt


# In[109]:


#Create dataframe for NBA 2022-2023 Season Team Stats
#Print first 5 rows
df = pd.read_csv("TeamStats2023.csv")
df.head()


# In[110]:


#Create dataframe for NBA 2021-2022 Season Team Stats
#Print first 5 rows
df2 = pd.read_csv("TeamStats2022.csv")
df2.head()


# In[111]:


#view 2022-2023 Season Team Point Averages
points1 = df[["Team","2023PTS"]]
print(points1)


# In[112]:


#view 2021-2022 Season Team Point Averages
points2 = df2[["Team","2022PTS"]]
print(points2)


# In[113]:


#Find league average team points for 2022-2023 NBA Season
#Create variable for Team points averaged in the 2022-2023 Season
ptsavg1 = df["2023PTS"].mean()
print("NBA Teams are scoring " + str(int(ptsavg1)) + " points on average in the 2022-2023 NBA Season.")


# In[114]:


#Find league average team points for 2021-2022 NBA Season
#Create variable for Team points averaged in the 2021-2022 Season
#Retrieve data from 2021-2022 Team averages
ptsavg2 = df2["2022PTS"].mean()
print("NBA Teams are scoring " + str(int(ptsavg2)) + " points on average in the 2021-2022 NBA Season.")


# In[115]:


#Now we will merge both dataframes, specifically the Teams and Points Averages for both seasons
#pd.concat function is able to add strings from a specified column to a varaible (pts) in our new df3
df3 = pd.concat([df[["Team", "2023PTS"]],df2["2022PTS"]], axis=1)
print(df3)


# In[116]:


#Plot a bar graph showing the points averages of all NBA teams for each season
#Change X-axis to NBA Teams
#Change Y-axis to total points
df3.plot(x = "Team", y = ["2023PTS", "2022PTS"], kind = "bar", figsize = (15,8))


# In[ ]:




