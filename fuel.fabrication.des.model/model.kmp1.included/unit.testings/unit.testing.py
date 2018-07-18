# -*- coding: utf-8 -*-
"""
Unit testings 

(1) random + systematic errors from measurement
(2) heel in the melter 
(3) propagation of variance
(4) inventory verification - physical inventory 
(5) inventory verification - random sampling 
(6) cdf (melter failure)

@author: jlee

"""

import math
import numpy as np
import matplotlib.pyplot as plt

import scipy.stats as stats
import pylab 


# (1) random + systematic errors from measurement
"""
ITVs already have estimated random and systemtatic errors associated with an electronic balance. 
relative measurement errors: 0.05%

20 kg of batch is moved from vertex to vertex. 
"""

# only measurement errors associated.

mu = 20 # unit: kg
sigma = math.sqrt(2*(20*0.05/100)**2) #std 
#print sigma

measurement = [] # 100 random measurements

for i in range (0, 100):
    tmp = mu + sigma*np.random.randn() 
    measurement.append(tmp)
    
measurement.sort()
pdf = stats.norm.pdf(measurement, mu, sigma)

pylab.plot(measurement, pdf, '-o')
pylab.hist(measurement, normed=True, alpha=0.7, histtype='bar', ec='black')
pylab.xlabel('Measurement (kg)')
pylab.ylabel('PDF')
pylab.title('Gaussian Distribution\n' +
    'mu = 20 kg, std = ' + '%.5f'%sigma + 'kg, 100 samples')
pylab.show() 

# (2) heel in the melter 

""" First, let's determine the delta sigma value (standard deviation associated with the hold-up material)
    ave = 250 g, sigma = 0.1 """
    
mu2 = 0.25
sigma2 = 0.1
hold_up_material = []

for i in range(0, 100):
    tmp = mu2 + sigma2*np.random.randn()
    hold_up_material.append(tmp)
    
hold_up_material.sort()
pdf2 = stats.norm.pdf(hold_up_material, mu2, sigma2) # a normal continuous random variable

pylab.plot(hold_up_material, pdf2 , '-o')
pylab.hist(hold_up_material, normed=True, alpha=0.5, histtype='bar', ec='black', color ='r')
pylab.xlabel('Measurement (kg)')
pylab.ylabel('PDF')
pylab.title('Gaussian Distribution\n' +
    'mu = 0.25 kg, std = ' + '%.1f'%sigma2 + 'kg, 100 samples')
pylab.show() 

kmp1 = 19.75 
sigma_kmp1 = math.sqrt(2*(19.75*0.05/100)**2)

# (3) propagation of variance
    
# R - S without material losses 
sigma_no_loss = math.sqrt(2*sigma**2)

# R - S - delta with a material loss
# delta_sigma has to be determined from lab-scale or engineering-scale experiments. 
# For now, we assume mu = 250 g, uncertainty = 100g.  
delta_sigma = 0.1 
sigma_with_loss = math.sqrt(sigma**2 + delta_sigma**2 + sigma_kmp1**2)
#print sigma_with_loss


"""
expected answers: 
measurement std: 0.0141421356237
R-S: 0.02
R-S - delta: 0.101980390272
"""
             
# R - S without material losses
mu_id = 0 
std_no_loss = []

for i in range(0, 100):
    tmp = mu_id + sigma_no_loss*np.random.randn()
    std_no_loss.append(tmp)
    
std_no_loss.sort()
pdf3 = stats.norm.pdf(std_no_loss, mu_id, sigma_no_loss)

pylab.plot(std_no_loss, pdf3 , '-o', label= 'mu = 0, std = 0.02kg (no material loss)')
pylab.hist(std_no_loss, normed=True, alpha=0.3, histtype='bar', ec='black', color ='b')
pylab.xlabel('Measurement (kg)')
pylab.ylabel('PDF')
pylab.title('ID Gaussian Distribution')


# R - S with a material loss

# R - S without material losses

std_loss = []

for i in range(0, 100):
    tmp = mu_id + sigma_with_loss*np.random.randn()
    std_loss.append(tmp)
    
std_loss.sort()
pdf4 = stats.norm.pdf(std_loss, mu_id, sigma_with_loss)

pylab.plot(std_loss, pdf4 , '-o', label= 'mu = 0, std = 0.102kg (with a material loss)')
pylab.hist(std_loss, normed=True, alpha=0.3, histtype='bar', ec='black', color ='r')

