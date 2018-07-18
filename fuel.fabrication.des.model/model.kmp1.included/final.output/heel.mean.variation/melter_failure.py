# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:33:51 2017
@author: Jieun


"""


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import os

os.chdir(os.getcwd() + "/mean.250")


melter_failure = []
operation_time = []

 
# 250 g

with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure.append(float(data[6]))
        operation_time.append(float(data[1]))
        
#print melter_failure
#print operation_time
        
#print len(melter_failure)
#print len(operation_time)

    
#print melter_failure_probability


# calculate the average
sum0 = 0.0
for i in range(0,1000):
    sum0 = sum0 + melter_failure[i]
ave0 = sum0/1000.

# calculate the standard deviation 
std0 = np.std(melter_failure)




# 150 g 
os.chdir("./../mean.150")


melter_failure1 = []
operation_time1 = []

# import data file
with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure1.append(float(data[6]))
        operation_time1.append(float(data[1]))
        
#print melter_failure1
#print operation_time1
        
#print len(melter_failure1)
#print len(operation_time1)

   
#print melter_failure_probability1


# calculate the average
sum1 = 0.0
for i in range(0,1000):
    sum1 = sum1 + melter_failure1[i]
ave1 = sum1/1000.

# calculate the standard deviation 
std1 = np.std(melter_failure1)



# 300 g 
os.chdir("./../mean.300")

melter_failure2 = []
operation_time2 = []

# import data file
with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure2.append(float(data[6]))
        operation_time2.append(float(data[1]))
        
#print melter_failure2
#print operation_time2
        
#print len(melter_failure2)
#print len(operation_time2)


#print melter_failure_probability2


# calculate the average
sum2 = 0.0
for i in range(0,1000):
    sum2 = sum2 + melter_failure2[i]
ave2 = sum2/1000.

# calculate the standard deviation 
std2 = np.std(melter_failure2)



# create the histogram with error bars
bar_width = 0.0061 
opacity = 0.4 
error_config = {'ecolor':'0.3'}


y = [ave1, ave0, ave2]
x = [1 + bar_width*1.3, 1 + bar_width*2.5, 1 + bar_width*3.7]

print ave1, std1
print ave0, std0
print ave2, std2

results1 = plt.bar(1 + bar_width*1.3, ave1, bar_width, alpha = opacity, color ='dodgerblue', yerr = std1, error_kw = error_config, capsize = 4)
results = plt.bar(1 + bar_width*2.5, ave0, bar_width, alpha = opacity, color ='dodgerblue', yerr = std0, error_kw = error_config)
results2 = plt.bar(1 + bar_width*3.7, ave2, bar_width, alpha = opacity, color ='dodgerblue', yerr = std2, error_kw = error_config)


os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel(' 150       250         300\n'  + 'Heel mean (g)')
plt.ylabel('# of melter failure')

plt.axis([0.99,1.04, 0.00, 60])
#plt.legend(handles=[results, results1])
plt.savefig('Melterfailure.png')
plt.show()

