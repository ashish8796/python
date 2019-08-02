#Documentation
'''
Documentation is used to make your code easier to understand and use.
Docstrings are a type of comment used to explain the purpose of a function, 
and how it should be used.
'''
def population_density(population, land_area):
    """Calculate the population density of an area. """
    return population / land_area

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area