# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:47:54 2017
@author: Jieun

This file is to calculate the average number of campaigns of 1000 simulation runs.  

"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os


attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
campaign = []

os.chdir(os.getcwd() + "/baseline")


# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        attempts.append(int(data[0]))
        campaign.append(int(data[2])) 

"""
print len(attempts)
print len(campaign)

print attempts 
print campaign 
"""
sum0 = 0.0
for i in range(0, 1000):
    sum0 = sum0 + campaign[i]
ave0 = sum0/1000.0
std0 = np.std(campaign)


print ave0, std0

# kmp1 removed
os.chdir("./../equipment")

campaign1 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign1.append(int(data[2])) 


#print len(campaign1)
#print campaign1 

sum1 = 0.0
for i in range(0, 1000):
    sum1 = sum1 + campaign1[i]
ave1 = sum1/1000.0
std1 = np.std(campaign1)


print ave1, std1
  

bar_width = 0.0045 

y = [ave0, ave1]
x = [1, 1 + bar_width*3]


#rint ave1 - ave0
opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}

results = plt.bar(1, ave0, bar_width, alpha = opacity, color ='b', yerr = std0, error_kw = error_config, capsize = 4)
results1 = plt.bar(1 + bar_width*3, ave1, bar_width, alpha = opacity, color ='r', yerr = std1, error_kw = error_config, label='alpha = 0.02')

print "\n"
os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)

plt.xlabel('           Baseline design       Equipment design (KMP1 removed)')
plt.ylabel('Average number of campaigns (250 days)')
plt.axis([0.99,1.025, 230, 260])
#plt.legend()
plt.savefig('AverageCampaigns.png')


plt.show()
