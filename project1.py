# SI 201 Project 1
# Your name: Mariam Alkhulaidi
# Your student id: 73128025
# Your email: malkhula@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): 
# If you worked with generative AI also add a statement for how you used it.  
# ""

import csv

def read_penguins_csv(filename): #read penguins file
    penguins = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            penguins.append(row)
    return penguins
