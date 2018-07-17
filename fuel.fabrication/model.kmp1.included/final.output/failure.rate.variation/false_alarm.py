# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:00:05 2017
@author: Jieun

This is for executing the false alarm probability for each kmp.

"""
# 1/30 days 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

os.chdir(os.getcwd() + "/1000.test.runs.with.kmp1.failure.rate.one.30days")
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

# results1 = plt.bar(1 +bar_width*8, ave_1, bar_width, alpha = opacity, color ='b', yerr = std_1, error_kw = error_config, label='KMP1', capsize = 4)
# results2 = plt.bar(1 +bar_width*9, ave_2, bar_width, alpha = opacity, color ='r', yerr = std_2, error_kw = error_config, label='KMP2')
results3 = plt.bar(1 +bar_width*8, ave_3, bar_width, alpha = opacity, color ='orange', yerr = std_3, error_kw = error_config, label='KMP3', capsize = 4)
# results = plt.bar(1 +bar_width*11, ave_total, bar_width, alpha = opacity, color ='g', yerr = std_total, error_kw = error_config, label='total')




# 1/ 20 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.20days')


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






# results1_1 = plt.bar(1 +bar_width*1, ave_1_1, bar_width, alpha = opacity, color ='b', yerr = std_1_1, error_kw = error_config, capsize = 4)
# results2_1 = plt.bar(1 +bar_width*2, ave_2_1, bar_width, alpha = opacity, color ='r', yerr = std_2_1, error_kw = error_config)
results3_1 = plt.bar(1 +bar_width*10, ave_3_1, bar_width, alpha = opacity, color ='orange', yerr = std_3_1, error_kw = error_config)
# results_1 = plt.bar(1 +bar_width*4, ave_total_1, bar_width, alpha = opacity, color ='g', yerr = std_total_1, error_kw = error_config)

# 1/ 40 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.40days')


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






# results1_2 = plt.bar(1 +bar_width*15, ave_1_2, bar_width, alpha = opacity, color ='b', yerr = std_1_2, error_kw = error_config, capsize = 4)
# results2_2 = plt.bar(1 +bar_width*16, ave_2_2, bar_width, alpha = opacity, color ='r', yerr = std_2_2, error_kw = error_config)
results3_2 = plt.bar(1 +bar_width*6, ave_3_2, bar_width, alpha = opacity, color ='orange', yerr = std_3_2, error_kw = error_config)
# results_2 = plt.bar(1 +bar_width*18, ave_total_2, bar_width, alpha = opacity, color ='g', yerr = std_total_2, error_kw = error_config)



# 1/ 60 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.60days')


false_alarm_1_3 = []
false_alarm_2_3 = []
false_alarm_3_3 = []
total_alarm_3 = []

total_check_1_3 = []
total_check_2_3 = []
total_check_3_3 = []
total_check_3 = []


with open('muf') as f:
    for line in f:
        data = line.split()
        total_check_3.append(int(data[1])) 
        total_check_1_3.append(int(data[2])) 
        total_check_2_3.append(int(data[3])) 
        total_check_3_3.append(int(data[4])) 
        
        false_alarm_1_3.append(int(data[5]))
        false_alarm_2_3.append(int(data[6]))
        false_alarm_3_3.append(int(data[7]))
        total_alarm_3.append(int(data[8]))


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





probability_1_3 = []
probability_2_3 = []
probability_3_3 = []
probability_total_3 = []


# probability 

for i in range(0, 1000):
    probability_1_3.append(float(false_alarm_1_3[i])/float(total_check_1_3[i]))
    probability_2_3.append(float(false_alarm_2_3[i])/float(total_check_2_3[i]))
    probability_3_3.append(float(false_alarm_3_3[i])/float(total_check_3_3[i]))
    probability_total_3.append(float(total_alarm_3[i])/float(total_check_3[i]))



# sum 
sum_1_3 = 0.0
sum_2_3 = 0.0
sum_3_3 = 0.0
sum_total_3 = 0.0
   
for j in range(0,1000):
    sum_1_3 = sum_1_3 + float(probability_1_3[j])
    sum_2_3 = sum_2_3 + float(probability_2_3[j])
    sum_3_3 = sum_3_3 + float(probability_3_3[j])
    sum_total_3 = sum_total_3 + float(probability_total_3[j])

ave_1_3 = sum_1_3/1000.
ave_2_3 = sum_2_3/1000.
ave_3_3 = sum_3_3/1000.
ave_total_3 = sum_total_3/1000.

print ave_1_3, ave_2_3, ave_3_3, ave_total_3


std_1_3 = np.std(probability_1_3)
std_2_3 = np.std(probability_2_3)
std_3_3 = np.std(probability_3_3)
std_total_3 = np.std(probability_total_3)


print std_1_3, std_2_3, std_3_3, std_total_3




# results1_3 = plt.bar(1 +bar_width*22, ave_1_3, bar_width, alpha = opacity, color ='b', yerr = std_1_3, error_kw = error_config, capsize = 4)
# results2_3 = plt.bar(1 +bar_width*23, ave_2_3, bar_width, alpha = opacity, color ='r', yerr = std_2_3, error_kw = error_config)
results3_3 = plt.bar(1 +bar_width*4, ave_3_3, bar_width, alpha = opacity, color ='orange', yerr = std_3_3, error_kw = error_config)
# results_3 = plt.bar(1 +bar_width*25, ave_total_3, bar_width, alpha = opacity, color ='g', yerr = std_total_3, error_kw = error_config)




# 1/ 90 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.90days')

false_alarm_1_4 = []
false_alarm_2_4 = []
false_alarm_3_4 = []
total_alarm_4 = []

total_check_1_4 = []
total_check_2_4 = []
total_check_3_4 = []
total_check_4 = []


with open('muf') as f:
    for line in f:
        data = line.split()
        total_check_4.append(int(data[1])) 
        total_check_1_4.append(int(data[2])) 
        total_check_2_4.append(int(data[3])) 
        total_check_3_4.append(int(data[4])) 
        
        false_alarm_1_4.append(int(data[5]))
        false_alarm_2_4.append(int(data[6]))
        false_alarm_3_4.append(int(data[7]))
        total_alarm_4.append(int(data[8]))


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





probability_1_4 = []
probability_2_4 = []
probability_3_4 = []
probability_total_4 = []


# probability 

for i in range(0, 1000):
    probability_1_4.append(float(false_alarm_1_4[i])/float(total_check_1_4[i]))
    probability_2_4.append(float(false_alarm_2_4[i])/float(total_check_2_4[i]))
    probability_3_4.append(float(false_alarm_3_4[i])/float(total_check_3_4[i]))
    probability_total_4.append(float(total_alarm_4[i])/float(total_check_4[i]))



# sum 
sum_1_4 = 0.0
sum_2_4 = 0.0
sum_3_4 = 0.0
sum_total_4 = 0.0
   
for j in range(0,1000):
    sum_1_4 = sum_1_4 + float(probability_1_4[j])
    sum_2_4 = sum_2_4 + float(probability_2_4[j])
    sum_3_4 = sum_3_4 + float(probability_3_4[j])
    sum_total_4 = sum_total_4 + float(probability_total_4[j])

ave_1_4 = sum_1_4/1000.
ave_2_4 = sum_2_4/1000.
ave_3_4 = sum_3_4/1000.
ave_total_4 = sum_total_4/1000.

print ave_1_4, ave_2_4, ave_3_4, ave_total_4


std_1_4 = np.std(probability_1_4)
std_2_4 = np.std(probability_2_4)
std_3_4 = np.std(probability_3_4)
std_total_4 = np.std(probability_total_4)


print std_1_4, std_2_4, std_3_4, std_total_4






# results1_4 = plt.bar(1 +bar_width*29, ave_1_4, bar_width, alpha = opacity, color ='b', yerr = std_1_4, error_kw = error_config, capsize = 4)
# results2_4 = plt.bar(1 +bar_width*30, ave_2_4, bar_width, alpha = opacity, color ='r', yerr = std_2_4, error_kw = error_config)
results3_4 = plt.bar(1 +bar_width*2, ave_3_4, bar_width, alpha = opacity, color ='orange', yerr = std_3_4, error_kw = error_config)
# results_4 = plt.bar(1 +bar_width*32, ave_total_4, bar_width, alpha = opacity, color ='g', yerr = std_total_4, error_kw = error_config)





# 1/ 180 days 
os.chdir('./../1000.test.runs.with.kmp1.failure.rate.one.180days')

false_alarm_1_5 = []
false_alarm_2_5 = []
false_alarm_3_5 = []
total_alarm_5 = []

total_check_1_5 = []
total_check_2_5 = []
total_check_3_5 = []
total_check_5 = []


with open('muf') as f:
    for line in f:
        data = line.split()
        total_check_5.append(int(data[1])) 
        total_check_1_5.append(int(data[2])) 
        total_check_2_5.append(int(data[3])) 
        total_check_3_5.append(int(data[4])) 
        
        false_alarm_1_5.append(int(data[5]))
        false_alarm_2_5.append(int(data[6]))
        false_alarm_3_5.append(int(data[7]))
        total_alarm_5.append(int(data[8]))


probability_1_5 = []
probability_2_5 = []
probability_3_5 = []
probability_total_5 = []


# probability 

for i in range(0, 1000):
    probability_1_5.append(float(false_alarm_1_5[i])/float(total_check_1_5[i]))
    probability_2_5.append(float(false_alarm_2_5[i])/float(total_check_2_5[i]))
    probability_3_5.append(float(false_alarm_3_5[i])/float(total_check_3_5[i]))
    probability_total_5.append(float(total_alarm_5[i])/float(total_check_5[i]))



# sum 
sum_1_5 = 0.0
sum_2_5 = 0.0
sum_3_5 = 0.0
sum_total_5 = 0.0
   
for j in range(0,1000):
    sum_1_5 = sum_1_5 + float(probability_1_5[j])
    sum_2_5 = sum_2_5 + float(probability_2_5[j])
    sum_3_5 = sum_3_5 + float(probability_3_5[j])
    sum_total_5 = sum_total_5 + float(probability_total_5[j])

ave_1_5 = sum_1_5/1000.
ave_2_5 = sum_2_5/1000.
ave_3_5 = sum_3_5/1000.
ave_total_5 = sum_total_5/1000.

print ave_1_5, ave_2_5, ave_3_5, ave_total_5


std_1_5 = np.std(probability_1_5)
std_2_5 = np.std(probability_2_5)
std_3_5 = np.std(probability_3_5)
std_total_5 = np.std(probability_total_5)


print std_1_5, std_2_5, std_3_5, std_total_5



# results1_5 = plt.bar(1 +bar_width*37, ave_1_5, bar_width, alpha = opacity, color ='b', yerr = std_1_5, error_kw = error_config, capsize = 4)
# results2_5 = plt.bar(1 +bar_width*38, ave_2_5, bar_width, alpha = opacity, color ='r', yerr = std_2_5, error_kw = error_config)
results3_5 = plt.bar(1, ave_3_5, bar_width, alpha = opacity, color ='orange', yerr = std_3_5, error_kw = error_config, capsize = 4)
# results_5 = plt.bar(1 +bar_width*40, ave_total_5, bar_width, alpha = opacity, color ='g', yerr = std_total_5, error_kw = error_config)

print "\n"


print std_3_5
print std_3_4
print std_3_3
print std_3_2
print std_3
print std_3_1



os.chdir('./../')

plt.xlabel('        1/180       1/90       1/60       1/40         1/30       1/20 \n'  + 'Failure rate (1/days)')
plt.ylabel('False alarm probability')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.axis([0.98,1.083, 0, 0.13])
plt.legend()
plt.savefig('FalseAlarm.png')
plt.show()


