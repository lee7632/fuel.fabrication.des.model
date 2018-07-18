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

os.chdir(os.getcwd() + "/1000.test.runs.with.kmp1.one.minus.alpha.0.95")

attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
campaign = []

# 0.95 (1- alpha)
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


# 0.9 (1-alpha)
os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.90")

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


#print ave1, std1
  

# 0.98 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.98")

campaign2 = []

# 0.95 (1- alpha)
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

# 0.99 (1- alpha) 

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.99")

campaign3 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign3.append(int(data[2])) 


#print len(campaign3)
#print campaign3 

sum3 = 0.0
for i in range(0, 1000):
    sum3 = sum3 + campaign3[i]
ave3 = sum3/1000.0
std3 = np.std(campaign3)


#print ave3, std3

#0.925 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.925")

campaign4 = []

# 0.95 (1- alpha)
with open('final_output') as f:
    for line in f:
        data = line.split()
        campaign4.append(int(data[2])) 


#print len(campaign4)
#print campaign4 

sum4 = 0.0
for i in range(0, 1000):
    sum4 = sum4 + campaign4[i]
ave4 = sum4/1000.0
std4 = np.std(campaign4)


#print ave4, std4


y = [ave3, ave2, ave0, ave4, ave1]
x = [1, 1 + bar_width*1.5, 1 + bar_width*3, 1 + bar_width*4.5 , 1 + bar_width*6]


bar_width = 0.0045 
#opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}


results3 = plt.bar(1, ave3, bar_width, alpha = opacity, color ='maroon', yerr = std3, error_kw = error_config, label='alpha = 0.01', capsize = 4)
results2 = plt.bar(1 + bar_width*1.5, ave2, bar_width, alpha = opacity, color ='maroon', yerr = std2, error_kw = error_config, label='alpha = 0.02')
results = plt.bar(1 + bar_width*3, ave0, bar_width, alpha = opacity, color ='maroon', yerr = std0, error_kw = error_config, label='alpha = 0.05')
results4 = plt.bar(1 + bar_width*4.5, ave4, bar_width, alpha = opacity, color ='maroon', yerr = std4, error_kw = error_config, label='alpha = 0.075')
results1 = plt.bar(1 + bar_width*6, ave1, bar_width, alpha = opacity, color ='maroon', yerr = std1, error_kw = error_config, label='alpha = 0.1')

print "\n"

print ave3, std3
print ave2, std2
print ave0, std0
print ave4, std4
print ave1, std1

os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')

plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)

plt.xlabel('    0.01         0.02         0.05        0.075         0.1\n'  + r'False alarm probability ($\alpha$)')
plt.ylabel('Average number of campaigns (250 days)')
plt.axis([0.99,1.035, 230, 270])
#plt.legend()
plt.savefig('AverageCampaigns.png')


plt.show()