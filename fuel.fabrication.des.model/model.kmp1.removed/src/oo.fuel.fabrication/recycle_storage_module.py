########################################################################
# Jieun Lee, R.A. Borrelli
# 06/03/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################
import pdb
import numpy as np

from facility_component_module import facility_component_class
from batch_module import batch_class

class recycle_storage_class(facility_component_class):
    """
    The recycle storage is the unit that takes in the batch and the heel when equipment failure occurs.
    A single batch (heal + batch) is moved to a recycle storage during repair, and is sent back to the melter.

    It also indefinitely holds onto SNM whenever an alarm is triggered. It accepts the material 
    from a key measurement point if the standard deviation of ID is higher than its expected value.  
    """

    def __init__(self, facility):
        
        
        self.batch = batch_class(0, "batch") 
        self.inventory_muf = 0
        self.inventory_2_melter = 0 
        self.measured_inventory = 0
        #self.inventory = 0
        
        self.time_delay = np.loadtxt(facility.process_states_dir+'/process.operation.time.inp',usecols=[1])[3] # 0.0833 days = 2 hours (recycle storage time) 
        facility_component_class.__init__(self, "recycle_storage", "storage", facility.inventory_odir)
        
        self.inventory_muf_output = open(facility.inventory_odir + '/inventory_muf.out','w+') 
        self.inventory_2_melter_output = open(facility.inventory_odir + '/inventory_2_melter.out','w+') 
        #self.inventory_output = open(facility.inventory_odir + '/inventory.out', 'w+')
   
    def process_batch(self, facility):
      
        self.write_to_log(facility,'Recycling batch and heel\n\n\n')
        self.increment_operation_time(facility, self.time_delay)
        
        print "total batch weight: ", self.batch.weight
        self.batch.description = "recycled batch"
        
                          
        # if(self.batch.weight == facility.kmp[2].batch.weight):
        #    self.inventory = self.inventory + self.batch.weight
        
        
        #self.inventory_output.write('%.4f\t%i\t%.4f\t%.4f\t%.4f\n'%(facility.operation_time, 
        #    facility.total_campaign, self.inventory, self.batch.weight, self.measured_inventory))
        #self.data_output.storage_output(facility, self)
        
        print "RS, true: ", self.batch.weight 
       # print "RS, inventory true: ", self.inventory 
        print "RS, inventory measured: ", self.measured_inventory
     
        
        
        return self.batch
        """
        This takes the batch and puts it into temporary storage.  Under the current code structure,
        everything in here soon gets sent either back into the melter (in the case of equpiment failure)
        or gets temporarily stored in it. (as is the case with facility alarms).
        """
        
        # In case of a false alarm ringing & melter failure: 
            
    def store_batch(self, facility, batchr):
        self.write_to_log(facility,'Storing %s in recycle storage \n\n\n' %(batchr.description))
        
        self.inventory_muf = self.inventory_muf + batchr.weight
        
        #self.measured_inventory = self.measured_inventory + kmp_weight
        print "RS, inventory_muf: ", self.inventory_muf
        print "RS, inventory_2_melter: ", self.inventory_2_melter
        print "\n\n"
        
        facility.total_campaign = facility.total_campaign + 1 
        
        self.inventory_muf_output.write('%.4f\t%i\t%.4f\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, self.inventory_muf, batchr.weight, self.measured_inventory))
         

        # In case of melter failure 
    def store_batch_2_melter(self, facility, batchr_2_melter):
        self.write_to_log(facility,'Storing %s in recycle storage \n\n\n' %(batchr_2_melter.description))
        
        self.inventory_2_melter = self.inventory_2_melter + batchr_2_melter.weight 
        
        print "RS, inventory_muf: ", self.inventory_muf
        print "RS, inventory_2_melter: ", self.inventory_2_melter
        print "\n\n"
        
        self.inventory_2_melter_output.write('%.4f\t%i\t%.4f\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, self.inventory_2_melter, batchr_2_melter.weight, self.measured_inventory))
        