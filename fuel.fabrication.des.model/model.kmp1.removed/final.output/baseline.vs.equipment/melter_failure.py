# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:33:51 2017
@author: Jieun


"""


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

melter_failure = []
operation_time = []

os.chdir(os.getcwd() + "/baseline")
# 0.95
# import data file
with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure.append(float(data[6]))
        operation_time.append(float(data[1]))
        
#print melter_failure
#print operation_time
        
#print len(melter_failure)
#print len(operation_time)

"""    
# calculate the probability of melter failure   
melter_failure_probability = []
for i in range(0,1000):
    melter_failure_probability.append(float(melter_failure[i])/float(operation_time[i]))

#print melter_failure_probability

"""
# calculate the average
sum0 = 0.0
for i in range(0,1000):
    sum0 = sum0 + melter_failure[i]
ave0 = sum0/1000.

# calculate the standard deviation 
std0 = np.std(melter_failure)


# kmp1 removed
os.chdir("./../equipment")


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



print ave0, std0
print ave1, std1



# create the histogram with error bars
bar_width = 0.0061 
opacity = 0.4 
error_config = {'ecolor':'0.3'}


y = [ave0, ave1]
x = [1, 1 + bar_width*3]



results = plt.bar(1, ave0, bar_width, alpha = opacity, color ='b', yerr = std0, error_kw = error_config, label='alpha = 0.01', capsize = 4)
results1 = plt.bar(1 + bar_width*3, ave1, bar_width, alpha = opacity, color ='r', yerr = std1, error_kw = error_config, label='alpha = 0.02')
os.chdir('./../')



plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel('    Baseline design       Equipment design (KMP1 removed)')
 

plt.ylabel('# of melter failure')

plt.axis([0.99,1.03, 10, 40])
#plt.legend(handles=[results, results1])
plt.savefig('Melterfailure.png')

plt.show()



