# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 00:27:27 2021
SQLite + panda - https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.html
https://towardsdatascience.com/python-pandas-and-sqlite-a0e2c052456f

@author: Eilham
"""

import pandas as pd
from matplotlib import pyplot as plt
import sqlite3
plt.style.use('seaborn')     

#==============SQLITE setup/connection =======================================

# creating connection with existing table
conn = sqlite3.connect('test_9.db')



# creating panda dataFrame from table
df = pd.read_sql_query('SELECT * FROM SENSOR_TABLE', conn)

# taking column 'time, accel' from database and assigning it onto a variable
time = df['TIME']
accel_x = df['ACCEL_X']
accel_y = df['ACCEL_Y']
accel_z = df['ACCEL_Z']

# setting up subplots ( 3 rows and 1 column)
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 3 , ncols = 1)



# i added something here


# plotting the points and adding artistic stuff
ax1.plot(time, accel_x, color='b', linewidth = 1, label= 'x-axis')
ax2.plot(time, accel_y, color='g', linewidth = 1, label = 'y-axis')
ax3.plot(time, accel_z, color='r', linewidth = 1, label = 'z-axis')

#===========SUBPLOT #1 ====================================================

# enabling legends
ax1.legend()


# label x and y axis
ax1.set_xlabel('Time (hh:mm:ss)')
ax1.set_ylabel('Accelerometer')

# put the title
ax1.set_title('Accelerometer Readings')

#===========SUBPLOT #2 ====================================================
# enabling legends
ax2.legend()


# label x and y axis
ax2.set_xlabel('Time (hh:mm:ss)')
ax2.set_ylabel('Accelerometer')

# put the title
ax2.set_title('Accelerometer Readings')

#===========SUBPLOT #3 ====================================================
# enabling legends
ax3.legend()


# label x and y axis
ax3.set_xlabel('Time (hh:mm:ss)')
ax3.set_ylabel('Accelerometer')

# put the title
ax3.set_title('Accelerometer Readings')




# enable grid (altho seaborn dah ada grid)
#plt.grid(True)

# tight layout to keep the shape consistent
plt.tight_layout()

# actually show the plot on the screen
plt.show()

# close the opened connection
conn.close()