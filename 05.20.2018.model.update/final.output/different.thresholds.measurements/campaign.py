# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:47:54 2017
@author: Jieun

This file is to calculate the average number of campaigns of 1000 simulation runs.  

"""

# measurement 0.05%

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os


attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
campaign = []

os.chdir(os.getcwd() + "/alpha.0.05.measurement.error.percent.0.05")

with open('final_output') as f:
    for line in f:
        data = line.split()
        attempts.append(int(data[0]))
        campaign.append(int(data[2])) 


#print len(attempts)
#print len(campaign)

#print attempts 
#print campaign 

sum0 = 0.0
for i in range(0, 1000):
    sum0 = sum0 + campaign[i]
ave0 = sum0/1000.0
std0 = np.std(campaign)


#print ave0, std0



# measurement 0.1 %
os.chdir(os.getcwd() + "/../different.false.alarm.probability.measurement.error.percent.0.1")


campaign1 = []

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


#print ave1, std1
  


bar_width = 0.0045 
opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}

y = [ave0, ave1]
x = [1 + bar_width*1.3, 1 + bar_width*2.5]

results = plt.bar(1 + bar_width*1.3, ave0, bar_width, alpha = opacity, color ='maroon', yerr = std0, error_kw = error_config, capsize = 4)
results1 = plt.bar(1 + bar_width*2.5, ave1, bar_width, alpha = opacity, color ='maroon', yerr = std1, error_kw = error_config)

print "\n"


print ave0, std0
print ave1, std1

os.chdir('./../')


"""
print "\n"
print ave5 - ave4
print ave4 - ave3
print ave3 - ave2
print ave2 - ave0
print ave0 - ave1
"""

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)

plt.xlabel('  0.05       0.1         \n'  + 'Relative random, or systematic error (%)')
plt.ylabel('Average number of campaigns (250 days)')
plt.axis([0.99,1.03, 230, 300])
#plt.legend()
plt.savefig('AverageCampaigns.png')
plt.show()


