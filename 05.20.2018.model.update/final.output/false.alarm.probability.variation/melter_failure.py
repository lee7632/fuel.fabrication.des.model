# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 10:33:51 2017
@author: Jieun


"""


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

os.chdir(os.getcwd() + "/1000.test.runs.with.kmp1.one.minus.alpha.0.95")

melter_failure = []
operation_time = []

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



# 0.9 (1-alpha)
os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.90")

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



# 0.98 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.98")


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

   


# calculate the average
sum2 = 0.0
for i in range(0,1000):
    sum2 = sum2 + melter_failure2[i]
ave2 = sum2/1000.

# calculate the standard deviation 
std2 = np.std(melter_failure2)




# 0.99 (1- alpha) 

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.99")


melter_failure3 = []
operation_time3 = []

# import data file
with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure3.append(float(data[6]))
        operation_time3.append(float(data[1]))
        
#print melter_failure3
#print operation_time3
        
#print len(melter_failure3)
#print len(operation_time3)

    

#print melter_failure_probability3


# calculate the average
sum3 = 0.0
for i in range(0,1000):
    sum3 = sum3 + melter_failure3[i]
ave3 = sum3/1000.

# calculate the standard deviation 
std3 = np.std(melter_failure3)


#0.925 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.925")



melter_failure4 = []
operation_time4 = []

# import data file
with open('melter_failure') as f:
    for line in f:
        data = line.split()
        melter_failure4.append(float(data[6]))
        operation_time4.append(float(data[1]))
        
#print melter_failure4
#print operation_time4
        
#print len(melter_failure4)
#print len(operation_time4)

  


# calculate the average
sum4 = 0.0
for i in range(0,1000):
    sum4 = sum4 + melter_failure4[i]
ave4 = sum4/1000.

# calculate the standard deviation 
std4 = np.std(melter_failure4)





# create the histogram with error bars
bar_width = 0.0061 
opacity = 0.4 
error_config = {'ecolor':'0.3'}


y = [ave3, ave2, ave0, ave4, ave1]
x = [1, 1 + bar_width*1.5, 1 + bar_width*3, 1 + bar_width*4.5 , 1 + bar_width*6]



results3 = plt.bar(1, ave3, bar_width, alpha = opacity, color ='dodgerblue', yerr = std3, error_kw = error_config, label='alpha = 0.01', capsize = 4)
results2 = plt.bar(1 + bar_width*1.5, ave2, bar_width, alpha = opacity, color ='dodgerblue', yerr = std2, error_kw = error_config, label='alpha = 0.02')
results = plt.bar(1 + bar_width*3, ave0, bar_width, alpha = opacity, color ='dodgerblue', yerr = std0, error_kw = error_config, label='alpha = 0.05')
results4 = plt.bar(1 + bar_width*4.5, ave4, bar_width, alpha = opacity, color ='dodgerblue', yerr = std4, error_kw = error_config, label='alpha = 0.075')
results1 = plt.bar(1 + bar_width*6, ave1, bar_width, alpha = opacity, color ='dodgerblue', yerr = std1, error_kw = error_config, label='alpha = 0.1')

os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel('  0.01           0.02           0.05          0.075          0.1\n'  + r'False alarm probability ($\alpha$)')
 

plt.ylabel('# of melter failure')

plt.axis([0.99,1.045, 10, 40])
#plt.legend(handles=[results, results1])
plt.savefig('Melterfailure.png')

plt.show()



print "\n"

print ave3, std3
print ave2, std2
print ave0, std0
print ave4, std4
print ave1, std1

print "\n"
print ave2 - ave3
print ave0 - ave2
print ave4 - ave0
print ave1 - ave4
