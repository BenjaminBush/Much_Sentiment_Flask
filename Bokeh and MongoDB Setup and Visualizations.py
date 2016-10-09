
# coding: utf-8

# In[109]:

#!/usr/bin/env python

import pymongo as pm
import pandas as pd
import numpy as np
from datetime import datetime
import urllib2
from bokeh.io import curdoc, output_file, show, vform, output_notebook
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import PreText, Select, MultiSelect, CheckboxButtonGroup
from bokeh.plotting import figure


# ### General Bokeh Workflow:
# 
# - Prepare some data (in this case plain python lists).
# - Tell Bokeh where to generate output (in this case using output_file(), with the filename "lines.html").
# - Call figure() to create a plot with some overall options like title, tools and axes labels.
# - Add renderers (in this case, Figure.line) for our data, with visual customizations like colors, legends and widths to the plot.
# - Ask Bokeh to show() or save() the results.

# In[5]:

mongo_uri = "mongodb://ec2-52-38-154-245.us-west-2.compute.amazonaws.com:27017"
client = pm.MongoClient(mongo_uri)
db = client['prod']


# In[10]:

debates = pd.DataFrame(list(db.debates.find({})))


# In[9]:

def lru_cache():
    def dec(f):
        def _(*args, **kws):
            return f(*args, **kws)
        return _
    return dec


# In[11]:

performance = pd.DataFrame(list(db.performance.find({})))


# In[12]:

performance.head()


# In[22]:




# In[27]:

data = get_data("performance")


# In[28]:

data


# In[36]:




# In[30]:

performance_source = ColumnDataSource(data)


# In[60]:




# In[99]:

speaker_queries = pd.DataFrame(list(db.speakers.find({})))
names = sorted(list(name.encode('utf-8','ignore') for name in speaker_queries["name"].unique()))
states = sorted(list(state.encode('utf-8','ignore') for state in speaker_queries["state"].unique()))
years = sorted(list(set(list(str(date.year) for date in speaker_queries[::2]['year']))))


# In[214]:

names


# In[205]:

party = CheckboxButtonGroup(labels=['Republican','Democrat','Independent'], active=[0,1,2])
name = CheckboxButtonGroup(labels=names, active=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
prior_experience = CheckboxButtonGroup(labels=["Incumbent", "Challenger"], active=[0,1])
election_result = CheckboxButtonGroup(labels=["Win","Lose"], active =[0,1])
state = CheckboxButtonGroup(labels=states, active=[0,1,2,3,4,5,6,7,8,9,10,11])
year = CheckboxButtonGroup(labels=years, active=[0,1,2,3,4,5,6,7,8,9,10,11])


# In[112]:

show(year)


# In[110]:

output_notebook()


# In[216]:

name.active = [0,1]


# In[203]:

def speaker_filter(party_arr, prior_experience_arr, election_result_arr, name_arr, state_arr, date_max, date_min):
    query = {}
    query['party'] = {'$in': party_arr}
    query['incumbent'] = {'$in': prior_experience_arr}
    query['election_result'] = {'$in': election_result_arr}
    query['name'] = {'$in': name_arr}
    query['state'] = {'$in': state_arr}
    query['year'] = {'$lt': date_max, '$gt': date_min}
    mongo_data = list(db.speakers.find(query, {'speaker_id':1}))
    ret_list = []
    for val in mongo_data:
        ret_list.append(val['speaker_id'].encode('utf-8','ignore'))
    return ret_list


# In[211]:

def update_performance_data(selected=None):
    party_arr = [party.labels[i] for i in party.active]
    prior_experience_arr = [True if prior_experience.labels[i] == "Incumbent" else False for i in prior_experience.active]
    election_result_arr = [election_result.labels[i].lower() for i in election_result.active]
    name_arr = [name.labels[i] for i in name.active]
    state_arr = [state.labels[i] for i in state.active]
    date_max = datetime((max([int(year.labels[i]) for i in year.active]) + 1),1,1)
    date_min = datetime((min([int(year.labels[i]) for i in year.active]) - 1),12,31)
    speaker_list = speaker_filter(party_arr, prior_experience_arr, election_result_arr, name_arr, state_arr, date_max, date_min)
    performance_data = pd.DataFrame(list(db.performance.find({'$or':[{'speakers.republican.speaker_id':{'$in': speaker_list}}, 
                                                                     {'speakers.democrat.speaker_id':{'$in': speaker_list}}, 
                                                                     {'speakers.independent.speaker_id':{'$in': speaker_list}}]})))
    return performance_data


# In[ ]:

def update_debate_data(selected=None):
    party_arr = [party.labels[i] for i in party.active]
    prior_experience_arr = [True if prior_experience.labels[i] == "Incumbent" else False for i in prior_experience.active]
    election_result_arr = [election_result.labels[i].lower() for i in election_result.active]
    name_arr = [name.labels[i] for i in name.active]
    state_arr = [state.labels[i] for i in state.active]
    date_max = datetime((max([int(year.labels[i]) for i in year.active]) + 1),1,1)
    date_min = datetime((min([int(year.labels[i]) for i in year.active]) - 1),12,31)
    speaker_list = speaker_filter(party_arr, prior_experience_arr, election_result_arr, name_arr, state_arr, date_max, date_min)
    debate_data = pd.DataFrame(list(db.debates.find({'$or':[{'speakers.republican.speaker_id':{'$in': speaker_list}}, 
                                                                     {'speakers.democrat.speaker_id':{'$in': speaker_list}}, 
                                                                     {'speakers.independent.speaker_id':{'$in': speaker_list}}]})))
    return debate_data


# In[ ]:




# In[213]:

x.head()


# In[75]:

data


# In[ ]:

def get_data(collection, query = {}):
    coll = db[collection]
    data = pd.DataFrame(list(coll.find(query)))
    return data

