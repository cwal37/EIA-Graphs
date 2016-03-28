# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:05:55 2016

@author: Connor
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.font_manager import FontProperties
import matplotlib.patheffects as path_effects

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 15})

# Code to bring in data and generate a csv to save graphing data somewhere so I
# don't need to run this code every time, and I have a "physical" file to inspect.

#future_gen = pd.read_csv('gen_future_Y2014.csv', skiprows = 1)
current_gen = pd.read_csv('gen_exist_Y2014.csv', skiprows = 1, low_memory = False)

years = np.array(list(set(current_gen['Operating Year'])))


sort_idx = years.argsort()
years = years[sort_idx]

graph_data = [] 
graph_data.append(['Year', 'Technology', 'Prime Mover', 'Capacity', 'Fraction'])

prime_movers = list(set(current_gen['Prime Mover']))
technologies = list(set(current_gen['Technology']))

for year in years:
    
    running_plants = current_gen[current_gen['Operating Year'] <= year]
    current_years  = 
    

    
    total_cap = np.sum(pd.to_numeric(pd.Series(running_plants['Nameplate Capacity (MW)']), errors='coerce'))
    
    for tech in technologies:
        tech_gen = running_plants[running_plants['Technology'] == tech]
        tech_gen_MW = pd.to_numeric(pd.Series(tech_gen['Nameplate Capacity (MW)']), errors='coerce')
        tech_gen_total = np.sum(tech_gen_MW)
        tech_gen_fraction = tech_gen_total/total_cap
        graph_data.append([year, tech, 'NaN', tech_gen_total, tech_gen_fraction])
        
    for PM in prime_movers:
        tech_gen = running_plants[running_plants['Prime Mover'] == PM]
        tech_gen_MW = pd.to_numeric(pd.Series(tech_gen['Nameplate Capacity (MW)']), errors='coerce')
        tech_gen_total = np.sum(tech_gen_MW)
        tech_gen_fraction = tech_gen_total/total_cap
        graph_data.append([year, 'NaN', PM, tech_gen_total, tech_gen_fraction])
        
        

graphing_data = pd.DataFrame(columns=graph_data[0])      
      
for i in range(1,len(graph_data)):
    graphing_data.loc[i] = graph_data[i]
    
#graphing_data.to_csv('graphing_data.csv')
print 'done'