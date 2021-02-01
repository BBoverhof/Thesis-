#!/usr/bin/env python
"""
@Author: Bart-Jan Boverhof
@Description: Central script with which data is read, windows are created and epochs are constructed.
"""
#### Prerequisites ####
#Importing packages
import pyxdf
import pandas as pd
import pickle
import os
import csv

#Setting WD to "Masterthesis/5.pipeline" folder. 
os.chdir("pipeline")

try:
    from transformer import transformer
except ModuleNotFoundError:
    wd = os.getcwd()
    print("Please make sure that working directory is set as '../Masterthesis/pipeline'")
    print("Current working directory is:", wd)

#### Preliminaries ####
#Defining required events and streams
event_list = ['1', '2', '3', 'break', 'rest']
stream_types_list = ['PPG', 'GSR', 'EEG']

#Window creation related parameters
block_start_margin = 0  
block_end_margin = 0    
window_size = 5  
window_overlap = 1     
window_exact = False     

#### Open labels file
labels = pd.read_csv("data/labels.csv", delimiter = ",")    



if __name__ == '__main__': 
    #First segment
    seg1 = transformer("data/bc10/bci10 operations.xdf", event_list, block_start_margin, block_end_margin, window_size, window_overlap, window_exact, stream_types_list) #Cut first segment
    with open('prepared_data/10_1.pickle', 'wb') as handle: #Save as .pickle
        pickle.dump(seg1, handle, protocol=pickle.HIGHEST_PROTOCOL)

    #Second segment
    seg2 = transformer("data/bc10/bci 10 engineering+.xdf", event_list, block_start_margin, block_end_margin, window_size, window_overlap, window_exact, stream_types_list)
    with open('prepared_data/10_2.pickle', 'wb') as handle: #Save as .pickle
        pickle.dump(seg2, handle, protocol=pickle.HIGHEST_PROTOCOL)

    #Third segment
    seg3 = transformer("data/bc10/bci10 tactical.xdf", event_list, block_start_margin, block_end_margin, window_size, window_overlap, window_exact, stream_types_list)
    with open('prepared_data/10_3.pickle', 'wb') as handle: #Save as .pickle
        pickle.dump(seg3, handle, protocol=pickle.HIGHEST_PROTOCOL)
