import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os

os.chdir(os.getcwd() + "/baseline")
attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
material = []

# 0.95 (1- alpha)
with open('product_storage') as f:
    for line in f:
        data = line.split()
        attempts.append(int(data[0]))
        material.append(float(data[4])) 

#print len(attempts)
#print len(material)

#print attempts 
#print material


sum0 = 0.0
for i in range(0, 1000):
    sum0 = sum0 + material[i]
ave0 = sum0/1000.0
std0 = np.std(material)


print ave0, std0


# kmp1 removed
os.chdir("./../equipment")


material1 = []


with open('product_storage') as f:
    for line in f:
        data = line.split()
        material1.append(float(data[4])) 


#print len(material1)
#print material1

sum1 = 0.0
for i in range(0, 1000):
    sum1 = sum1 + material1[i]
ave1 = sum1/1000.0
std1 = np.std(material1)


print ave1, std1
  
print ave1 - ave0


y = [ave0, ave1]
x = [1, 1 + bar_width*3]


bar_width = 0.0045 
#opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}


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
plt.ylabel('Processed material (kg)')
plt.axis([0.99,1.025, 3250, 5000])
#plt.legend()

plt.savefig('processedmaterial.png')


plt.show()
