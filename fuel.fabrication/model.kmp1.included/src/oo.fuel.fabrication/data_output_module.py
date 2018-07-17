########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################

import pdb

class data_output_class:
    """
    This class will contain functions that will be used for writing data to an output file. 
    
    """

    def __init__(self, object_description, output_dir):
        self.output_file = open(output_dir + '/' + object_description + '.out','w+') 
        # This is for opening a specific output file.

    def write_to_data_output(self, message): 
        # This is for writing the messages to the output files. 
        self.output_file.write(message) 

    def storage_output(self, facility, storage_object): 
        # For instance, 'storage_object' can be the class 'storage_buffer_class' type. 9980 kg, 9980 kg, 10,000kg 
        self.output_file.write('%.4f\t%i\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, storage_object.inventory, storage_object.measured_inventory))
        
    def failure_output(self, facility, processor, fail_check, cfd):
        self.output_file.write('%.4f\t%i\t%.4f\t%.4f\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, processor.time_of_last_failure, fail_check, cfd, processor.failure_count))

    def kmp_output(self, facility, kmp):
        self.output_file.write('%.4f\t%i\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, kmp.batch.weight, kmp.measured_weight))

    
    def processor_output(self, facility, processor):
        self.output_file.write('%.4f\t%i\t%.4f\t%.4f\t%.4f\n'%(facility.operation_time, 
            facility.total_campaign, processor.heel.weight, processor.true_batch_loss, processor.batch.weight))

    
    def muf_output(self, facility, kmp):
        self.output_file.write('%.4f\t%i\t%.4f\t %.4f\n'%(facility.operation_time,
            facility.total_campaign, facility.melter.heel.weight, kmp.muf))
        
# recycle storage (Special case)

   