import math
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats
import pylab 

"""This file is to have a unit test of 'random sampling'. 
   Number of vessels, which must be inspected to maintain the detection probability of 0.95, can be calculated by using this equation of 'random sampling'. 
"""
# number of vessels
N = [50, 100, 150, 200, 250, 300, 350 , 400, 450, 500]   
# non-detection probability
beta = 0.05  
# average weights of vessels
mu = [0.1, 0.5, 1, 3, 5, 8, 10, 13, 15, 18, 20] 

# This is to provide the standard error for each weight measurement (systematic error + random error). 
sigma = [] 
for i in range(11):
    sigma.append(math.sqrt(2*(mu[i]*0.05/100)**2))
   
#print sigma 
# weight measurements 
x = []
x1 = []
x2 = [] 
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
x10 = []

# sum 
su = [] 
su1 = [] 
su2 = [] 
su3 = [] 
su4 = [] 
su5 = [] 
su6 = [] 
su7 = [] 
su8 = []
su9 = []
su10 = []

# average
ave = []  
ave1 = [] 
ave2 = [] 
ave3 = []
ave4 = []
ave5 = []
ave6 = []
ave7 = [] 
ave8 = [] 
ave9 = [] 
ave10 = []

# sample size
n = []
n1 = [] 
n2 = [] 
n3 = [] 
n4 = [] 
n5 = [] 
n6 = [] 
n7 = [] 
n8 = []
n9 = [] 
n10 = []

# initialization of dummy variables to calculate the average weights of vessels. 
for i in range(0, 10):
    x.append([])
    x1.append([])
    x2.append([])
    x3.append([])
    x4.append([])
    x5.append([])
    x6.append([])
    x7.append([])
    x8.append([])
    x9.append([])
    x10.append([])
    
    su.append(0.0)
    su1.append(0.0)
    su2.append(0.0)
    su3.append(0.0)
    su4.append(0.0)
    su5.append(0.0)
    su6.append(0.0)
    su7.append(0.0)
    su8.append(0.0)
    su9.append(0.0)
    su10.append(0.0)
       
    ave.append(0.0)
    ave1.append(0.0)
    ave2.append(0.0)
    ave3.append(0.0)
    ave4.append(0.0)
    ave5.append(0.0)
    ave6.append(0.0)
    ave7.append(0.0)
    ave8.append(0.0)
    ave9.append(0.0)
    ave10.append(0.0)
   
    n.append(0.0)
    n1.append(0.0)
    n2.append(0.0)
    n3.append(0.0)
    n4.append(0.0)
    n5.append(0.0)
    n6.append(0.0)
    n7.append(0.0)
    n8.append(0.0)
    n9.append(0.0)
    n10.append(0.0)
    
# In reality, the recorded measurements will be used. 
for j in range(0, len(N)):
    for i in range(0, N[j]):
        tmp = mu[0]  + sigma[0]*np.random.randn() 
        tmp1 = mu[1]  + sigma[1]*np.random.randn() 
        tmp2 = mu[2]  + sigma[2]*np.random.randn() 
        tmp3 = mu[3]  + sigma[3]*np.random.randn() 
        tmp4 = mu[4]  + sigma[4]*np.random.randn() 
        tmp5 = mu[5]  + sigma[5]*np.random.randn() 
        tmp6 = mu[6]  + sigma[6]*np.random.randn() 
        tmp7 = mu[7]  + sigma[7]*np.random.randn() 
        tmp8 = mu[8]  + sigma[8]*np.random.randn() 
        tmp9 = mu[9]  + sigma[9]*np.random.randn() 
        tmp10 = mu[10]  + sigma[10]*np.random.randn() 
        
        x[j].append(tmp)
        x1[j].append(tmp1)
        x2[j].append(tmp2)
        x3[j].append(tmp3)
        x4[j].append(tmp4)
        x5[j].append(tmp5)
        x6[j].append(tmp6)
        x7[j].append(tmp7)
        x8[j].append(tmp8)
        x9[j].append(tmp9)
        x10[j].append(tmp10)
        
