import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]
#Plotting a bar graph of the viewers against games
plt.bar(range(len(games)), viewers, color = "slateblue")
#Making the graph more descriptive
plt.title("Game Viewers")
plt.legend(["Viewers"])
plt.xlabel("Game")
plt.ylabel("Number of Viewers")
ax = plt.subplot()
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games, rotation = 30)
plt.show()
plt.clf()
# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
#Creating an array of colors that will be applied to the pie chart
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
#Exploding the first slice
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#Drawing a pie chart of the countries where viewers of the League of Legends game are and making the graph more easier to understand and appealing
plt.pie(countries, colors = colors, explode = explode, shadow = True, startangle = 345, autopct = "%1.0f%%", pctdistance = 1.15)
plt.axis("equal")
plt.legend(labels)
plt.title("Viewers' Countries")
plt.show()
plt.clf()
# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
#Plotting a line graph of the viewers_hour
plt.plot(hour, viewers_hour)
plt.title("Viewing Hours")
plt.xlabel("Hours")
plt.ylabel("Number of Views")
plt.legend(["2015-01-01"])
ax1 = plt.subplot()
ax1.set_xticks(hour)
#Accounting for a 15% error in the data
y_upper = [1.15 * i for i in viewers_hour]
y_lower = [0.85 * i for i in viewers_hour]
plt.fill_between(hour, y_lower, y_upper, alpha = 0.2)
plt.show()
