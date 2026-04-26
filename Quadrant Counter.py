from math import sqrt
import matplotlib.pyplot as plt
import seaborn as sns
#import csv and count number of pixels in each quadrant 

WT_data = ["1411_closedtracks.csv", "1440_closedtracks.csv", "1507_closedtracks.csv", "1541_closedtracks.csv", "1608_closedtracks.csv", "1637_closedtracks.csv", "1705_closedtracks.csv"]
alx = []
aly = []

for file in WT_data:
    
    data = open(file, "r")

    #Create dictonary to store data
    #{track_ID: [TL, TR, BL, BR]}
    
    allx = []
    ally = []

    #iterate through each line in file
    for line in data:
        if line[0:2] == "ID":
            row_list = line.split(",")
        
            track_ID = row_list[2]
        
            
            x, y = float(row_list[4]), float(row_list[5])
            alx.append(x)
            aly.append(y)
        
    data.close()
#print(quad)

plt.hist2d(alx, aly, bins = 40)
plt.ylim(max(aly), min(aly))
plt.legend
plt.title("WILD TYPE HEAT MAP",fontsize = 13, fontweight = "bold")
plt.show()

PPK_data = ["1520_closedtracks.csv", "1426_closedtracks.csv", "1454_closedtracks.csv", "1554_closedtracks.csv", "1621_closedtracks.csv", "1651_closedtracks.csv", "1719_closedtracks.csv"]
allx = []
ally = []

for file in PPK_data:
    
    data = open(file, "r")

    #Create dictonary to store data
    #{track_ID: [TL, TR, BL, BR]}
    
    allx = []
    ally = []

    #iterate through each line in file
    for line in data:
        if line[0:2] == "ID":
            row_list = line.split(",")
        
            track_ID = row_list[2]
        
            
            x, y = float(row_list[4]), float(row_list[5])
            allx.append(x)
            ally.append(y)
        
    data.close()
#print(quad)

plt.hist2d(allx, ally, bins = 40)
plt.ylim(max(ally), min(ally))
plt.title("PPK HEAT MAP",fontsize = 13, fontweight = "bold")
plt.legend
plt.show()


        
        
    #track ID is 3rd column
    #x is 5th column
    #y is 6th column

