import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os

os.chdir(os.getcwd() + "/1000.test.runs.with.kmp1.one.minus.alpha.0.95")

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


#print ave0, std0


# 0.9 (1-alpha)
os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.90")

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


#print ave1, std1
  

# 0.98 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.98")

material2 = []


with open('product_storage') as f:
    for line in f:
        data = line.split()
        material2.append(float(data[4])) 


#print len(material2)
#print material2 

sum2 = 0.0
for i in range(0, 1000):
    sum2 = sum2 + material2[i]
ave2 = sum2/1000.0
std2 = np.std(material2)


#print ave2, std2



# 0.99 (1- alpha) 

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.99")

material3 = []

# 0.95 (1- alpha)
with open('product_storage') as f:
    for line in f:
        data = line.split()
        material3.append(float(data[4])) 


#print len(material3)
#print material3 

sum3 = 0.0
for i in range(0, 1000):
    sum3 = sum3 + material3[i]
ave3 = sum3/1000.0
std3 = np.std(material3)


#print ave3, std3


#0.925 (1-alpha)

os.chdir("./../1000.test.runs.with.kmp1.one.minus.alpha.0.925")

material4 = []

# 0.95 (1- alpha)
with open('product_storage') as f:
    for line in f:
        data = line.split()
        material4.append(float(data[4])) 


#print len(material4)
#print material4 

sum4 = 0.0
for i in range(0, 1000):
    sum4 = sum4 + material4[i]
ave4 = sum4/1000.0
std4 = np.std(material4)


#print ave4, std4


y = [ave3, ave2, ave0, ave4, ave1]
x = [1, 1 + bar_width*1.5, 1 + bar_width*3, 1 + bar_width*4.5 , 1 + bar_width*6]


bar_width = 0.0045 
#opacity = 0.4
#index = np_groups  
error_config = {'ecolor':'0.3'}


results3 = plt.bar(1, ave3, bar_width, alpha = opacity, color ='c', yerr = std3, error_kw = error_config, label='alpha = 0.01', capsize = 4)
results2 = plt.bar(1 + bar_width*1.5, ave2, bar_width, alpha = opacity, color ='c', yerr = std2, error_kw = error_config, label='alpha = 0.02')
results = plt.bar(1 + bar_width*3, ave0, bar_width, alpha = opacity, color ='c', yerr = std0, error_kw = error_config, label='alpha = 0.05')
results4 = plt.bar(1 + bar_width*4.5, ave4, bar_width, alpha = opacity, color ='c', yerr = std4, error_kw = error_config, label='alpha = 0.075')
results1 = plt.bar(1 + bar_width*6, ave1, bar_width, alpha = opacity, color ='c', yerr = std1, error_kw = error_config, label='alpha = 0.1')

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
plt.ylabel('Processed material (kg)')
plt.axis([0.99,1.035, 3250, 5000])
#plt.legend()

plt.savefig('processedmaterial.png')


plt.show()
