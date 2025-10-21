# SI 201 Project 1
# Your name: Mariam Alkhulaidi
# Your student id: 73128025
# Your email: malkhula@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): 
# If you worked with generative AI also add a statement for how you used it.  
# ""

import csv
#import unittest

def read_penguins_csv(filename): #read penguins file
    penguins = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            penguins.append(row)
    return penguins

#sex percentages per species and island
def sex_percentage_per_species_island(data):
    results = {}

    for info in data:
        species = info.get("species")
        island = info.get("island")
        sex = info.get("sex")
        if sex is None or sex == "NA":
            continue

        #nested dictionary 
        if species not in results:
            results[species] = {}
        if island not in results[species]:
            results[species][island] = {"male": 0, "female": 0, "total": 0}

        sex_lower = sex.lower()
        if sex_lower in {"male", "female"}:
            results[species][island][sex_lower] += 1
            results[species][island]["total"] += 1

    #percentage calc.
    result = []
    for species, islands in results.items():
        for island, counts in islands.items():
            total = counts["total"]
            result.append({
                "species": species,
                "island": island,
                "percent_male": counts["male"] / total * 100,
                "percent_female": counts["female"] / total * 100
            })
    return result
