import matplotlib.pyplot as plt 


y_views = [534,689,258,401,724,689,350,202,209,176,415,824,389,550]
f_views = [534,689,258,401,724,689,350,202,209,176,415,824,389,550]
days = range(1,15)

#ploting bar charts
plt.bar([a-.25 for a in days], y_views, width=.25, label="Youtube views",align='edge')
plt.bar([a+.25 for a in days], y_views,width=-.25,  label="Facebook views",align='edge')
plt.xlabel("Day")
plt.ylabel("Views")
plt.legend(loc="upper left")
plt.title("Daily views for Marketing channels")
plt.grid(True, linewidth=1, color='g', linestyle='-.')



plt.show()