#print len(x[0])
# sum of values. & average calculation
for j in range(0, len(N)):
    for i in range(0, N[j]):
        su[j] = su[j] + x[j][i]
        su1[j] = su1[j] + x1[j][i]
        su2[j] = su2[j] + x2[j][i]
        su3[j] = su3[j] + x3[j][i]
        su4[j] = su4[j] + x4[j][i]
        su5[j] = su5[j] + x5[j][i]
        su6[j] = su6[j] + x6[j][i]
        su7[j] = su7[j] + x7[j][i]
        su8[j] = su8[j] + x8[j][i]
        su9[j] = su9[j] + x9[j][i]
        su10[j] = su10[j] + x10[j][i]
       
for j in range(0, len(N)):
    ave[j] = su[j]/N[j]
    ave1[j] = su1[j]/N[j]
    ave2[j] = su2[j]/N[j]
    ave3[j] = su3[j]/N[j]
    ave4[j] = su4[j]/N[j]
    ave5[j] = su5[j]/N[j]
    ave6[j] = su6[j]/N[j]
    ave7[j] = su7[j]/N[j]
    ave8[j] = su8[j]/N[j]
    ave9[j] = su9[j]/N[j]
    ave10[j] = su10[j]/N[j]
    
M = 8.0 # 8kg of Pu 

for j in range(0, len(N)):
    n[j] = N[j]*(1 - (beta)**(ave[j]/M))
    n1[j] = N[j]*(1 - (beta)**(ave1[j]/M))
    n2[j] = N[j]*(1 - (beta)**(ave2[j]/M))
    n3[j] = N[j]*(1 - (beta)**(ave3[j]/M))
    n4[j] = N[j]*(1 - (beta)**(ave4[j]/M))
    n5[j] = N[j]*(1 - (beta)**(ave5[j]/M))
    n6[j] = N[j]*(1 - (beta)**(ave6[j]/M))
    n7[j] = N[j]*(1 - (beta)**(ave7[j]/M))
    n8[j] = N[j]*(1 - (beta)**(ave8[j]/M))
    n9[j] = N[j]*(1 - (beta)**(ave9[j]/M))
    n10[j] = N[j]*(1 - (beta)**(ave10[j]/M))
    
# number of samples that you have to physically check out. 
plt.plot(N, n, color = 'r', alpha = 0.8, markersize = 4, label = str(mu[0]) +' kg')
plt.plot(N, n1, color = 'b', alpha = 0.8, markersize = 4, label = str(mu[1]) +' kg')
plt.plot(N, n2, color = 'purple', alpha = 0.8, markersize = 4, label = str(mu[2]) +' kg')
plt.plot(N, n3, color = 'orange', alpha = 0.8, markersize = 4, label = str(mu[3]) +' kg')
plt.plot(N, n4, alpha = 0.8, markersize = 4, label = str(mu[4]) +' kg')
plt.plot(N, n5, alpha = 0.8, markersize = 4, label = str(mu[5]) +' kg')
plt.plot(N, n6, alpha = 0.8, markersize = 4, label = str(mu[6]) +' kg')
plt.plot(N, n7, alpha = 0.8, markersize = 4, label = str(mu[7]) +' kg')
plt.plot(N, n8, alpha = 0.8, markersize = 4, label = str(mu[8]) +' kg')
plt.plot(N, n9, alpha = 0.8, markersize = 4, label = str(mu[9]) +' kg')
plt.plot(N, n10, alpha = 0.8, markersize = 4, label = str(mu[10]) +' kg')

plt.xlabel('Population size (N)')
plt.ylabel('Sample size (n)')

#plt.axis([0.97,1.25, 0, 0.15])
plt.legend(loc = [1.05, 0.23])

#print n, n10