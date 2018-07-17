########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
# 
# Storage buffer  
# 
########################################################################
#
# The storage buffer contains the materials to be processed by the fuel fabrication process.
# Uranium, TRUs with REFPs, and Zr arrive in the buffer at different times in different quantities.
# Fuel fabrication processes the materials into metal alloy fuel slugs with a prescribed batch size.
#
########################################################################
#
# Currently, the simulation starts off with a fixed amount of unprocessed material in the buffer.
# Eventually materials will enter the storage buffer in differing quantities at different times.
#
########################################################################
import numpy as np
import math

from facility_component_module import facility_component_class
from batch_module import batch_class

# This storage_buffer_module is a subclass. 
class storage_buffer_class(facility_component_class): # inheritance; facility_component_class is the super class. 

    """
    #######
    # Variables 
    #######
    batch_size = weight of a batch in kg 

    inventory = true amount of SNM that the storage buffer is holding in kg

    measured_inventory = measured amount of SNM 

    time_delay = amount of time it takes the storage buffer to create a batch

    storage_buffer = component module that handles storing the SNM and creating a batch.	
	 """

    def __init__(self, facility, initial_inventory):
        self.batch_size = np.loadtxt(facility.process_states_dir + '/batch.inp') # 20 KG
        self.inventory = initial_inventory # 10,000 KG
        
        self.batch = batch_class(self.batch_size, "batch")
        
        self.measured_inventory = self.measured_inventory_calculation(facility)
        print "Round (measured storage buffer inventory) " + str(facility.total_campaign) +" : " + str(self.measured_inventory)
        
        self.time_delay = np.loadtxt(facility.process_states_dir + '/process.operation.time.inp', usecols=[1])[0] #Storage buffer batch preparation time: 1 hour = 0.0417 
        self.time_inspection = 0.333333 # 8 hours of inspection; an input file for it is needed (two different inventories)
                
        facility_component_class.__init__(self, "storage_buffer", "storage", facility.inventory_odir) 

        #self.true_weight = 0
        
    def measured_inventory_calculation(self, facility):
        
        """
        Let's assume that 20 kg of SNM gets stored in a vessel.
        Therefore, total 500 vessels are stored in the buffer. 
        Weight meausurement is performed with each vessel using an electronic balance. 
        It is only at the beginning before the process starts. 
        """
                
        sigma_measured_inventory = math.sqrt(( 500 - facility.total_campaign + 1 )*(float(self.batch_size)*0.05/100.0)**2) # 500 - self.campaign... 
        #; expected value: 0.22360679775 kg
        
        self.write_to_log(facility, '\nInitial inventory verification of storage buffer')
        #self.increment_operation_time(facility, self.time_inspection)
        tmp = self.batch_size*( 500 - facility.total_campaign + 1) + sigma_measured_inventory*np.random.randn()
      
        self.measured_inventory = tmp 
        print "measured storage buffer inventory " + str(facility.total_campaign) +" : " + str(tmp)
        print "std:  " + str(sigma_measured_inventory)
        self.write_to_log(facility, '\nPhysical inventory: ' + str(tmp))
        
        return tmp
        # mu + np.random.randn(...)*sigma for random samples from N(mu, sigma^2)
         
    			   
    def batch_preparation(self, facility):
        """
        The storage buffer takes some SNM from its inventory, creates it into a batch, then passes such on
        to the next part.
        """
                        
        self.write_to_log(facility, 'Prepare batch in Storage Buffer for transfer: %.1f kg \n\n\n'%(self.batch.weight))
    
        if(self.inventory == 10000): # only the first time, you need the PIV time. 
            time = self.time_delay + self.time_inspection
            
        else: 
            time = self.time_delay
        
        self.increment_operation_time(facility, time) # Add one hour for the batch preparation.
        self.inventory = self.inventory - self.batch.weight 
        self.data_output.storage_output(facility, self) 
       
        # writing the output data.  true initial inventory, expected residual weight, measured inventory weight. 
         
        # self.true_weight = self.batch.weight
        
        print "SB, true: ", self.batch.weight
        print "SB, inventory true: ", self.inventory 
        print "SB, inventory measured: ", self.measured_inventory
        
        return self.batch # The size of the batch is returned. 

