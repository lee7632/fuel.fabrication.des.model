import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os

os.chdir(os.getcwd() + "/mean.250")

attempts = []
#operation_time = []
#false_alarm = []
#melter_failure = []
material = []



# 250 g 
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



# 150 g 
os.chdir("./../mean.150")




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
 


# 300 g 
os.chdir("./../mean.300")



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


print "\n"

print ave1, std1
print ave0, std0
print ave2, std2



y = [ave1, ave0, ave2]
x = [1 + bar_width*1.3, 1 + bar_width*2.5, 1 + bar_width*3.7]

results1 = plt.bar(1 + bar_width*1.3, ave1, bar_width, alpha = opacity, color ='c', yerr = std1, error_kw = error_config, capsize = 4)
results = plt.bar(1 + bar_width*2.5, ave0, bar_width, alpha = opacity, color ='c', yerr = std0, error_kw = error_config)
results2 = plt.bar(1 + bar_width*3.7, ave2, bar_width, alpha = opacity, color ='c', yerr = std2, error_kw = error_config)
os.chdir('./../')

plt.tick_params(
    axis='x',
    which='both',
    bottom='off',
    top='off',
    labelbottom='off')
    
plt.plot(x, y, 'o-', color='black', linewidth = 0.8, markersize = 4)
plt.xlabel('   150       250         300\n'  + 'Heel mean (g)')
plt.ylabel('Processed material (kg)')

plt.axis([0.99,1.032, 3500, 5000])
#plt.legend(handles=[results, results1])
plt.savefig('Processedmaterial.png')
plt.show()