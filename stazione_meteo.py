#Code written by Antonio Nirta

import pandas as pd
import matplotlib.pyplot as plt
import math

#import csv file. "LOG(5).csv" is the name of file
db = pd.read_csv("feed.csv")

#Variables with accelerations 
Temperature= db.iloc[:,2]
Humidity= db.iloc[:,3]
Pressure= db.iloc[:,4]

#Time settings
time = db.iloc[:0]     #time in milliseconds, give by arduino

#tempo = [i/1000 for i in time]      #time in seconds

#Pressione= []

#for i in Pressure:
    #Pressione.append(int(i))


#print(Pressione)
    


plt.subplot(3, 1, 1)
plt.plot(time, Temperature, '-', linewidth=0.8)
plt.title('Meteo San Luca')
plt.ylabel('Umidità (%)')

plt.subplot(3, 1, 2)
plt.plot(time, Humidity, '-', color='red', linewidth=0.8)
plt.xlabel('time (s)')
plt.ylabel('Temperatura')

plt.subplot(3, 1, 3)
plt.plot(time, Pressione, '-', color='green', linewidth=0.8)
plt.xlabel('time (s)')
plt.ylabel('P. atmosferica')

plt.show()


# Axis' name
plt.xlabel('Tempo (s)')        



#Show graph
plt.show()


