import matplotlib.pyplot as plt 

#some data 
lables = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]

#Make figures and axes
fig, axs = plt.subplot(2,2)
plt.show()

# #A standard pie plot
# axs[0,0].pie(fracs, lables=lables, autopct='%1.1f%%', shadow=True)
# plt.show()