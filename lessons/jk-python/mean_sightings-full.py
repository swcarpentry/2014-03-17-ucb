#!/usr/bin/env python

'''
Module/script to calculate mean number of sightings of a given animal in a 
given sightings csv file.
'''

import sys
import pandas as pd
import numpy as np


def get_sightings(filename, focusanimal):

    # Load table
    tab = pd.read_csv(filename)

    # Standardize capitalization of focusanimal
    focusanimal = focusanimal.capitalize()

    # Find number of records and total count of animals seen
    isfocus = (tab['Animal'] == focusanimal)
    totalrecs = np.sum(isfocus)

    if totalrecs == 0:
        meancount = 0
    else:
        meancount = np.mean(tab['Count'][isfocus])

    # Return num of records and animals seen
    return totalrecs, meancount


def get_sightings_loop(filename, focusanimal):

    # Load table
    tab = pd.read_csv(filename)

    # Standardize capitalization of focus animal
    focusanimal = focusanimal.capitalize()

    # Loop through all records, countings recs and animals
    totalrecs = 0
    totalcount = 0
    for i, rec in tab.iterrows(): # Iterate through DataFrame rows
        if rec['Animal'] == focusanimal:
            totalrecs += 1
            totalcount += rec['Count']

    meancount = totalcount/totalrecs

    # Return num of records and animals seen
    return totalrecs, meancount

if __name__ == '__main__':
    #print sys.argv
    filename = sys.argv[1]
    focusanimal = sys.argv[2]
    print get_sightings(filename, focusanimal)
