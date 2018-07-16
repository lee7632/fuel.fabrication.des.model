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

os.chdir(os.getcwd() + "/1000.test.runs.with.kmp1.failure.rate.one.30days")
attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
campaign = []

# 1/30
with open('final_output') as f:
    for line in f:
        data = line.split()
        attempts.append(int(data[0]))
        campaign.append(int(data[2])) 


print len(attempts)
print len(campaign)

print attempts 
print campaign 

sum0 = 0.0
for i in range(0, 1000):
    sum0 = sum0 + campaign[i]
ave0 = sum0/1000.0
std0 = np.std(campaign)


print ave0, std0



# 1/20 days
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.20days')


campaign1 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign1.append(int(data[2])) 


print len(campaign1)
print campaign1 

sum1 = 0.0
for i in range(0, 1000):
    sum1 = sum1 + campaign1[i]
ave1 = sum1/1000.0
std1 = np.std(campaign1)


print ave1, std1
  

# 1/ 40 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.40days')

campaign2 = []


with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign2.append(int(data[2])) 


print len(campaign2)
print campaign2 

sum2 = 0.0
for i in range(0, 1000):
    sum2 = sum2 + campaign2[i]
ave2 = sum2/1000.0
std2 = np.std(campaign2)


print ave2, std2


# 1/ 60 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.60days')


campaign3 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign3.append(int(data[2])) 


print len(campaign3)
print campaign3 

sum3 = 0.0
for i in range(0, 1000):
    sum3 = sum3 + campaign3[i]
ave3 = sum3/1000.0
std3 = np.std(campaign3)


print ave3, std3


# 1/ 90 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.90days')

campaign4 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign4.append(int(data[2])) 


print len(campaign4)
print campaign4 

sum4 = 0.0
for i in range(0, 1000):
    sum4 = sum4 + campaign4[i]
ave4 = sum4/1000.0
std4 = np.std(campaign4)


print ave4, std4



# 1/ 180 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.180days')

campaign5 = []


with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign5.append(int(data[2])) 


print len(campaign5)
print campaign5 

sum5 = 0.0
for i in range(0, 1000):
    sum5 = sum5 + campaign5[i]
ave5 = sum5/1000.0
std5 = np.std(campaign5)


print ave5, std5


y = [ave5, ave4, ave3, ave2, ave0, ave1]
x = [1, 1 + bar_width*1.5, 1 + bar_width*3, 1 + bar_width*4.5 , 1 + bar_width*6,  1 + bar_width*7.5]


bar_width = 0.0045 
#opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}


results5 = plt.bar(1, ave5, bar_width, alpha = opacity, color ='maroon', yerr = std5, error_kw = error_config, capsize = 4)
results4 = plt.bar(1 + bar_width*1.5, ave4, bar_width, alpha = opacity, color ='maroon', yerr = std4, error_kw = error_config)
results3 = plt.bar(1 + bar_width*3, ave3, bar_width, alpha = opacity, color ='maroon', yerr = std3, error_kw = error_config)
results2 = plt.bar(1 + bar_width*4.5, ave2, bar_width, alpha = opacity, color ='maroon', yerr = std2, error_kw = error_config)
results0 = plt.bar(1 + bar_width*6, ave0, bar_width, alpha = opacity, color ='maroon', yerr = std0, error_kw = error_config)
results1 = plt.bar(1 + bar_width*7.5, ave1, bar_width, alpha = opacity, color ='maroon', yerr = std1, error_kw = error_config, capsize = 4)


print "\n"

print ave5, std5
print ave4, std4
print ave3, std3
print ave2, std2
print ave0, std0
print ave1, std1


print "\n"
print ave5 - ave4
print ave4 - ave3
print ave3 - ave2
print ave2 - ave0
print ave0 - ave1

os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)

plt.xlabel('       1/180      1/90        1/60       1/40      1/30       1/20 \n'  + 'Failure rate (1/days)')
plt.ylabel('Average number of campaigns (250 days)')
plt.axis([0.99,1.04, 230, 270])
#plt.legend()
plt.savefig('AverageCampaigns.png')


plt.show()