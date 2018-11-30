#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


poll_path = "election_data.csv"
poll_df = pd.read_csv(poll_path)
poll_df.tail()


# In[8]:


total_votes = poll_df["Voter ID"].count()
total_votes


# In[9]:


poll_df["Candidate"].unique()


# In[10]:


khan_votes = poll_df.loc[poll_df["Candidate"] == "Khan"]
khan_votes.head()


# In[20]:


khan_wins = khan_votes["Voter ID"].count()
khan_wins


# In[12]:


correy_votes = poll_df.loc[poll_df["Candidate"] == "Correy"]
correy_votes.head()


# In[21]:


correy_wins = correy_votes["Voter ID"].count()
correy_wins


# In[14]:


li_votes = poll_df.loc[poll_df["Candidate"] == "Li"]
li_votes.head()


# In[22]:


li_wins = li_votes["Voter ID"].count()
li_wins


# In[16]:


otooley_votes = poll_df.loc[poll_df["Candidate"] == "O'Tooley"]
otooley_votes.head()


# In[23]:


otooley_wins = otooley_votes["Voter ID"].count()
otooley_wins


# In[42]:


results_list = {"Candidate": ["Khan", 
                        "Correy", 
                        "Li", 
                        "O'Tooley"],
           "Percentage of Votes Won":["{0:.3f}%".format((khan_wins/total_votes)*100),
                                      "{0:.3f}%".format((correy_wins/total_votes)*100),
                                      "{0:.3f}%".format((li_wins/total_votes)*100),
                                      "{0:.3f}%".format((otooley_wins/total_votes)*100)],
           "Votes Won": ["(" + str(khan_wins) + ")", 
                        "(" + str(correy_wins) + ")", 
                        "(" + str(li_wins) + ")", 
                        "(" + str(otooley_wins) + ")"]}   
results_df = pd.DataFrame(results_list)
results_df.head()


# In[54]:


candidates = results_df["Candidate"].unique().tolist()
candidates


# In[65]:


print("Election Results")
print("--------------------------------")
print("Total Votes : " + str(total_votes))
print("--------------------------------")
print(candidates[0] + " : " + str("{0:.3f}%".format((khan_wins/total_votes)*100)) + " (" + str(khan_wins) + ") ")
print(candidates[1] + " : " + str("{0:.3f}%".format((correy_wins/total_votes)*100)) + " (" + str(correy_wins) + ") ")
print(candidates[2] + " : " + str("{0:.3f}%".format((li_wins/total_votes)*100)) + " (" + str(li_wins) + ") ")
print(candidates[3] + " : " + str("{0:.3f}%".format((otooley_wins/total_votes)*100)) + " (" + str(otooley_wins) + ") ")
print("--------------------------------")
print("Winner : " + results_df["Candidate"].loc[results_df["Percentage of Votes Won"] == results_df["Percentage of Votes Won"].max()].values[0])

