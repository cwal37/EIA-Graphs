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
import pdb
import time

plt.close()
mpl.rcdefaults()
mpl.rcParams['figure.figsize'] = 14, 9
plt.style.use('ggplot')
mpl.rcParams.update({'font.size': 15})

# Code to bring in data and generate a csv to save graphing data somewhere so I
# don't need to run this code every time, and I have a "physical" file to inspect.

#future_gen = pd.read_csv('gen_future_Y2014.csv', skiprows = 1)
#current_gen = pd.read_csv('gen_exist_Y2014.csv', skiprows = 1, low_memory = False)
#past_gen = pd.read_csv('gen_past_Y2014.csv', skiprows = 1, low_memory = False)
#
generators = pd.read_csv('gen_exist_and_ret_Y2014.csv', skiprows = 1, low_memory = False)







# add a list to the set of lists that includes the MW retired from each year in each year
# so this list will be blank for a while until stuff starts getting retired






"""
put everything in a technology loop, I can use the categories I designed
for that incorrect graph a few days ago.

Need to deal with some keyerrors probably, as specific year and tech combos
definitely are gonna be 0, and I assume the sum function doesn't like that.
Also, retirement will need to be treated similarly.
Also, this will greatly expand the dataset, like at least (data*5)?
Also, each tech is an island, indepedent fraction, so not aginst the whole,
although I could work that through later.

1. Add tech categories
2. Add outer tech loop
3. Check keyerror error
4. Build new dataframe
5. Add in a graphing loop to deal with new categories


ALTERNATE
Add a bar graph to original graph to show # of generators built.

"""
#start = time.clock()
#print 'hello'
#
#graph_data = [] 
#graph_data.append(['current_year','tech', 'cap_added', 'year_calc', 'Fraction', 'Age', 'cap_retired', 'weighted_age'])
#
#technologies = list(set(generators['Plant Type']))
#
#for tech in technologies:
#    tech_gen = generators[generators['Plant Type'] == tech]
#    
#    op_years = np.array(list(set(tech_gen['Operating Year'])))
#    sort_idx = op_years.argsort()
#    op_years = op_years[sort_idx]
#    
#    ret_years = np.array(list(set(tech_gen['Retirement Year'])))
#    sort_idx = ret_years.argsort()
#    ret_years = ret_years[sort_idx]
#    
#    start_year = np.min(op_years)
#    years_tracked = []
#
#    for op_year in op_years:
#        
#        # generators that are new in this year
#        new_plants = tech_gen[tech_gen['Operating Year'] == op_year] 
#        cap_added = np.sum(pd.to_numeric(pd.Series(new_plants['Nameplate Capacity (MW)']), errors='coerce'))
#    
#        ret_plants = tech_gen[tech_gen['Retirement Year'] == op_year]
#        cap_retired = np.sum(pd.to_numeric(pd.Series(ret_plants['Nameplate Capacity (MW)']), errors='coerce'))
#        if cap_added > 0 or cap_retired > 0:
#            years_tracked.append(op_year)
#
#            # generators that operated in this year and prior (might include retirees)
#            op_plants = tech_gen[tech_gen['Operating Year'] <= op_year]
#            cap_active = np.sum(pd.to_numeric(pd.Series(op_plants['Nameplate Capacity (MW)']), errors='coerce'))    
#            
#            for tyear in years_tracked:
#                
#                age = (tyear - op_year)*-1 + 1
#                df_year = op_plants[op_plants['Operating Year'] == tyear]
#                year_cap = np.sum(pd.to_numeric(pd.Series(df_year['Nameplate Capacity (MW)']), errors='coerce'))
#                
#                df_ret_year = op_plants[op_plants['Retirement Year'] == tyear]
#                year_ret_cap = np.sum(pd.to_numeric(pd.Series(df_ret_year['Nameplate Capacity (MW)']), errors='coerce'))
#                
#                
#                year_cap = year_cap - year_ret_cap
#                
#                
#                try:
#                    fraction = year_cap/cap_active
#                    weighted_age = fraction*age
#                    graph_data.append([op_year, tech, cap_added, tyear, fraction, age, cap_retired, weighted_age])
#                
#                except ZeroDivisionError: 
#                    error=0
#        else:
#            print 'No '+ tech+' capacity added in '+ str(op_year)
#
#        
#print 'writing'
#graphing_data = pd.DataFrame(graph_data, columns=graph_data[0])      
#print 'saving'
#graphing_data.to_csv('tech_weighted_capacity_datav3.csv')
#print 'done'
#
#end = time.clock()
#print(end-start)


