########################################################################
# Jieun Lee, R.A. Borrelli
# 05/30/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################
import numpy as np
from facility_component_module import facility_component_class
import math

from batch_module import batch_class
from data_output_module import data_output_class

class key_measurement_point_class(facility_component_class):
    
    """
    Key measurement points are the only points along the system that can actually weigh the materials and determine
    if a discrepancy has occurred. How much weight should be detected is passed
    to it from the previous object via the edge transition.  
    
    Each kmp should be specified separately where it lies along the
    system. Each one will measure the weight of the batch as it comes in.
   
    The kmp_indentifier is used for the log file and for getting the correct
    data from the input file.

    #######
    # Variables 
    #######

    uncertainty = standard deviation of each measurement to simulate realistic 
    equipment uncertainty when measuring the weight.

    time_delay = time in days that the kmp takes to make the measurement.

    alarm_threshold = weight in kg that will make an alarm ring when the standard deviation of ID is at least that much.

    identifier = integer number labeling used for a kmp. Used in getting input data from files and
    also keeping track in the log file.

    measured_weight = the weight of the batch most recently measured in kg
    """

    def __init__(self, facility, kmp_identifier):
        
        self.batch = batch_class(0, "batch")
        
        self.identifier = kmp_identifier 
        self.measured_weight = 0 # measurement
        self.muf = 0
        
        
        
        self.uncertainty = np.loadtxt(facility.kmps_dir + '/key.measurement.points.inp', usecols=[2])[kmp_identifier] # std = 0.01; uncertainty only associated with measurement
        self.time_delay = np.loadtxt(facility.kmps_dir + '/key.measurement.points.inp', usecols=[1])[kmp_identifier] # kmp measurement time = 30 mins = 0.0208 days.
        #print self.uncertainty
        
        #self.kmp_alarm_threshold = self.alarm_threshold() #expected values: (0.02, 0.101980390272)
        # print self.kmp_alarm_threshold[1]
        # only one standard deviation can be used as a threshold. However, the false alarm probability will be low in this case compared to 0.95.
        # Or, you can use a false alarm probability of 95%. 
        
        self.kmp_alarm_threshold1 = 0.0 
        self.kmp_alarm_threshold2 = 0.0
        self.kmp_alarm_threshold_0_3 = 0.0
        self.kmp_alarm_threshold_3_3 = 0.0
        
        facility_component_class.__init__(self, "key_measurement_point_%i"%(kmp_identifier), "kmp", facility.kmps_odir)
        
        self.muf_data_output1 = open(facility.muf_odir+ '/muf1.out', 'w+') # muf info
        self.muf_data_output2 = open(facility.muf_odir+ '/muf2.out', 'w+')
        self.muf_data_output3 = open(facility.muf_odir+ '/muf3.out', 'w+')        
              
        
    def alarm_threshold1(self, facility):
        
        combined_sigma = math.sqrt(2*(20*0.05/100)**2)  # 0.0141421356237
        combined_sigma_next = math.sqrt(2*(19.75*0.05/100)**2) # 0.0139653589284
        
        
        # R - S - delta with a material loss
        # delta_sigma has to be determined from lab-scale or engineering-scale experiments. 
        # For now, we assume mu = 250 g, uncertainty = 100g.  
        delta_sigma = 0.1 
        sigma_with_loss = math.sqrt(combined_sigma**2 + (combined_sigma_next)**2 + delta_sigma**2)
        #print combined_sigma
        #print combined_sigma_next
        #print sigma_with_loss # 0.10195602606
        return 1.645*sigma_with_loss # 0.95%   1.645*0.10195602606 = 0.16771766286More info

    
    def alarm_threshold2(self, facility):
       
        combined_sigma = math.sqrt(2*(20*0.05/100)**2)  # 0.0141421356237
        combined_sigma_next = math.sqrt(2*(19.75*0.05/100)**2) # 0.0139653589284
        
        
        # R - S - delta with a material loss
        # delta_sigma has to be determined from lab-scale or engineering-scale experiments. 
        # For now, we assume mu = 250 g, uncertainty = 100g.  
        delta_sigma = 0.1 
        sigma_with_loss = math.sqrt(combined_sigma**2 + (combined_sigma_next)**2 + delta_sigma**2)
        #print combined_sigma
        #print combined_sigma_next
        #print sigma_with_loss # 0.10195602606
        return 1.645*sigma_with_loss # 0.95%   1.645*0.10195602606 = 0.16771766286More info

    
    def alarm_threshold3(self, facility):
        # For the material going to recycle storage ..
        
        combined_sigma = math.sqrt(2*(20*0.05/100)**2) # 0.01414213562
        sigma_no_loss = math.sqrt(combined_sigma**2 + combined_sigma**2)
        
        print combined_sigma # 0.02
        
        return 1.645*sigma_no_loss # 0.0329
        
    def process_batch(self, facility):
        """
        The kmp weighs the batch, then checks to see if it is close enough to what is expected.
        
        """
                     
        self.write_to_log(facility,'Measurement event at KMP: %i\n'%(self.identifier))
        
        #print 'batch weight' + str(self.batch.weight) + '\n\n'
        #print self.batch.weight
        combined_sigma = math.sqrt(2*(20*0.05/100)**2)
        combined_sigma_next = math.sqrt(2*(19.75*0.05/100)**2)
    
        #print combined_sigma # 0.0141421356237
        #print combined_sigma_next # 0.0139653589284
        
        if (self.identifier == 0 or self.identifier == 3): 
            self.measured_weight = 20.0 + combined_sigma*np.random.randn() 
            #print "kmp" # return a sample from the "standard normal" distribution; sigma*np.random.rand(... ) N(mu, sigma^2)
        
        if (self.identifier == 1 or self.identifier == 2):
            self.measured_weight = 19.75 + combined_sigma_next*np.random.randn()
             
        self.increment_operation_time(facility, self.time_delay)
        
        #print self.batch.weight
        
        #######
        # Data Writing  
        #######
        self.write_to_log(facility,'Operation time %.4f (d) \nTrue quantity %.4f (kg) \nMeasured quantity %.4f (kg) \n\n\n'\
                %(facility.operation_time, self.batch.weight, self.measured_weight))
        
        self.data_output.kmp_output(facility, self) 
       
        print "KMP", self.identifier, ", true: ", self.batch.weight
        print "KMP", self.identifier, ", measured: ", self.measured_weight
        
    
        return self.batch
        #######
        # Check for discrepancy  
        #######
        # i indicates the previous kmp number.
     
       
    def muf_check(self, facility): 
        
        muf_check = False
        
        facility.total_muf_cal = facility.total_muf_cal + 1 
        
        """
        if (self.identifier == 1):  
            
            facility.muf_cal_1 = facility.muf_cal_1 + 1
        
            if (facility.failure_check == True):
                
                #print '\n'
                #print facility.kmp[self.identifier - 1].measured_weight
                #print self.measured_weight 
            
                self.muf = facility.kmp[self.identifier + 2].measured_weight - self.measured_weight - facility.melter.heel.weight
                       
                print "std muf: " + str(self.muf) # This threshold is from unit.testing.py.
             
                self.kmp_alarm_threshold1 = self.alarm_threshold1(facility) 
                print "threshold: " + str(self.kmp_alarm_threshold1)
                
                facility.sequential_muf = facility.sequential_muf + self.muf
                                       
                if (self.muf > self.kmp_alarm_threshold1):
                    
                    facility.false_alarm_count_1 = facility.false_alarm_count_1 + 1 
                    
                    print "threshold: " + str(self.kmp_alarm_threshold1)
                    muf_check = self.kmp_alarm(facility)
            
                    self.write_to_log(facility,
                    '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY!\n\n\n'%(self.description))
                
                    self.muf_data_output1.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold1))
                
                
                    #self.data_output.muf_output(facility, self)
                else:
                    self.write_to_log(facility, 'Keep going! The material can be passed to the next point.\n\n\n')
                    # print self.kmp_alarm_threshold[0]
                    # print self.kmp_alarm_threshold[1]       
                    #self.data_output.muf_output(facility, self)
                    self.muf_data_output1.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold1))
                                   
            
            else:   
                            
                self.muf = facility.kmp[self.identifier - 1].measured_weight - self.measured_weight - facility.melter.heel.weight
                       
                print "std muf: " + str(self.muf) # This threshold is from unit.testing.py.
            
                self.kmp_alarm_threshold1 = self.alarm_threshold1(facility) 
                print "threshold: " + str(self.kmp_alarm_threshold1)
                
                facility.sequential_muf = facility.sequential_muf + self.muf
            
                if (self.muf > self.kmp_alarm_threshold1):
                    
                    facility.false_alarm_count_1 = facility.false_alarm_count_1 + 1 
                    
                    print "threshold: " + str(self.kmp_alarm_threshold1)
                    muf_check = self.kmp_alarm(facility)
            
                    self.write_to_log(facility,
                    '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY!\n\n\n'%(self.description))
                
                    self.muf_data_output1.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold1))
                
                
                    #self.data_output.muf_output(facility, self)
                else:
                    self.write_to_log(facility, 'Keep going! The material can be passed to the next point.\n\n\n')
                    # print self.kmp_alarm_threshold[0]
                    # print self.kmp_alarm_threshold[1]       
                    #self.data_output.muf_output(facility, self)
                    self.muf_data_output1.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold1))
        """
        if (self.identifier == 2):
        
            facility.muf_cal_2 = facility.muf_cal_2 + 1
           
            
            self.muf = facility.kmp[self.identifier - 2].measured_weight - self.measured_weight - facility.melter.heel.weight
            print "std muf: " + str(self.muf)
            
            self.kmp_alarm_threshold2 = self.alarm_threshold2(facility) 
            print "threshold: " + str(self.kmp_alarm_threshold2)
            
            facility.sequential_muf = facility.sequential_muf + self.muf
            
            if (self.muf > self.kmp_alarm_threshold2):
                
                facility.false_alarm_count_2 = facility.false_alarm_count_2 + 1 
                
                print "threshold: " + str(self.kmp_alarm_threshold2)
                muf_check = self.kmp_alarm(facility)
                              
                self.write_to_log(facility,
                    '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY TO RECYCLE STORAGE!\n\n\n'%(self.description))
                
                self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold2)) 
                #self.data_output.muf_output(facility, self)
                
            else:
                self.write_to_log(facility, 'Keep going! The material can be passed to the next point.\n\n\n')
            # print self.kmp_alarm_threshold[0]
            # print self.kmp_alarm_threshold[1]       
            # self.data_output.muf_output(facility, self)   
                self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold2))     
            
        if (self.identifier == 3):
            
            facility.muf_cal_3 = facility.muf_cal_3 + 1
          
            
            self.muf = facility.kmp[self.identifier - 3].measured_weight - self.measured_weight # '-heel' does not require because, everything gets transferred to recycle storage.  
            print "std muf: " + str(self.muf)
            
            self.kmp_alarm_threshold_0_3 = self.alarm_threshold3(facility)
            print "threshold: " + str(self.kmp_alarm_threshold_0_3)
            
            facility.sequential_muf = facility.sequential_muf + self.muf
            
            if (self.muf > self.kmp_alarm_threshold_0_3):
                
                facility.false_alarm_count_3 = facility.false_alarm_count_3 + 1
                
                print "threshold: " + str(self.kmp_alarm_threshold_0_3)
                muf_check = self.kmp_alarm(facility)
                              
                self.write_to_log(facility,
                    '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY TO RECYCLE STORAGE!\n\n\n'%(self.description))
                
                self.muf_data_output3.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold_0_3)) 
                #self.data_output.muf_output(facility, self)
                
            else:
                self.write_to_log(facility, 'No missing SNM has found, however, the melter failed. The material will be passed to the recycle storage.\n\n\n')
            # print self.kmp_alarm_threshold[0]
            # print self.kmp_alarm_threshold[1]       
            # self.data_output.muf_output(facility, self)   
                self.muf_data_output3.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold_0_3)) 
        
        return muf_check
        
        #threshold with no loss: 0.0332078231199
        #threshold without a loss: 0.169327338092
    
    
    def muf_check_2_melter(self, facility, previous_value): 
        
        facility.muf_cal_3 = facility.muf_cal_3 + 1
        facility.total_muf_cal = facility.total_muf_cal + 1 
        
        muf_check = False
        
        self.muf = previous_value - self.measured_weight 
        print "std muf: " + str(self.muf)
        
        self.kmp_alarm_threshold_3_3 = self.alarm_threshold3(facility) 
        print "threshold: " + str(self.kmp_alarm_threshold_3_3)
        
        facility.sequential_muf = facility.sequential_muf + self.muf
            
        if (self.muf > self.kmp_alarm_threshold_3_3):
           
           facility.false_alarm_count_3 = facility.false_alarm_count_3 + 1
            
           print "threshold: " + str(self.kmp_alarm_threshold_3_3)
           muf_check = self.kmp_alarm(facility)
                              
           self.write_to_log(facility,
                '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY TO RECYCLE STORAGE!\n\n\n'%(self.description))
                
           self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold_3_3)) 
                #self.data_output.muf_output(facility, self)
                
        else:
           self.write_to_log(facility, 'No missing SNM has found, however, the melter failed. The material will be passed to the recycle storage.\n\n\n')
            # print self.kmp_alarm_threshold[0]
            # print self.kmp_alarm_threshold[1]       
            # self.data_output.muf_output(facility, self)   
           self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold_3_3)) 
            
        return muf_check

    def muf_check_from_recycle(self, facility):
        
        facility.total_muf_cal = facility.total_muf_cal + 1 

        facility.muf_cal_2 = facility.muf_cal_2 + 1 

        
        muf_check = False
        
        self.muf = facility.kmp[self.identifier + 1].measured_weight - self.measured_weight - facility.melter.heel.weight
                       
        print "std muf: " + str(self.muf) # This threshold is from unit.testing.py.
            
        self.kmp_alarm_threshold2 = self.alarm_threshold2(facility) 
        print "threshold: " + str(self.kmp_alarm_threshold2)
        
        facility.sequential_muf = facility.sequential_muf + self.muf
                
        if (self.muf > self.kmp_alarm_threshold2):

            facility.false_alarm_count_2 = facility.false_alarm_count_2 + 1
            
            print "threshold: " + str(self.kmp_alarm_threshold2)
            muf_check = self.kmp_alarm(facility)
                              
            self.write_to_log(facility,
                  '\nMISSING SNM DETECTED in %s!  A BATCH WILL GET MOVED IMMEDIATELY TO RECYCLE STORAGE!\n\n\n'%(self.description))
                
            self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold2)) 
                #self.data_output.muf_output(facility, self)
                
        else:
            self.write_to_log(facility, 'Keep going! The material can be passed to the next point.\n\n\n')
                # print self.kmp_alarm_threshold[0]
                # print self.kmp_alarm_threshold[1]       
                # self.data_output.muf_output(facility, self)   
            self.muf_data_output2.write('%.4f\t%i\t%i\t%.4f\t%.4f\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count, self.muf, self.kmp_alarm_threshold2))     
        
        return muf_check
        
    def kmp_alarm(self, facility):
        
        """
        When a kmp discovers a discrepancy between the stanard deviation of ID and its threshold, this routine is called.
        The kmp gets inspected. The material is sent to recycle storage.  
        """
                
        #  The false_alarm_count gets incremented here.
        facility.false_alarm_count = facility.false_alarm_count + 1 # Increment the false alarm count.
        
        # The previous kmp info check up
        if(self.identifier == 1):
            self.write_to_log(facility, '\nInspecting %s: \n'%(self.description) + 'Threshold: %.4f \nMeasured quantity %.4f \n'%(self.kmp_alarm_threshold1, self.measured_weight))
        
        if(self.identifier == 2):
            self.write_to_log(facility, '\nInspecting %s: \n'%(self.description) + 'Threshold: %.4f \nMeasured quantity %.4f \n'%(self.kmp_alarm_threshold2, self.measured_weight))
        
        if(self.identifier == 3):
            if(self.kmp_alarm_threshold_3_3):
                self.write_to_log(facility, '\nInspecting %s: \n'%(self.description) + 'Threshold: %.4f \nMeasured quantity %.4f \n'%(self.kmp_alarm_threshold_3_3, self.measured_weight))
            else:
                self.write_to_log(facility, '\nInspecting %s: \n'%(self.description) + 'Threshold: %.4f \nMeasured quantity %.4f \n'%(self.kmp_alarm_threshold_0_3, self.measured_weight))
            
        
        return True
    
   
        
        
            
