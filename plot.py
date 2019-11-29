import numpy as np
import matplotlib.pyplot as plt

## open file & read

fin = open('shoshone.gpx')

for i in range(8):
    fin.readline()

bounds = str(fin.readline()).strip(' <bounds').split()
minlat = float(bounds[0].strip('minlat="'))
minlon = float(bounds[1].strip('minlo="'))
maxlat = float(bounds[2].strip('maxlt="'))
maxlon = float(bounds[3].strip('maxlon="/>'))

#print(minlat,minlon,maxlat,maxlon)

## get every points in a list, then ndarray

for i in range(6):
    fin.readline()

tracks_list = []
amount = 0
while True:
    hrzt_line = fin.readline()
    if hrzt_line.strip() == '</trkseg>': break

    hrzt_list = hrzt_line.strip('<> trkpt\n').split()
    #print(hrzt_list)
    tracks_list.append( float(hrzt_list[0].strip('lat="')) )
    tracks_list.append( float(hrzt_list[1].strip('lon="')) )

    ele_line = fin.readline().strip('<el>/ \n')
    tracks_list.append( float(ele_line) )

    fin.readline()
    
    amount += 1

#for i in range(3):
   # print(tracks_list[i])

tracks = np.array(tracks_list).reshape(amount,3)

#for i in range(6):
#    print(tracks[i])

#print(tracks[3,1])

fin.close()

## plot locations

plt.scatter(tracks[:,1],tracks[:,0],c=tracks[:,2],s=5)

plt.xlabel('longtitude',fontsize = 15)
plt.ylabel('lattitude',fontsize = 15)
plt.title('Shoshone',fontsize = 20)
plt.axis('equal')


plt.colorbar()

plt.show()
