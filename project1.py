# SI 201 Project 1
# Your name: Mariam Alkhulaidi
# Your student id: 73128025
# Your email: malkhula@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): 
#Solo Project
# If you worked with generative AI also add a statement for how you used it.  
# "I asked Chatgpt hints for debugging and suggesting the general sturcture of the code, 
# as well as pointing out errors and giving me explanations for when I didn't understand certain code"


# SI 201 Project 1
# Your name: Mariam Alkhulaidi
# Your student id: 73128025
# Your email: malkhula@umich.edu
# Who or what you worked with on this project (including generative AI like ChatGPT): 
# If you worked with generative AI also add a statement for how you used it.  
# ""

import csv
import unittest

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
        if sex == "NA":
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
       if bill in ("NA") or flipper in ("NA"):
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

def write_csv(filename, data, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

data = read_penguins_csv("penguins.csv")

#print out sex percentages
sex_stats = sex_percentage_per_species_island(data)
print(sex_stats)  
write_csv("sex_percentages.csv", sex_stats, fieldnames=["species", "island", "percent_male", "percent_female"]) 

#prints out bill and flipper averages
avg_stats = bill_flipper_stats(data)
print(avg_stats)  
write_csv("avg_bill_flipper.csv", avg_stats, fieldnames=["species", "avg_bill_length_mm", "avg_flipper_length_mm"])

#unit tests
class TestPenguinsFunctions(unittest.TestCase):
    #tests for the sex_percentage_per_species_island
    #regular tests 
    def test_sex_percentage_general(self):
        data = [
            {"species": "Adelie", "island": "Torgersen", "sex": "male"},
            {"species": "Adelie", "island": "Torgersen", "sex": "female"}
        ]
        result = sex_percentage_per_species_island(data)
        self.assertEqual(result[0]['percent_male'], 50.0)
        self.assertEqual(result[0]['percent_female'], 50.0)

        data = [
            {"species": "Adelie", "island": "Biscoe", "sex": "male"},
            {"species": "Adelie", "island": "Dream", "sex": "female"}
        ]
        result = sex_percentage_per_species_island(data)
        self.assertEqual(result[0]['percent_male'], 100.0)
        self.assertEqual(result[1]['percent_female'], 100.0)
    #edge tests
    def test_sex_percentage_na_values(self):
        data = [
            {"species": "Gentoo", "island": "Biscoe", "sex": "NA"},
            {"species": "Gentoo", "island": "Biscoe", "sex": "NA"}
        ]
        result = sex_percentage_per_species_island(data)
        self.assertEqual(result, [])

    def test_sex_percentage_single_penguin(self):
        data = [{"species": "Adelie", "island": "Torgersen", "sex": "male"}]
        result = sex_percentage_per_species_island(data)
        self.assertEqual(result[0]['percent_male'], 100.0)
        self.assertEqual(result[0]['percent_female'], 0.0)

    #tests for bill_flipper_stats
    #regular tests
    def test_bill_flipper_general(self):
        data = [
            {"species": "Adelie", "bill_length_mm": "38.6", "flipper_length_mm": "191"},
            {"species": "Adelie", "bill_length_mm": "42.5", "flipper_length_mm": "197"}
        ]
        result = bill_flipper_stats(data)
        self.assertEqual(result[0]['avg_bill_length_mm'], 40.55)
        self.assertEqual(result[0]['avg_flipper_length_mm'], 194.0)

    def test_bill_flipper_multiple_species(self):
        data = [
            {"species": "Gentoo", "bill_length_mm": "53.4", "flipper_length_mm": "219"},
            {"species": "Chinstrap", "bill_length_mm": "47", "flipper_length_mm": "185"}
        ]
        result = bill_flipper_stats(data)
        self.assertEqual(len(result), 2)
    #edge tests
    def test_bill_flipper_na_values(self):
        data = [
            {"species": "Adelie", "bill_length_mm": "NA", "flipper_length_mm": "NA"},
            {"species": "Gentoo", "bill_length_mm": "NA", "flipper_length_mm": "NA"}
        ]
        result = bill_flipper_stats(data)
        self.assertEqual(result, [])

    def test_bill_flipper_single_penguin(self):
        data = [{"species": "Chinstrap", "bill_length_mm": "49", "flipper_length_mm": "210"}]
        result = bill_flipper_stats(data)
        self.assertEqual(result[0]['avg_bill_length_mm'], 49.0)
        self.assertEqual(result[0]['avg_flipper_length_mm'], 210.0)

if __name__ == "__main__":
    unittest.main()
