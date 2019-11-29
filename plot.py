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

## distance

d = []
for i in range(1,amount):
    d.append( np.sqrt((tracks[i,0]-tracks[i-1,0])**2 + (tracks[i,1]-tracks[i-1,1])**2 + (tracks[i,2]-tracks[i-1,2])**2 ) )
dis = np.array(d)

## plot locations

plt.scatter(tracks[:,1],tracks[:,0],c=tracks[:,2],s=5)

plt.xlabel('longtitude',fontsize = 15)
plt.ylabel('lattitude',fontsize = 15)
plt.title('Shoshone',fontsize = 20)
plt.axis('equal')

plt.colorbar()

## plot moving direction

arrow = tracks[::100,:2]
arrow[:,0] += 0.01

for i in range(2,amount//100,2):
    plt.annotate('', xy=(arrow[i,1],arrow[i,0]), xytext=(arrow[i-1,1],arrow[i-1,0]),arrowprops=dict(facecolor='none',shrink=0.05))

## show figure

plt.show()

