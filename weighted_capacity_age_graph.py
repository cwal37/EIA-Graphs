# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:12:20 2016

@author: Connor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#future_gen = pd.read_csv('gen_future_Y2014.csv', skiprows = 1)
current_gen = pd.read_csv('gen_exist_Y2014.csv', skiprows = 1, low_memory = False)

years = np.array(list(set(current_gen['Operating Year'])))


sort_idx = years.argsort()
years = years[sort_idx]

graph_data = [] 
graph_data.append(['Year', 'Technology', 'Prime Mover', 'Capacity', 'Fraction'])

for year in years:
    
    running_plants = current_gen[current_gen['Operating Year'] <= year]
    
    prime_movers = list(set(running_plants['Prime Mover']))
    technologies = list(set(running_plants['Technology']))
    
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
    
print 'done'
## prime mover graph
#    
#tech_data = graphing_data[graphing_data['Technology'] != 'NaN']
#
#tech_years = list(set(tech_data['Year']))
#
#for year in tech_years:
#    current_year = tech_data[tech_data['Year'] <= year]
#    tech_list = list(set(current_year['Technology']))
#    
#    for tech in tech_list:
#    




# technology graph
    
    
        
    