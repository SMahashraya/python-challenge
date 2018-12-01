#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


budget_path = "budget_data.csv"
budget_df0 = pd.read_csv(budget_path)
budget_df0.head()


# In[9]:


total_months_calc = budget_df0["Date"].value_counts()
total_months = total_months_calc.sum()
total_months


# In[10]:


net_total = budget_df0["Profit/Losses"].sum()
net_total


# In[11]:


average = budget_df0["Profit/Losses"].mean()
average


# In[12]:


budget_df0.groupby(["Date"])
budget_df0["Change on Month"] = budget_df0["Profit/Losses"].diff(periods=1)
budget_df0.head(10)


# In[13]:


avg_chg = budget_df0["Change on Month"].mean()


# In[14]:


greatest_inc = budget_df0["Change on Month"].max()


# In[15]:


budget_df = budget_df0.set_index(["Date"])
budget_df.head()


# In[16]:


greatest_inc_dt = budget_df.index[budget_df["Change on Month"] == budget_df["Change on Month"].max()][0]
greatest_inc_dt


# In[17]:


greatest_dec = budget_df["Change on Month"].min()


# In[18]:


greatest_dec_dt = budget_df.index[budget_df["Change on Month"] == budget_df["Change on Month"].min()][0]
greatest_dec_dt


# In[19]:


print("Financial Analysis")
print("-------------------------------")
print("Total Months : " + str(total_months))
print("Total : $" + str(net_total))
print("Average Change : $" + str(round(avg_chg,2)))
print("Greatest Increase in Profits : " + str(greatest_inc_dt) + " $" + str(int(greatest_inc)))
print("Greatest Decrease in Profits : " + str(greatest_dec_dt) + " $" + str(int(greatest_dec)))


# In[36]:


txt_file = open("PyBank_output.txt", "a+")
txt_file.write("Financial Analysis") 
txt_file.write("-------------------------------")
txt_file.write("Total Months : 86")
txt_file.write("Total : $38382578")
txt_file.write("Average Change : $-2315.12")
txt_file.write("Greatest Increase in Profits : Feb-2012 $1926159")
txt_file.write("Greatest Decrease in Profits : Sep-2013 $-2196167")
txt_file.close()