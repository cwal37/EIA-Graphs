# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:12:20 2016

@author: Connor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

future_gen = pd.read_csv('gen_future_Y2014.csv', skiprows = 1)
current_gen = pd.read_csv('gen_exist_Y2014.csv', skiprows = 1)

years = np.array(list(set(current_gen['Operating Year'])))


sort_idx = years.argsort()
years = years[sort_idx]

graph_data = ['Year', 'Technology', 'Prime Mover' 

for year in years:
    year_gens = current_gen[current_gen['Operating Year'] == year]
    
    prime_movers = list(set(year_gens['Prime Mover']))
    technologies = list(set(year_gens['Technology']))
    
    running_plants = current_gen[current_gen['Operating Year'] <= year]
    total_cap = np.sum(running_plants['Nameplate Capacity (MW)'])
    
    