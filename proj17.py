#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import folium as fo
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


map = fo.Map()


# In[ ]:


map


# In[ ]:


x = fo.FeatureGroup(name='My Map')


# In[ ]:


x.add_child(fo.Marker(location=[27.1750,78.0422] , popup='hey' , icon=fo.Icon(color='blue')))


# In[ ]:


map.add_child(x)


# In[ ]:


for lat,lon in ([34,53],[24,-50],[90,-68]):
    x.add_child(fo.Marker(location=[lat,lon] ,
                          popup='hey' , icon=fo.Icon(color='red')))


# In[ ]:


map.add_child(x)


# In[ ]:


volcano = pd.read_csv('volcano.csv')


# In[ ]:


lat_vo = list(volcano['Latitude'])
lon_vo = list(volcano['Longitude'])
name_vo = list(volcano['Name'])


# In[ ]:


vol = fo.FeatureGroup(name='My Map')


# In[ ]:


for lat,lon,name in zip(lat_vo,lon_vo,name_vo):
    vol.add_child(fo.Marker(location=[lat,lon] ,
                          popup=name , icon=fo.Icon(color='red')))


# In[ ]:


map.add_child(vol)


# In[ ]:


vol.add_child(fo.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read())))


# In[ ]:


map.add_child(vol)


# In[ ]:


popu = pd.read_csv('us cities pop.csv')


# In[ ]:


popu.head()


# In[ ]:


lat_po = list(popu['lat'])
lon_po = list(popu['lon'])
name_po = list(popu['name'])
pop_po = list(popu['pop'])


# In[ ]:


po = fo.FeatureGroup(name='My Map')


# In[ ]:


def mar(popu):
    if(popu>35000):
        return 'red'
    elif(popu>10000 and popu<=35000):
        return 'blue'
    else:
        return 'green'


# In[ ]:


for lat,lon,name,pop in zip(lat_po,lon_po,name_po,pop_po):
    po.add_child(fo.Marker(location=[lat,lon],popup=[pop,name] , 
                          icon=fo.Icon(color=mar(pop))))


# In[ ]:


map.add_child(po)


# In[ ]:





# In[ ]:




