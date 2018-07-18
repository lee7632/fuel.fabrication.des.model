########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
#
# Functions defined in the 'command and control' module are used.
# This file will set up all input/output directories and allow for input parameter editing.
#
########################################################################

# Import modules 
import os      # This is to import the operating system dependent functionality. 
import shutil  # High-level operations on files are offered through this module. 
import sys     # It has an access to some variables used by the interpreter. 

# Insert the specific search path to the first item of this list, path[0]. 
sys.path.insert(0, os.getcwd() + '/src/command.and.control') 
# os.getcwd() gets the address of the directory which contains this file. 

# Import the module named 'pyroprocessing_command_functions' as 'command_and_control.'
import pyroprocessing_command_functions as command_and_control

""" 
This function rewrites the 'file_to_change' with a new root directory and a simulation directory.
This is used for running a main flow program from any folder after a new root directory for the source code is determined.

"""
 
def edit_global_vars(file_to_change, new_root_dir, new_simulation_dir):
  
    with open(file_to_change,'r') as input_file, open(new_root_dir + '/new_temp.txt','w') as output_file: 
    # Set 'global_vars.py' to the input file and 'new_temp.txt' to the output file.  
        for line in input_file: # Read the file line-by-line. 
            if line[0:10] == 'root_dir =': # If there is the root directory defined, change it to a new root directory. 
                output_file.write('root_dir = "%s"\n'%(new_root_dir)) 
            elif line[0:16] == 'simulation_dir =': # If there is the simulation directory defined, change it to a new simulation directory.  
                output_file.write('simulation_dir = "%s/simulation/%s"\n'%(new_root_dir, new_simulation_dir))
            else:
                output_file.write(line) # Copy other lines to 'new_temp.txt.'
    shutil.move(new_root_dir + '/new_temp.txt', file_to_change)  # Move the contents from the output file to the 'global_var.py' 

########################################################################


# Start command and control
print 'Starting the command and control module for the pyroprocessing system.'
print '*******NOTICE FOR NEW USERS************\n'
print 'The "root directory" refers to the directory that contains "mainflow.py".\n \
The "simulation directory" is the directory that this program will create to hold input and output data from \n \
the simulations that you run.\n'


# Get the address of the root directory. 
root_dir = os.getcwd()
print 'root dir is: ', root_dir

# Set the root directory. 
change_directory_input = raw_input('Would you like to change the root directory (y/n)? ')

if change_directory_input == 'y':
    root_dir = raw_input('Please enter the desired root directory: ')

# Set the address of the lib directory.  
lib_dir = root_dir + '/lib'


# Set the simulation directory
simulation_dir = raw_input('Please enter the desired simulation directory name: ')


print '\nChanging global variables in %s'%(root_dir) 

# This is for changing global variables in 'global_vars.py.' 
# 'global_vars.py' is stored in 'root_dir.'
# Use the function called 'edit_global_vars.' This function is defined at the top of this file.  
edit_global_vars(root_dir + '/global_vars.py', root_dir, simulation_dir)

# Set the home directory where all the simulation data will go.
home_dir = command_and_control.write_home_dir(root_dir, lib_dir, simulation_dir)
print home_dir + "\n"
########################################################################
#
# Start the fuel fabrication module
#
########################################################################


# Set the file trees.
input_dir, output_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir, data_dir, figures_dir, system_odir, material_flow_odir, inventory_odir, false_alarm_odir, kmps_odir, muf_odir, equipment_failure_odir, system_gdir, material_flow_gdir, inventory_gdir, false_alarm_gdir, kmps_gdir, muf_gdir, equipment_failure_gdir = command_and_control.make_data_dir(home_dir,'fuel.fabrication')

# Copy lib input files to home directory.
command_and_control.copy_input_files(lib_dir, input_dir, 'fuel.fabrication', simulation_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir)

# Make readme file.
command_and_control.make_readme(home_dir)

# Write directory paths for the subsystem module. 
command_and_control.write_simulation_dir(root_dir, 'fuel.fabrication', input_dir, output_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir, data_dir, figures_dir, system_odir, material_flow_odir, inventory_odir, false_alarm_odir, kmps_odir, muf_odir, equipment_failure_odir, system_gdir, material_flow_gdir, inventory_gdir, false_alarm_gdir, kmps_gdir, muf_gdir, equipment_failure_gdir)


# Change back to the root directory so users won't be confused. 
os.chdir(root_dir)

########################################################################
#
# End fuel fabrication module
#
########################################################################
