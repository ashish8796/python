import matplotlib.pyplot as plt 


y_views = [534,689,258,401,724,689,350,202,209,176,415,824,389,550]
days = range(1,15)

plt.scatter(days, y_views, label="Youtube views")
plt.xlabel("Day")
plt.ylabel("Views")
plt.legend(loc="lower right")
plt.title("Daily views for Marketing channels")
plt.grid(True, linewidth=1, color='r', linestyle='-.')



plt.show()