########################################################################
# Jieun Lee, R.A.Borrelli
# 05/29/2018
# 
########################################################################
# 
# See class description
#
########################################################################
import numpy as np
from facility_component_module import facility_component_class
from batch_module import batch_class
import math

class product_storage_class(facility_component_class):
    """
    The product storage is the facility component that stores the final product of the entire pyroprocessing
    facility. 

    #######
    # Variables 
    #######
    inventory = actual amount of SNM that the storage buffer is holding in kg

    inventory = the amount of SNM that the storage buffer is holding in kg with the associated uncertainties

    measured_inventory = measured amount of SNM in the product storage
    
    time_delay = amount of time it takes the product storage to store a batch.

       
    """

    def __init__(self, facility):
        
        #self.batch_size = np.loadtxt(facility.process_states_dir + '/batch.inp') # 20 KG
        self.batch = batch_class(0, "batch") 
        
        self.inventory = 0
        self.end_time_inspection = 0.166667 # 4 hours 
        
        self.time_delay = np.loadtxt(facility.process_states_dir+'/process.operation.time.inp',usecols=[1])[3] # 0.0833 days; 2 hours
       
        #if (facility.total_campaign == 1):
        self.measured_inventory = 0
        
        #self.measured_inventory_calculation(facility)
        #print "Round (storage buffer inventory) " + str(facility.total_campaign) +" : " + str(self.measured_inventory) 
               
        facility_component_class.__init__(self, "product_storage", "storage", facility.inventory_odir)
        
        
    def process_batch(self, facility):
        """
        The final product is added to the inventory.
        """
        self.write_to_log(facility,'Processing the final product \n\n\n')
        self.increment_operation_time(facility, self.time_delay)
        
        self.inventory = self.inventory + self.batch.weight
        self.measured_inventory = self.measured_inventory + facility.kmp[2].measured_weight
        
                       
        self.increment_operation_time(facility, self.end_time_inspection)
        self.data_output.storage_output(facility, self)
        
        print "PS, true: ", self.batch.weight
        print "PS, inventory true: ", self.inventory 
        print "PS, inventory measured: ", self.measured_inventory
        
               
        self.write_to_log(facility,
            str(facility.total_campaign) + ' cycle completed\n\n\n')
        
        #print "time: " + str(facility.operation_time)
        
        facility.total_campaign = facility.total_campaign + 1 
        
       
        
        self.batch.weight = 0.0
        print "\n\n"
        # The size of the batch is returned. 


    def measured_inventory_calculation(self, facility):
        
        # only used at the end of a year, # also for the beginning inventory calculation
        
        sigma_measured_inventory = math.sqrt((float(self.inventory)*0.05/100.0)**2) # 500 - self.campaign... 
        print "std (product storage inventory) " + str(facility.total_campaign) +" : " + str(sigma_measured_inventory) #; expected value: 0.22360679775 kg
        
        self.write_to_log(facility, '\nInitial inventory verification of product storage')
        #self.increment_operation_time(facility, self.time_inspection)
        
        tmp = self.inventory + sigma_measured_inventory*np.random.randn()
        self.write_to_log(facility, '\nPhysical inventory: ' + str(tmp))  
              
        return tmp
        # mu + np.random.randn(...)*sigma for random samples from N(mu, sigma^2)
                                                       
               
        
         
        
        