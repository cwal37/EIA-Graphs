# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 14:12:20 2016

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

##future_gen = pd.read_csv('gen_future_Y2014.csv', skiprows = 1)
#current_gen = pd.read_csv('gen_exist_Y2014.csv', skiprows = 1, low_memory = False)
#
#years = np.array(list(set(current_gen['Operating Year'])))
#
#
#sort_idx = years.argsort()
#years = years[sort_idx]
#
#graph_data = [] 
#graph_data.append(['Year', 'Technology', 'Prime Mover', 'Capacity', 'Fraction'])
#
#prime_movers = list(set(current_gen['Prime Mover']))
#technologies = list(set(current_gen['Technology']))
#
#for year in years:
#    
#    running_plants = current_gen[current_gen['Operating Year'] <= year]
#    
#
#    
#    total_cap = np.sum(pd.to_numeric(pd.Series(running_plants['Nameplate Capacity (MW)']), errors='coerce'))
#    
#    for tech in technologies:
#        tech_gen = running_plants[running_plants['Technology'] == tech]
#        tech_gen_MW = pd.to_numeric(pd.Series(tech_gen['Nameplate Capacity (MW)']), errors='coerce')
#        tech_gen_total = np.sum(tech_gen_MW)
#        tech_gen_fraction = tech_gen_total/total_cap
#        graph_data.append([year, tech, 'NaN', tech_gen_total, tech_gen_fraction])
#        
#    for PM in prime_movers:
#        tech_gen = running_plants[running_plants['Prime Mover'] == PM]
#        tech_gen_MW = pd.to_numeric(pd.Series(tech_gen['Nameplate Capacity (MW)']), errors='coerce')
#        tech_gen_total = np.sum(tech_gen_MW)
#        tech_gen_fraction = tech_gen_total/total_cap
#        graph_data.append([year, 'NaN', PM, tech_gen_total, tech_gen_fraction])
#        
#        
#
#graphing_data = pd.DataFrame(columns=graph_data[0])      
#      
#for i in range(1,len(graph_data)):
#    graphing_data.loc[i] = graph_data[i]
#    
##graphing_data.to_csv('graphing_data.csv')
#print 'done'
## prime mover graph

# colors come from "Twenty-Two Colors of Maximum Contrast" by Kenneth L. Kelly"
# I skip white, because I don't need all 22, and don't want a white line.
colors = ['k','#FFB300', '#803E75', '#FF6800', '#A6BDD7', '#C10020', '#CEA262',
          '#817066', '#007D34', '#F6768E', '#00538A', '#FF7A5C']
    
    
    
graphing_data = pd.read_csv('graphing_data.csv')    
tech_data = graphing_data[graphing_data['Technology'] != 'NaN']

years = np.array(list(set(graphing_data['Year'])))
sort_idx = years.argsort()
years = years[sort_idx]

technologies = list(set(graphing_data['Technology']))
technologies.pop(0)

#fig, ax = plt.subplots()
#
##print len(technologies)
##print technologies
##Technologies Graph
#i = 0
#for tech in technologies:
#    specific_tech_data = tech_data[tech_data['Technology'] == tech]
#    
#    fraction = specific_tech_data['Fraction'] *100
#    if np.average(fraction) > 0.75:
#
#        break
#        plt.plot(years, fraction, label=tech, linewidth = 3, color= colors[i])
#        i = i + 1
#    
#legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11),fancybox=True, shadow=True, ncol=2)
#plt.ylim(0,101)
#plt.xlim(1900, 2014)
#plt.xlabel('Year')
#plt.gcf().subplots_adjust(bottom=0.27)
#
#ax.set_ylabel('Percent')
#
#plt.savefig('tech_graph4.png', dpi=400)
##plt.show()
#plt.close()

# PM graph 
PMs = list(set(graphing_data['Plant Type']))
print PMs
PMs.pop(0)
PM_data = graphing_data[graphing_data['Plant Type'] != 'NaN']
fig, ax = plt.subplots()
   
i = 0
for tech in PMs:
    specific_tech_data = PM_data[PM_data['Plant Type'] == tech]
    
    fraction = specific_tech_data['Fraction'] *100
    plt.plot(years, fraction, label=tech, linewidth = 3, color= colors[i])
    i = i + 1
    
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11),fancybox=True, shadow=True, ncol=5)
plt.ylim(0,101)
plt.xlim(1900, 2014)
plt.xlabel('Year')
plt.gcf().subplots_adjust(bottom=0.27)
plt.title('Fuel Type Disposition of United States Operating Generation, 1891-2014')

ax.set_ylabel('Percent')

plt.savefig('plant_type_graph3.png', dpi=400)
plt.show()     
    