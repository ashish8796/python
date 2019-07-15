#Compound data structure
#We can include containers in other containers to create compound data structures.

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]                       # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
print(helium)
#{'symbol': 'He', 'number': 2, 'weight': 4.002602}