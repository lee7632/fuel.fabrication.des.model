# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:00:05 2017
@author: Jieun

This is for executing the false alarm probability for each kmp.

"""
# 250 g 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt



os.chdir(os.getcwd() + "/mean.250")

attempts = []

false_alarm_1 = []
false_alarm_2 = []
false_alarm_3 = []
total_alarm = []

total_check_1 = []
total_check_2 = []
total_check_3 = []
total_check = []


with open('muf') as f:
    for line in f:
        data = line.split()
        attempts.append(int(data[0]))
        total_check.append(int(data[1])) 
        total_check_1.append(int(data[2])) 
        total_check_2.append(int(data[3])) 
        total_check_3.append(int(data[4])) 
        
        false_alarm_1.append(int(data[5]))
        false_alarm_2.append(int(data[6]))
        false_alarm_3.append(int(data[7]))
        total_alarm.append(int(data[8]))



#print total_check_1
#print len(total_check_1)

#print total_check_2 
#print len(total_check_2)

#print total_check_3
#print len(total_check_3) 
       
#print total_check
#print len(total_check)

#print false_alarm_1
#print len(false_alarm_1)

#print false_alarm_2
#print len(false_alarm_2)

#print false_alarm_3
#print len(false_alarm_3)

#print total_alarm
#print len(total_alarm)



probability_1 = []
probability_2 = []
probability_3 = []
probability_total = []


# probability 

for i in range(0, 1000):
    probability_1.append(float(false_alarm_1[i])/float(total_check_1[i]))
    probability_2.append(float(false_alarm_2[i])/float(total_check_2[i]))
    probability_3.append(float(false_alarm_3[i])/float(total_check_3[i]))
    probability_total.append(float(total_alarm[i])/float(total_check[i]))



# sum 
sum_1 = 0.0
sum_2 = 0.0
sum_3 = 0.0
sum_total = 0.0
   
for j in range(0,1000):
    sum_1 = sum_1 + float(probability_1[j])
    sum_2 = sum_2 + float(probability_2[j])
    sum_3 = sum_3 + float(probability_3[j])
    sum_total = sum_total + float(probability_total[j])

ave_1 = sum_1/1000.
ave_2 = sum_2/1000.
ave_3 = sum_3/1000.
ave_total = sum_total/1000.

print ave_1, ave_2, ave_3, ave_total


std_1 = np.std(probability_1)
std_2 = np.std(probability_2)
std_3 = np.std(probability_3)
std_total = np.std(probability_total)


print std_1, std_2, std_3, std_total


bar_width = 0.007 
opacity = 0.4 
#index = np_groups  
error_config = {'ecolor':'0.3'}

results1 = plt.bar(1 +bar_width*8, ave_1, bar_width, alpha = opacity, color ='b', yerr = std_1, error_kw = error_config, label='KMP1', capsize = 4)
results2 = plt.bar(1 +bar_width*9, ave_2, bar_width, alpha = opacity, color ='r', yerr = std_2, error_kw = error_config, label='KMP2')
results3 = plt.bar(1 +bar_width*10, ave_3, bar_width, alpha = opacity, color ='orange', yerr = std_3, error_kw = error_config, label='KMP3', capsize = 4)
results = plt.bar(1 +bar_width*11, ave_total, bar_width, alpha = opacity, color ='g', yerr = std_total, error_kw = error_config, label='total')






# 150 g 
os.chdir("./../mean.150")




false_alarm_1_1 = []
false_alarm_2_1 = []
false_alarm_3_1 = []
total_alarm_1 = []

total_check_1_1 = []
total_check_2_1 = []
total_check_3_1 = []
total_check_1 = []


with open('muf') as f:
    for line in f:
        data = line.split()
        total_check_1.append(int(data[1])) 
        total_check_1_1.append(int(data[2])) 
        total_check_2_1.append(int(data[3])) 
        total_check_3_1.append(int(data[4])) 
        
        false_alarm_1_1.append(int(data[5]))
        false_alarm_2_1.append(int(data[6]))
        false_alarm_3_1.append(int(data[7]))
        total_alarm_1.append(int(data[8]))


#print total_check_1_1
#print len(total_check_1_1)

#print total_check_2_1 
#print len(total_check_2_1)

#print total_check_3_1
#print len(total_check_3_1) 
       
#print total_check_1
#print len(total_check_1)

#print false_alarm_1_1
#print len(false_alarm_1_1)

#print false_alarm_2_1
#print len(false_alarm_2_1)

#print false_alarm_3_1
#print len(false_alarm_3_1)

#print total_alarm_1
#print len(total_alarm_1)





probability_1_1 = []
probability_2_1 = []
probability_3_1 = []
probability_total_1 = []


# probability 

for i in range(0, 1000):
    probability_1_1.append(float(false_alarm_1_1[i])/float(total_check_1_1[i]))
    probability_2_1.append(float(false_alarm_2_1[i])/float(total_check_2_1[i]))
    probability_3_1.append(float(false_alarm_3_1[i])/float(total_check_3_1[i]))
    probability_total_1.append(float(total_alarm_1[i])/float(total_check_1[i]))



# sum 
sum_1_1 = 0.0
sum_2_1 = 0.0
sum_3_1 = 0.0
sum_total_1 = 0.0
   
for j in range(0,1000):
    sum_1_1 = sum_1_1 + float(probability_1_1[j])
    sum_2_1 = sum_2_1 + float(probability_2_1[j])
    sum_3_1 = sum_3_1 + float(probability_3_1[j])
    sum_total_1 = sum_total_1 + float(probability_total_1[j])

ave_1_1 = sum_1_1/1000.
ave_2_1 = sum_2_1/1000.
ave_3_1 = sum_3_1/1000.
ave_total_1 = sum_total_1/1000.

print ave_1_1, ave_2_1, ave_3_1, ave_total_1


std_1_1 = np.std(probability_1_1)
std_2_1 = np.std(probability_2_1)
std_3_1 = np.std(probability_3_1)
std_total_1 = np.std(probability_total_1)


print std_1_1, std_2_1, std_3_1, std_total_1






results1_1 = plt.bar(1 +bar_width*1, ave_1_1, bar_width, alpha = opacity, color ='b', yerr = std_1_1, error_kw = error_config, capsize = 4)
results2_1 = plt.bar(1 +bar_width*2, ave_2_1, bar_width, alpha = opacity, color ='r', yerr = std_2_1, error_kw = error_config)
results3_1 = plt.bar(1 +bar_width*3, ave_3_1, bar_width, alpha = opacity, color ='orange', yerr = std_3_1, error_kw = error_config)
results_1 = plt.bar(1 +bar_width*4, ave_total_1, bar_width, alpha = opacity, color ='g', yerr = std_total_1, error_kw = error_config)



# 300 g 
os.chdir("./../mean.300")

false_alarm_1_2 = []
false_alarm_2_2 = []
false_alarm_3_2 = []
total_alarm_2 = []

total_check_1_2 = []
total_check_2_2 = []
total_check_3_2 = []
total_check_2 = []


with open('muf') as f:
    for line in f:
        data = line.split()
        total_check_2.append(int(data[1])) 
        total_check_1_2.append(int(data[2])) 
        total_check_2_2.append(int(data[3])) 
        total_check_3_2.append(int(data[4])) 
        
        false_alarm_1_2.append(int(data[5]))
        false_alarm_2_2.append(int(data[6]))
        false_alarm_3_2.append(int(data[7]))
        total_alarm_2.append(int(data[8]))


#print total_check_1_1
#print len(total_check_1_1)

#print total_check_2_1 
#print len(total_check_2_1)

#print total_check_3_1
#print len(total_check_3_1) 
       
#print total_check_1
#print len(total_check_1)

#print false_alarm_1_1
#print len(false_alarm_1_1)

#print false_alarm_2_1
#print len(false_alarm_2_1)

#print false_alarm_3_1
#print len(false_alarm_3_1)

#print total_alarm_1
#print len(total_alarm_1)





probability_1_2 = []
probability_2_2 = []
probability_3_2 = []
probability_total_2 = []


# probability 

for i in range(0, 1000):
    probability_1_2.append(float(false_alarm_1_2[i])/float(total_check_1_2[i]))
    probability_2_2.append(float(false_alarm_2_2[i])/float(total_check_2_2[i]))
    probability_3_2.append(float(false_alarm_3_2[i])/float(total_check_3_2[i]))
    probability_total_2.append(float(total_alarm_2[i])/float(total_check_2[i]))



# sum 
sum_1_2 = 0.0
sum_2_2 = 0.0
sum_3_2 = 0.0
sum_total_2 = 0.0
   
for j in range(0,1000):
    sum_1_2 = sum_1_2 + float(probability_1_2[j])
    sum_2_2 = sum_2_2 + float(probability_2_2[j])
    sum_3_2 = sum_3_2 + float(probability_3_2[j])
    sum_total_2 = sum_total_2 + float(probability_total_2[j])

ave_1_2 = sum_1_2/1000.
ave_2_2 = sum_2_2/1000.
ave_3_2 = sum_3_2/1000.
ave_total_2 = sum_total_2/1000.

print ave_1_2, ave_2_2, ave_3_2, ave_total_2


std_1_2 = np.std(probability_1_2)
std_2_2 = np.std(probability_2_2)
std_3_2 = np.std(probability_3_2)
std_total_2 = np.std(probability_total_2)


print std_1_2, std_2_2, std_3_2, std_total_2



results1_2 = plt.bar(1 +bar_width*15, ave_1_2, bar_width, alpha = opacity, color ='b', yerr = std_1_2, error_kw = error_config, capsize = 4)
results2_2 = plt.bar(1 +bar_width*16, ave_2_2, bar_width, alpha = opacity, color ='r', yerr = std_2_2, error_kw = error_config)
results3_2 = plt.bar(1 +bar_width*17, ave_3_2, bar_width, alpha = opacity, color ='orange', yerr = std_3_2, error_kw = error_config)
results_2 = plt.bar(1 +bar_width*18, ave_total_2, bar_width, alpha = opacity, color ='g', yerr = std_total_2, error_kw = error_config)



print "\n"


os.chdir('./../')

plt.xlabel('       150       250         300\n'  + 'Heel mean (g)')
plt.ylabel('False alarm probability')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.axis([0.97,1.15, 0, 0.13])
plt.legend()
plt.savefig('FalseAlarm.png')
plt.show()