#print "std with no loss: " + str(sigma_no_loss)
#print "std with a loss: " + str(sigma_with_loss)

# false alarm: 0.05%

confidence1 = stats.t.interval(alpha = 0.90, df= 99, loc = 0, scale = sigma_no_loss)
#print "threshold with no loss: " + str(confidence1[1])
threshold_no_loss= confidence1[1]

confidence2 = stats.t.interval(alpha = 0.90, df= 99, loc = 0, scale = sigma_with_loss)
#print "threshold with a loss: " + str(confidence2[1])
threshold_with_loss = confidence2[1]


# alarm thresholds set up (line graphs construction)
 
y_threshold = []
x_threshold = []
x_threshold_loss = []

# 25 values used.
for i in range(0, 25):
    y_threshold.append(float(i))
    x_threshold.append(float(threshold_no_loss))
    x_threshold_loss.append(float(threshold_with_loss))
    
pylab.plot(x_threshold, y_threshold, linewidth = 0.7 , label='an alarm threshold with a false alarm probability of 0.05')
pylab.plot(x_threshold_loss, y_threshold, linewidth =  0.7, label='an alarm threshold with a false alarm probability of 0.05')
#pylab.hist(std_with_loss, normed=True, alpha=0.3, histtype='bar', ec='black', color ='r')
pylab.legend(bbox_to_anchor=(0.03, -.2), loc=2, borderaxespad=0.)
pylab.show() 

"""
expected answers:
threshold with no loss: 0.0332078231199
threshold without a loss: 0.169327338092
"""

# (4) inventory verification - physical inventory 

"""
Let's assume that 20 kg of SNM gets stored in a vessel.
Therefore, total 500 vessels are stored in the buffer. 
Weight meausurement is performed with each vessel using an electronic balance. 
"""
# storage buffer
# initial inventory  
total_campaign = 1 
sigma_measured_inventory = math.sqrt(( 500 - total_campaign + 1 )*(20.0*0.05/100.0)**2) # mu = 10000 kg
#print "std " + str(total_campaign) +" : " + str(sigma_measured_inventory) #; expected value: 0.22360679775 kg

# end inventory
total_campaign = 30  # 30; an arbitrary value, other values will be used for this later. 
sigma_measured_inventory = math.sqrt(( 500 - total_campaign )*(20.0*0.05/100.0)**2) # mu = vessel numbers* 20kg 
#print "std " + str(total_campaign) +" : " + str(sigma_measured_inventory) 

# product storage 
# initial inventory
# 0 kg

"""
expected answers:
std 1   0.22360679775
std 30  0.217025344142
"""

# (5) inventory verification - random sampling 

#initial variables
N = 500.0 # vessels 
beta = 0.95 # detection probability 

x = []

# In reability, the recorded measurements will be used. 
for i in range(0, 500):
    tmp = 20.0 + sigma*np.random.randn() 
    x.append(tmp)

# sum of 500 values. 
su = 0.0
for j in range(0, 500):
    su = su + x[j]

# average calculation
ave = su/N

M = 8.0 # 8kg of Pu 

n = N*(1 - (beta)**(ave/M))

# number of samples that you have to physically check out. 
#print "number of test samples: " + str(n)

# (6) cdf (melter failure)
# rate parameter (lambda) = 1/beta 
time = np.linspace(0, 50, 100)
failure_rate = 1/30.0 # (day^-1) # 1 failure / 30 days.

pdf = failure_rate*np.exp(-time*failure_rate)
cdf = 1 - np.exp(-time*failure_rate)

# cdf plot

plt.subplot(212)

plt.plot(time, pdf, 'r')
plt.ylabel('pdf', rotation = 0, labelpad = 20)
plt.xlabel('Time (days)')
plt.axis([0.00,50, 0.00, 0.035])
plt.fill_between(time, pdf, alpha = 0.3, color = 'orange')

plt.subplot(211)
plt.plot(time, cdf, 'b', alpha = 0.7)
plt.ylabel('cdf', rotation = 0, labelpad = 25)
plt.title('Melter Failure Probability Function')
plt.axis([0.00,50, 0.00, 0.8])



# 25 random numbers between 0 and 1 are chosen.
test = []
for i in range(0, 25):
    fail_check = np.random.rand()
    test.append(fail_check)

#print len(test)

#print len(test_time)



plt.show()






# also, needs a graph for cumulative muf
# graph for accumulated sequential muf

# error bars 
# ending inventory calculations...
# 

  