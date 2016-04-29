# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:16:28 2016

@author: Connor
"""
import os
from os import walk
import pandas as pd



# this function walks through a directory of csvs and filters them all be a specific
# column and value pair, returning filtered csvs to the host directory of the script
# calling the function

def file_walk(directory):
    file_name_list = []
    for (dirpath, dirnames, filenames) in walk(directory):
        file_name_list.extend(filenames)
        break
    return(file_name_list)



def filter_walk(source_directory, output_directory, column, value):
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)    
    
    file_name_list = []
    for (dirpath, dirnames, filenames) in walk(source_directory):
        file_name_list.extend(filenames)
        break
    
    for fname in file_name_list:
        
        df = pd.read_csv(source_directory+ '\\' + fname)
        df = df[df[column] == value]
        output_name = output_directory+ '\\' + fname
        df.to_csv(output_name, index = False)
        


    
        
