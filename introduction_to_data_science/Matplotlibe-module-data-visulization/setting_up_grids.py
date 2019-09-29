import matplotlib.pyplot as plt 


#the veiws got on a post in last seven days on different platform
y_views = [534,689,258,401,724,689,350]
f_views = [123,342,700,304,405,650,325]
t_views = [202,209,176,415,824,389,550]
days = range(1,8)

plt.plot(days, y_views, label="Youtube views",marker='o', markerfacecolor='b')
plt.plot(days, f_views, label="Facebook views",marker='o', markerfacecolor='y')
plt.plot(days, t_views, label="Twitter views",marker='o', markerfacecolor='g')

plt.xlabel("Day")
plt.ylabel("Views")
plt.legend(loc="lower right")
plt.title("Daily views for Marketing channels")
plt.grid(True, linewidth=1, color='g', linestyle='-.')
plt.xlim(1,5)
plt.ylim(100, 900)

plt.show()