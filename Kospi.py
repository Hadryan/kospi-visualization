#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas-datareader')


# In[2]:


import pandas_datareader as pdr


# In[239]:


from datetime import datetime

start = datetime(2020,6,1)
end= datetime(2020,6,30)

df = pdr.get_data_yahoo('^KS11',start,end)


# In[240]:


df


# In[241]:


Kospi=df.iloc[:,3:4]
Kospi


# In[242]:


import numpy as np
Kospi.index=np.array([6.01,6.02,6.03,6.04,6.05,6.08,6.09,6.10,6.11,6.12,6.15,6.16,6.17,6.18,6.19,6.22,6.23,6.24,6.25,6.26,6.29,6.30],dtype=np.float64)
Kospi['model']=['11/12 2/6' , '11/12 0/6' ,'10/12 0/6' , '10/12 0/6' ,'10/12 0/6' ,'10/12 0/6' , '9/12 0/6' , 
             '8/12 0/6','6/12 0/6' , '6/12 0/6','6/12 0/6','6/12 0/6','6/12 0/6','7/12 0/6','6/12 0/6','5/12 0/6',
            '3/12 0/6' ,'3/12 0/6','3/12 0/6','2/12 0/6','2/12 0/6' , '2/12 0/6']
Kospi


# In[243]:


import pandas as pd
import numpy as np
Kospi=pd.DataFrame(Kospi)
Kospi


# In[7]:


get_ipython().system('pip install plotly')


# In[244]:


import plotly.offline as offline
import plotly.graph_objs as go 
offline.init_notebook_mode(connected=True)



# Scatter graph

fig.add_trace(go.Scatter(x=Kospi.index,y=Kospi.Close,name="Close",line=dict(color='Black')))
fig.add_trace(go.Scatter(x=Kospi.index[0:2],y=Kospi.Close.iloc[:2], name="11/12 2/6"))
fig.add_trace(go.Scatter(x=Kospi.index[2:6],y=Kospi.Close.iloc[2:6], name="10/12 0/6"))
fig.add_trace(go.Scatter(x=Kospi.index[6:7],y=Kospi.Close.iloc[6:7], name="9/12 0/6",marker=dict(size=[15])))
fig.add_trace(go.Scatter(x=Kospi.index[7:8],y=Kospi.Close.iloc[7:8], name="8/12 0/6",marker=dict(size=[15])))
fig.add_trace(go.Scatter(x=Kospi.index[8:13],y=Kospi.Close.iloc[8:13], name="6/12 0/6"))
fig.add_trace(go.Scatter(x=Kospi.index[13:14],y=Kospi.Close.iloc[13:14], name="7/12 0/6",marker=dict(size=[15])))
fig.add_trace(go.Scatter(x=Kospi.index[14:15],y=Kospi.Close.iloc[14:15], name="6/12 0/6",marker=dict(size=[15])))
fig.add_trace(go.Scatter(x=Kospi.index[15:16],y=Kospi.Close.iloc[15:16], name="5/12 0/6",marker=dict(size=[15])))
fig.add_trace(go.Scatter(x=Kospi.index[16:19],y=Kospi.Close.iloc[16:19], name="3/12 0/6"))
fig.add_trace(go.Scatter(x=Kospi.index[19:22],y=Kospi.Close.iloc[19:22], name="2/12 0/6"))

#MAKE VERTICAL LINE
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=6.04,
            y0=0,
            x1=6.04,
            y1=2250,
            line=dict(
                color="Black",
                dash="dot",
                width=1
            )))

fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=6.10,
            y0=0,
            x1=6.10,
            y1=2250,
            line=dict(
                color="Black",
                dash="dot",
                width=1
            )))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=6.12,
            y0=0,
            x1=6.12,
            y1=2250,
            line=dict(
                color="Black",
                dash="dot",
                width=1
            )))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=6.19,
            y0=0,
            x1=6.19,
            y1=2250,
            line=dict(
                color="Black",
                dash="dot",
                width=1
            )))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=6.24,
            y0=0,
            x1=6.24,
            y1=2250,
            line=dict(
                color="Black",
                dash="dot",
                width=1
            )))

#ANNOTATION

fig.add_trace(go.Scatter(
    x=[6.03],
    y=[2220],
    mode="markers+text",
    name="Weight #1",
    text=["30"],
    
))
fig.add_trace(go.Scatter(
    x=[6.07],
    y=[2220],
    mode="markers+text",
    name="Weight #2",
    text=["15"],
    
))
fig.add_trace(go.Scatter(
    x=[6.11,6.21],
    y=[2220,2220],
    mode="markers+text",
    name="Weight #3",
    text=["10","10"],
          ))          
fig.add_trace(go.Scatter(
    x=[6.15,6.28],
    y=[2220,2220,2220],
    mode="markers+text",
    name="Weight #4",
    text=["0","0"]   
))





fig.update_shapes(dict(xref='x', yref='y'))
fig.update_layout(title='Kospi Close',
                 xaxis_title='days'
                 , yaxis_title='Price',
                   xaxis = dict(
                           tickmode = 'linear',
                           tick0 = 6.01,
                           dtick = 0.01),
                 yaxis=dict(range=(2000,2250),
                 
           
                 ))
fig.show()

