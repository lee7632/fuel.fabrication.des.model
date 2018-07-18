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

os.chdir(os.getcwd() + "/mean.250")

attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
campaign = []

# 250 g 
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



# 150 g 
# 0.05
os.chdir("./../mean.150")


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
  

# 300 g 
os.chdir("./../mean.300")
campaign2 = []


with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign2.append(int(data[2])) 


#print len(campaign2)
#print campaign2 

sum2 = 0.0
for i in range(0, 1000):
    sum2 = sum2 + campaign2[i]
ave2 = sum2/1000.0
std2 = np.std(campaign2)


#print ave2, std2


y = [ave1, ave0, ave2]
x = [1 + bar_width*1.3, 1 + bar_width*2.5, 1 + bar_width*3.7]


bar_width = 0.0045 
#opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}


results1 = plt.bar(1 + bar_width*1.3, ave1, bar_width, alpha = opacity, color ='maroon', yerr = std1, error_kw = error_config, capsize = 4)
results = plt.bar(1 + bar_width*2.5, ave0, bar_width, alpha = opacity, color ='maroon', yerr = std0, error_kw = error_config)
results2 = plt.bar(1 + bar_width*3.7, ave2, bar_width, alpha = opacity, color ='maroon', yerr = std2, error_kw = error_config)



print "\n"



print ave1, std1
print ave0, std0
print ave2, std2


"""
print "\n"
print ave5 - ave4
print ave4 - ave3
print ave3 - ave2
print ave2 - ave0
print ave0 - ave1
"""
os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)

plt.xlabel('       150       250         300\n'  + 'Heel mean (g)')
plt.ylabel('Average Number of Campaigns (250 days)')
plt.axis([0.99,1.03, 240, 255])
#plt.legend()
plt.savefig('AverageCampaigns.png')


plt.show()