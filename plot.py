import numpy as np
import matplotlib.pyplot as plt

# open file & read

fin = open('shoshone.gpx')

for i in range(8):
    fin.readline()

bounds = str(fin.readline()).strip(' <bounds').split()
minlat = float(bounds[0].strip('minlat="'))
minlon = float(bounds[1].strip('minlo="'))
maxlat = float(bounds[2].strip('maxlt="'))
maxlon = float(bounds[3].strip('maxlon="/>'))

print(minlat,minlon,maxlat,maxlon)

# get every points in an ndarray

fin.close()

# create an array that every row is a point
