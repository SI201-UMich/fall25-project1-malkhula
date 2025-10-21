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

#average bill and flipper lengths per species
def bill_flipper_stats(data):
   species_totals = {}
   for entry in data:
       species = entry.get("species")
       bill = entry.get("bill_length_mm")
       flipper = entry.get("flipper_length_mm")
       if bill in (None, "", "NA") or flipper in (None, "", "NA"):
           continue
       bill = float(bill)
       flipper = float(flipper)
       if species not in species_totals:
           species_totals[species] = {"bill_sum": 0.0, "flipper_sum": 0.0, "count": 0}
       species_totals[species]["bill_sum"] += bill
       species_totals[species]["flipper_sum"] += flipper
       species_totals[species]["count"] += 1


   result = []
   for species, totals in species_totals.items():
       count = totals["count"]
       avg_bill = totals["bill_sum"] / count
       avg_flipper = totals["flipper_sum"] / count
       result.append({
           "species": species,
           "avg_bill_length_mm": avg_bill,
           "avg_flipper_length_mm": avg_flipper
       })
   return result

data = read_penguins_csv("penguins.csv")

# Sex percentages
sex_stats = sex_percentage_per_species_island(data)
print(sex_stats)  # <--- This prints the list of dictionaries directly

# Bill and flipper averages
avg_stats = bill_flipper_stats(data)
print(avg_stats)  # <--- This prints the list of dictionaries directly