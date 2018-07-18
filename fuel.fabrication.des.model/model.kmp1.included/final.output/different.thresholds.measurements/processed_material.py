import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os


os.chdir(os.getcwd() + "/alpha.0.05.measurement.error.percent.0.05")

attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
material = []

#0.05 %
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



# measurement 0.1 %
os.chdir(os.getcwd() + "/../different.false.alarm.probability.measurement.error.percent.0.1")

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
 




print ave0, std0
print ave1, std1




y = [ave0, ave1]
x = [1 + bar_width*1.3, 1 + bar_width*2.5]

results = plt.bar(1 + bar_width*1.3, ave0, bar_width, alpha = opacity, color ='c', yerr = std0, error_kw = error_config, capsize = 4)
results1 = plt.bar(1 + bar_width*2.5, ave1, bar_width, alpha = opacity, color ='c', yerr = std1, error_kw = error_config)


os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel('             0.05          0.1         \n'  + 'Relative random, or systematic error (%)')
plt.ylabel('Processed material (kg)')

plt.axis([0.99,1.033, 3500, 5000])
#plt.legend(handles=[results, results1])


plt.savefig('Processedmaterial.png')
plt.show()