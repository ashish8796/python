import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972] #population in billion 

plt.plot (year, pop) #plot the data on line graph
plt.show() # used for to show the graph
plt.clf() #used for clear the plot
plt.scatter(year, pop) #plot the data through only dots
plt.show()

