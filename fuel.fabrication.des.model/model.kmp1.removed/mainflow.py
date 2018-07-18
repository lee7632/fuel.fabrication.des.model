########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
#
# This program will simulate the fuel fabrication process.
#
# True to the system diagram, U and TRU will get fed into the fuel
# fabricator. It then processes the SNM (special nuclear material)
# into metal slugs that are stored in the product storage. One batch that moves
# from the storage buffer through the system to the product storage counts
# as a single campaign. Once that occurs, a brief end of campaign
# inspection is held. Currently, if the material is stored in recycle storage, 
# it is also considered as a campaign.
#
#
########################################################################
#
# EDITOR'S NOTES:
#
# If you are viewing this code for one of the first times, we would recommend
# following the logic, file by file. Start with the facility command
# module, follow the initializing routine, and process batch, then view
# the called module as it comes up.
#
# This code tries to be as straightforward as possible while maintaining
# modularity and component hierarchy. The edge transition takes the batch 
# weight of object 1, passes it to object 2, then
# resets the batch weight of object 1.
#
# Most of the notes are found in the class and method descriptions. 
#
# Run 'simulation_set_up.py' first before you run 'main.py.'
#
########################################################################

# Import modules 
import numpy as np
import global_vars
import sys
import os

# The search path is inserted into path[0].
sys.path.insert(0, global_vars.root_dir + '/src/oo.fuel.fabrication') 
#sys.path.insert(1, global_vars.root_dir + '/simulation/test2/fuel.fabrication/output/data/muf/')

# Import a class from a module. 
from facility_command_module import facility_command_class 

#np.random.seed()


# Initialize facility
facility = facility_command_class(global_vars.root_dir, 'fuel.fabrication')


# Process the materials  
facility.write_to_log('Start facility operation\n')

# If the operation time passes 250 days, the oepration stops.  


while facility.operation_time <= 250: #facility.total_operation_time:  around 530 days. 
    facility.write_to_log('Starting campaign: %i at time:  %.4f  days \n\n' %(facility.total_campaign, facility.operation_time))   
    facility.process_batch()
    
facility.close_files()
facility.makePlots()
