import matplotlib.pyplot as plt 

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#changing the linestyle and linewidth
plt.plot(year, pop, label='population in year',
color="red", marker='o', markerfacecolor="g", linestyle='-.', 
linewidth=5)

plt.xlabel('year')
plt.ylabel('population')
plt.title('population per year')
plt.legend(loc="lower right")
plt.show()