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


os.chdir(os.getcwd() + "/alpha.0.05.measurement.error.percent.0.05")

melter_failure = []
operation_time = []

# 0.05%
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




#measurement 0.1 %
os.chdir(os.getcwd() + "/../different.false.alarm.probability.measurement.error.percent.0.1")

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




# create the histogram with error bars
bar_width = 0.0061 
opacity = 0.4 
error_config = {'ecolor':'0.3'}


y = [ave0, ave1]
x = [1 + bar_width*1.3, 1 + bar_width*2.5]

results = plt.bar(1 + bar_width*1.3, ave0, bar_width, alpha = opacity, color ='dodgerblue', yerr = std0, error_kw = error_config, capsize = 4)
results1 = plt.bar(1 + bar_width*2.5, ave1, bar_width, alpha = opacity, color ='dodgerblue', yerr = std1, error_kw = error_config)
print ave0, std0
print ave1, std1


os.chdir('./../')
plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel('0.05           0.1         \n'  + 'Relative random, or systematic error (%)')
plt.ylabel('# of melter failure')

plt.axis([0.988,1.04, 0.00, 60])
#plt.legend(handles=[results, results1])
plt.savefig('Melterfailure.png')
plt.show()

