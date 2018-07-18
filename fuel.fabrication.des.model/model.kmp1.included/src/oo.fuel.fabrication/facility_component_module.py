########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
#
# This class contains methods that the facility will essentially use.  (Super class)
#
########################################################################

# Import modules 
import numpy as np
from data_output_module import data_output_class

class facility_component_class:
    """
    This class will get inherited by most of other classes.

    #######
    #  Variables
    #######
	
    data_output = module that handles data output for this class. It creates a data output file and
    contains methods for writing important data to such.

    description = a name that will be used in differentiating this object from any others of its kind.
    This gets used in identification in the log file as well as naming the output file where data
    for the specific class is written.

    Object type = a string describing the object type. Can be either "manager", "storage", "kmp", or "processor".
    Other methods utilize this in conditional statements.

    #######
    # Coding Notes  
    #######
    
    Note that if you don't want an object to have a data output file, simply pass "None" in for the output
    directory.
    
    """

	
    def __init__(self, description, object_type, output_dir):
        
        if output_dir != None:
            self.data_output = data_output_class(description, output_dir)  
        self.description = description
        self.object_type = object_type

    def write_to_log(self, facility, message):
        """
        Write a message to the log file carried by the facility.
        """
        facility.log_file.write(message)

    def increment_operation_time(self, facility, time_added):
        """
        This function increases the operation time by the desired amount indicated by time_added;
        it then logs the incremented operation time in the designated output file.

        inputs: facility class, amount of time to increase operation time (float)
        """
		
        facility.operation_time = facility.operation_time + time_added
        print 'operation time: ' + str(facility.operation_time)
        facility.system_time_output.write('%.4f\n'%(facility.operation_time))
        facility.system_info_output.write('%.4f\t%i\t%i\n'%(facility.operation_time, facility.total_campaign, facility.false_alarm_count))


    def check_equipment_failure(self, facility):

        """
        This method calculates the cumulative probability of an equipment failure.

        Currently, beta (or k, depending on who's syntax you use) is set to be 1.  That is the value
        used when the failure rate is constant over time, and then 1/lambda represents a general
        estimate of the failure rate (units of 1/days).

        Whether or not an actual failure occurs is determined by whether or not a randomly selected number between 0 and 1 from a uniform distribution 
		 is smaller than the calculated probability.
		      
        #######
        # Return 
        #######
        
        True = Equipment did fail. Need to run the failure routine.

        False = Equipment did not fail. The facility may continue to run as normal.

        *************DEVELOPER NOTES******************

        Any object that calls this method will need the attributes "time_of_last_failure"
        and "failure_rate". 
        
        """

        #######
        # Initialize the boolean 
        #######
        did_fail = False
        
        #######
        # The time used to calculate the probability is the time that has passed since the last failure. 
        #######
        time = facility.operation_time - self.time_of_last_failure 
        """
        print "operation time: " + str(facility.operation_time)
        print "time of last failure: " + str(self.time_of_last_failure)
        
        print "time: " + str(time)  
        """
        #######
        # The cumulative distribution function caclulated according to time 
        #######
        cdf = 1 - np.exp(-time * self.failure_rate)
        
        fail_check = np.random.rand() # It generates random samples from a uniform distribution over [0, 1) 

        #print "cdf: " + str(cdf)
        #print "fail_check: " + str(fail_check)

        if  fail_check <= cdf:
            did_fail = True
            self.time_of_last_failure = facility.operation_time
            self.failure_count = self.failure_count + 1

            self.failure_data_output.failure_output(facility, self, fail_check, cdf)
        
        return did_fail

  