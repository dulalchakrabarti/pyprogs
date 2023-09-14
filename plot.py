import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('marine.csv')

fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(df['Date/Time'], df['Surface Wind Spd [m/s]'],'bo-')
ax1.set_xticklabels(df['Date/Time'],rotation = 90)

ax1.set_xlim(0, 20)
ax1.set_xlabel("Date/Time")
ax1.set_ylabel("Wind Speed(blue)(m/s)/Gust(red)(m/s)")

ax2 = ax1.twiny()
ax2.set_xlabel("Wind Direction(Deg)")
ax2.set_xlim(0, len(df['Surface Wind Dir']))
ax2.plot(range(len(df['Surface Wind Dir'])),df['Surface wind Gust [m/s]'],'ro-')
ax2.set_xticks(range(len(df['Surface Wind Dir'])))
ax2.set_xticklabels(df['Surface Wind Dir'],rotation = 90)
plt.tight_layout()
plt.savefig('wind.png')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.plot(df['Date/Time'], df['Combined(swell+wind)Wave Height(m)'],'ro-')
ax1.set_xticklabels(df['Date/Time'],rotation = 90)

ax1.set_xlim(0, 20)
ax1.set_xlabel("Date/Time")
ax1.set_ylabel("Combined(swell+wind)Wave Height(m)")

ax2 = ax1.twiny()
ax2.set_xlabel("Primary Swell Direction(Deg)")
ax2.set_xlim(0, len(df['Combined(swell+wind)Wave Height(m)']))
#ax2.plot(range(len(df['htsgwsfc'])),df['Surface wind Gust [m/s]'],'ro-')
ax2.set_xticks(range(len(df['Swell Dir(Deg)'])))
ax2.set_xticklabels(df['Swell Dir(Deg)'],rotation = 90)
plt.tight_layout()
plt.savefig('wave.png')
plt.show()

'''

ax1 = df['Surface Wind Spd [m/s]'].plot(xticks=df.index, rot=90,style='b-o')
ax1.set_xticklabels(df['Date/Time'])
plt.tick_params(labeltop=True)
ax2 = df['Surface wind Gust [m/s]'].plot(xticks=df.index, rot=90,style='r-o')
ax2.set_xticklabels(df['Surface Wind Dir'])
plt.show()
plt.xlabel('Forecast Hours/6')
plt.ylabel('Wave Height(m)')
plt.title('Maximum Wave Height(m)')
plt.grid(True)
plt.plot(pd['htsgwsfc'])
plt.savefig("wave.png")

plt.xlabel('Forecast Hours/6')
plt.ylabel('Wind Dir(Deg)')
plt.title('Wind Direction')
plt.grid(True)
plt.plot(pd['wdirsfc'])
plt.savefig("wdir.png")
plt.show()

plt.xlabel('Forecast Hours/6')
plt.ylabel('Wind Speed(m/s)')
plt.title('Wind Speed')
plt.grid(True)
plt.plot(pd['windsfc'])
plt.savefig("ws.png")
plt.show()
'''