#for i in range(0,len(graph_data)):
#    graphing_data.loc[i] = graph_data[i+1]
#    if i == 100000:
#        print '30%+ written'
#    elif i == 200000:
#        print '60%+ written'
#    elif i == 300000:
#        print 'Over 95% written, nearly there'

##
#
#df = pd.read_csv('tech_weighted_capacity_datav3.csv', skiprows = 1, low_memory = False)
#
#single_add = df[df['year_calc'] == 1891]
#
#final_data = []
#
#ptypes = list(set(df['tech']))
#
#final_data.append(['Year', 'Plant Type', 'Cap_added', 'Capacity-Weighted Age'])
#
#for ptype in ptypes:
#    ptype_df = df[df['tech'] == ptype]
#    
#    calc_years = np.array(list(set(ptype_df['current_year'])))
#    sort_idx = calc_years.argsort()
#    calc_years = calc_years[sort_idx]
#    
#    for year in calc_years:
#        
#        year_df = ptype_df[ptype_df['current_year'] == year]
#        year_weighted_age = np.sum(pd.to_numeric(pd.Series(year_df['weighted_age']), errors='coerce'))
#        
## sum of MW  from specific plant type in specific year, however, there are potentially
## a lot of entries in there, so I'm dividing by the number of entries to get the
## singular value, this can probably be fixed up the chain in this script.         
#        cap_added = (np.sum(pd.to_numeric(pd.Series(year_df['cap_added']), errors='coerce')))/len(year_df['current_year'])
#
#        
#        #cap_added_df = single_add[single_add['current_year'] == year]
#        
#        #cap_added = (cap_added_df['cap_added'])
#        #cap_added = cap_added[0]
#        #if ptype == 'Other' and year == 1925:
#         #   pdb.set_trace()
#        
#        final_data.append([year, ptype, cap_added, year_weighted_age])
#        
#        print year
#    
#f_data = pd.DataFrame(final_data, columns=final_data[0])      
#f_data.to_csv('tech_weighted_capacity_data_finalv4.csv')
####      
###for i in range(1,len(final_data)):
###    f_data.loc[i] = final_data[i]
####    
##    
##    

#print 'done'    

colors = ['k','#FFB300', '#803E75', '#FF6800', '#A6BDD7', '#C10020', '#CEA262',
          '#817066', '#007D34', '#F6768E', '#00538A', '#FF7A5C']
    
    
df = pd.read_csv('tech_weighted_capacity_data_finalv4.csv', skiprows = 1, low_memory = False)
ptypes = list(set(df['Plant Type']))

i = 0
fig, ax = plt.subplots()
for x in ptypes:
    tech_df = df[df['Plant Type'] == x]
    
    years = list(tech_df['Year'])

    
    w_age = list(tech_df['Capacity-Weighted Age'])

    
    plt.plot(years, w_age, linewidth = 8, label = x, color= colors[i])
    i = i + 1
    
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.11),fancybox=True, shadow=True, ncol=5)
plt.title('Capacity-Weighted Age of US Generators, 1891-2014')
plt.xlabel('Year')
plt.ylabel('Age (years)')
plt.gcf().subplots_adjust(bottom=0.27)

plt.savefig('tech_weighted_capacity_agev2.png', dpi = 400)


    
    

