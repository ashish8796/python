import matplotlib.pyplot as plt 


labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0) 

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True,startangle=90)
plt.axis('equal')
plt.show()
