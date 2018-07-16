########################################################################
# Jieun Lee
# 05/31/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################
import numpy as np

from facility_component_module import facility_component_class
from batch_module import batch_class
from data_output_module import data_output_class

class melter_class(facility_component_class):
    
    """
    The melter takes the U and TRU, melts them with zirconium, and injects the melted alloy into quartz molds
    that will cool as they are passed onto the trimmer.

    This is the only component in the entire facility where some of the material gets left
    behind. 
    
    The actual amount lost each batch experiences is randomly selected as a uniform distribution
    
    The heel is made of the same stuff as the batch, thus comes from the same object. Whenever an alarm
    is set off, or if there is an equipment failure, the material gets sent to the recycle storage to be accounted
    for and eventually reprocessed.

    This is also the only component that can experience equipment failure. 
    
    #######
    # Variables 
    #######
    
    process_time_delay = the amount of time in days it takes to process the batch. 

    heel = object that keeps track how much SNM has left in the melter.

    failure_rate = average frequency that the melter will fail in the unit of 1/days.

    maintenance_time_delay = amount of time in days it takes to maintain the melter after it has experienced
    a failure.

    cleaning_time_delay = amount of time it takes to clean the heel out of the melter.

    time_of_last_failure = the operation time clocked (in days) when the melter last failed. This is used
    to keep track of how long it has been since parts have been replaced, thus how likely it is for a failure to
    occur again (maintenance_time_delay has to be accounted for.)

    true_batch_loss = variable that stores the true amount of batch loss. 

    failure_count = number of times this component has failed.

    failure_data_output = object that handles opening and writing to a file exclusively for variables
    that deal with the equipment failure check.
    
    """
    
    def __init__(self, facility):
             
        self.heel = batch_class(0, "heel") # heel initialization. 
        self.batch = batch_class(0, "batch") # batch initialization.
        
        self.process_time_delay = np.loadtxt(facility.process_states_dir + '/process.operation.time.inp', usecols=[1])[1]      # 8 hours = 0.3333 days 
        # self.batch = batch_class(self.batch_size, "batch")
        self.failure_rate = np.loadtxt(facility.failure_equipment_dir + '/melter.failure.data.inp', usecols=[1])               # 0.0333 days-1 = 1/30 days
        self.maintenance_time_delay = np.loadtxt(facility.failure_equipment_dir + '/melter.failure.data.inp', usecols=[2])     # 0.1667 days = 4 hours
        self.cleaning_time_delay = np.loadtxt(facility.failure_equipment_dir + '/melter.failure.data.inp', usecols=[3])        # 0.0833 days = 2 hours
        
        self.time_of_last_failure = 0 # The melter hasn't failed yet.
        self.true_batch_loss = 0  
        self.failure_count = 0
        
        self.failure_data_output = data_output_class("melter_failure_data", facility.equipment_failure_odir)
        facility_component_class.__init__(self, "melter", "processor", facility.material_flow_odir)

        self.sum = 0.0
        # self.true_weight = 0
        
    def process_batch(self, facility):
        
        """
        The melter loses some of the SNM during this process. Such is selected from a uniform distribution.

        #######
        # Return 
        #######
        True = melter did fail.  Need to run the failure routine.

        False = melter did not fail.  Fuel fabricator may continue running as normal.
        """
   
        self.write_to_log(facility,'Alloy melting\n')
        self.increment_operation_time(facility, self.process_time_delay) # 8 hours (melter process)
         
        did_fail = False
        #facility.melter_did_fail = True
        
        did_fail = self.check_equipment_failure(facility) # check the melter failure 
        
        if did_fail:
            self.write_to_log(facility,'Failure status:  True \n\n\n')
            facility.melter_did_fail = True
            
            
        
        else:
            self.write_to_log(facility,'Failure status:  False \n\n\n')
            
            ######
            # Calculate and assign weight losses 
            ######
            
            #print self.batch.weight
            #print 0.25 + 0.1*np.random.randn() 
            
            self.true_batch_loss = 0.25 + 0.1*np.random.randn()
            
            # true weight update        
            self.batch.weight = self.batch.weight - self.true_batch_loss
           
            print "melter, true batch weight: ", self.batch.weight 
            
            # return a sample from the "standard normal" distribution; sigma*np.random.rand(... ) N(mu, sigma^2)
            
            # self.true_weight = self.batch.weight 
            
            #######
            # Everything lost in batch is accumulated in the heel 
            #######
            
            self.heel.add_weight(self.true_batch_loss)
            print "true heel weight: ", self.heel.weight  
        
            self.sum = self.sum + self.heel.weight # total heel weight 
            
            #self.data_output.processor_output(facility, self)
            
        return did_fail, self.batch, self.heel

    def process_batch_without_failure_checkup(self, facility):
        
        self.write_to_log(facility,'Alloy melting\n')
        self.increment_operation_time(facility, self.process_time_delay) # 8 hours (melter process)
         
      
        self.write_to_log(facility,'Failure status:  False \n\n\n')
            
        ######
        # Calculate and assign weight losses 
        ######
            
        #print self.batch.weight
        #print 0.25 + 0.1*np.random.randn() 
            
        self.true_batch_loss = 0.25 + 0.1*np.random.randn()
            
        # true weight update        
        self.batch.weight = self.batch.weight - self.true_batch_loss
           
        print "melter, true batch weight: ", self.batch.weight 
            
        # return a sample from the "standard normal" distribution; sigma*np.random.rand(... ) N(mu, sigma^2)
            
        # self.true_weight = self.batch.weight 
            
        #######
        # Everything lost in batch is accumulated in the heel 
        #######
        self.heel.add_weight(self.true_batch_loss)
        print "true heel weight: ", self.heel.weight  
        
        self.sum = self.sum + self.heel.weight
                
        #self.data_output.processor_output(facility, self)
            
        return self.batch, self.heel
    
    def clean_material(self, facility):
        
        """
        material gets moved to recycle storage. This part is only for the time increment. 
        """
        
        self.write_to_log(facility,'Cleaning the material\n\n')
        self.increment_operation_time(facility, self.cleaning_time_delay)
        #######
        # Create new batch instance, because the assignment variable only copies the pointer, not the 
        # object itself.
        #######
        
        #self.data_output.processor_output(facility, self)
        

    def repair(self, facility):
        
        """
        Repair and maintain the melter after a failure has occurred.
        """
        
        self.write_to_log(facility,'Repairing melter\n\n')
        self.increment_operation_time(facility, self.maintenance_time_delay)
        
        
        self.time_of_last_failure = facility.operation_time
        
        #print "time of last failure: " + str(self.time_of_last_failure)
