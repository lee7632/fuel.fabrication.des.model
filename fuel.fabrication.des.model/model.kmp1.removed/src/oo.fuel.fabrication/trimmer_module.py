########################################################################
# Jieun Lee
# 05/28/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################
import numpy as np
from facility_component_module import facility_component_class
from batch_module import batch_class


class trimmer_class(facility_component_class):
    
    """
    The trimmer takes the quartz molds from the melter and sheers them to produce the metal slugs.
    The broken quartz molds are treated as a waste stream, and the metal slugs are sent into
    product storage, as they are the final product of the entire pyroprocessing system, much less the
    fuel fabrication process.

    For now, the trimmer doesn't experience equipment failure, nor does it lose any material during
    it's batch processing time.  It simply accepts the batch from the melter, increments
    the operation time accordingly, then passes the product along to the product storage.

    #######
    # Variables 
    #######
    time_delay = amount of time in days it takes to process the batch.
    """

    def __init__(self, facility):
        
        self.batch = batch_class(0, "batch")
        self.time_delay = np.loadtxt(facility.process_states_dir+'/process.operation.time.inp',usecols=[1])[2] # 0.125 days = 3 hours
                
        facility_component_class.__init__(self, "trimmer", "processor", None)
      
        
    def process_batch(self,facility):
        
        
        """
        See class description
        """
        
        self.write_to_log(facility,'Slug trimming\n')
        self.increment_operation_time(facility, self.time_delay)
        self.write_to_log(facility,'Failure status:  False \n\n\n')
        
        return self.batch
