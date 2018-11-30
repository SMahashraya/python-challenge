#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd


# In[117]:


budget_path = "budget_data.csv"
budget_df0 = pd.read_csv(budget_path)
budget_df0.head()


# In[118]:


total_months_calc = budget_df0["Date"].value_counts()
total_months = total_months_calc.sum()
total_months


# In[119]:


net_total = budget_df0["Profit/Losses"].sum()
net_total


# In[120]:


average = budget_df0["Profit/Losses"].mean()
average


# In[121]:


budget_df0.groupby(["Date"])
budget_df0["Change on Month"] = budget_df0["Profit/Losses"].diff(periods=1)
budget_df0.head(10)


# In[122]:


avg_chg = budget_df0["Change on Month"].mean()


# In[123]:


greatest_inc = budget_df0["Change on Month"].max()


# In[126]:


budget_df = budget_df0.set_index(["Date"])
budget_df.head()


# In[131]:


greatest_inc_dt = budget_df.index[budget_df["Change on Month"] == budget_df["Change on Month"].max()][0]
greatest_inc_dt


# In[79]:


greatest_dec = budget_df["Change on Month"].min()


# In[134]:


greatest_dec_dt = budget_df.index[budget_df["Change on Month"] == budget_df["Change on Month"].min()][0]
greatest_dec_dt


# In[137]:


print("Financial Analysis")
print("-------------------------------")
print("Total Months : " + str(total_months))
print("Total : $" + str(net_total))
print("Average Change : $" + str(avg_chg))
print("Greatest Increase in Profits : " + str(greatest_inc_dt) + " $" + str(greatest_inc))
print("Greatest Decrese in Profits : " + str(greatest_dec_dt) + " $" + str(greatest_dec))

