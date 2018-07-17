########################################################################
# Jieun Lee, R.A. Borrelli 
# 05/28/2018
# v1.0**
########################################################################
#
# Functions for the pyropocessing command and control main module.
#
########################################################################
#
# Import modules
#
import os     # This is to import the operating system dependent functionality. 
import shutil # High-level operations on files are offered through this module. 
#
########################################################################
#
# List of functions
#
# (1): Build data directories.
# (2): Copy files from 'lib directory' to 'home directory'.
# (3): Create a readme file for the simulation.
# (4): Write directory paths for the subsystem module. 
# (5): Make subdirectories.
# (6): Copy input files from 'default directory' to 'simulation directory'.
# (7): Write home directory information for a pyroprocessing simulation.
#
########################################################################

# (1): Build data directories.
def make_data_dir(home_dir, subsystem):

    print 'creating data directories'
    os.makedirs(home_dir)
    os.chdir(home_dir) # Change the current location to 'home_dir'
    os.makedirs(subsystem) # Create the directory called 'fuel.fabrication.' 

    input_dir = home_dir + '/' + subsystem + '/input' # Set input and output directories.
    output_dir = home_dir + '/' + subsystem + '/output' 

    os.makedirs(input_dir) # Make input and output directories. 
    os.makedirs(output_dir)

# Set input subdirectories.
    edge_transition_dir = make_subdirectory(input_dir, 'edge_transition') 
    failure_distribution_dir = make_subdirectory(input_dir, 'failure_distribution') 
    failure_equipment_dir = make_subdirectory(input_dir, 'failure_equipment') 
    kmps_dir = make_subdirectory(input_dir, 'kmps') 
    process_states_dir = make_subdirectory(input_dir, 'process_states') 
    system_false_alarm_dir = make_subdirectory(input_dir, 'system_false_alarm') 

# Create input subdirectories.
    os.makedirs(edge_transition_dir)
    os.makedirs(failure_distribution_dir)
    os.makedirs(failure_equipment_dir)
    os.makedirs(kmps_dir)
    os.makedirs(process_states_dir)
    os.makedirs(system_false_alarm_dir)

# Set output directories.
    data_dir = make_subdirectory(output_dir, 'data')
    figures_dir = make_subdirectory(output_dir, 'figures')

# Create output subdirectories.
    os.makedirs(data_dir)
    os.makedirs(figures_dir)

# Set output/data subdirectories.
    system_odir = make_subdirectory(data_dir, 'system')
    material_flow_odir = make_subdirectory(data_dir, 'material.flow')
    inventory_odir = make_subdirectory(data_dir, 'inventory')
    false_alarm_odir = make_subdirectory(data_dir, 'false.alarm')
    kmps_odir = make_subdirectory(data_dir, 'kmps')
    muf_odir = make_subdirectory(data_dir, 'muf')
    equipment_failure_odir = make_subdirectory(data_dir, 'equipment.failure')

# Set output/figures subdirectories.
    system_gdir = make_subdirectory(figures_dir, 'system')
    material_flow_gdir = make_subdirectory(figures_dir, 'material.flow')
    inventory_gdir = make_subdirectory(figures_dir, 'inventory')
    false_alarm_gdir = make_subdirectory(figures_dir, 'false.alarm')
    kmps_gdir = make_subdirectory(figures_dir, 'kmps')
    muf_gdir = make_subdirectory(figures_dir, 'muf')
    equipment_failure_gdir = make_subdirectory(figures_dir, 'equipment.failure')

# Make subdirectories under 'output/data.'
    os.makedirs(system_odir)
    os.makedirs(material_flow_odir)
    os.makedirs(inventory_odir)
    os.makedirs(false_alarm_odir)
    os.makedirs(kmps_odir)
    os.makedirs(muf_odir)
    os.makedirs(equipment_failure_odir)

# Make subdirectories under 'output/figures.'
    os.makedirs(system_gdir)
    os.makedirs(material_flow_gdir)
    os.makedirs(inventory_gdir)
    os.makedirs(false_alarm_gdir)
    os.makedirs(kmps_gdir)
    os.makedirs(muf_gdir)
    os.makedirs(equipment_failure_gdir)

    return(input_dir, output_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir, data_dir, figures_dir, system_odir, material_flow_odir, inventory_odir, false_alarm_odir, kmps_odir, muf_odir, equipment_failure_odir, system_gdir, material_flow_gdir, inventory_gdir, false_alarm_gdir, kmps_gdir, muf_gdir, equipment_failure_gdir)


# (2): copy files from lib directory to simulation directory
def copy_input_files(lib_dir, input_dir, subsystem, simulation_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir):
    default_dir = lib_dir + '/' + subsystem # Define the default directory as 'lib/fuel.fabrication.'
    os.chdir(default_dir) # Change the current location to the default directory.
	
# Copy input files from lib directory to simulation directory.
    copy_file('edge_transition', edge_transition_dir, default_dir)
    copy_file('failure_distribution', failure_distribution_dir, default_dir)
    copy_file('failure_equipment', failure_equipment_dir, default_dir)
    copy_file('kmps', kmps_dir, default_dir)
    copy_file('process_states', process_states_dir, default_dir)
    copy_file('system_false_alarm', system_false_alarm_dir, default_dir)

# Copy readme file for input data
    shutil.copy('readme.md', input_dir)
    return()

# (3): make a readme file for the simulation
def make_readme(home_dir):
    os.chdir(home_dir) # Move to simulation directory.
    readme_information = open('readme.md','w+') # Open the file. 

    readme_statement = raw_input('Enter a readme statement for the simulation: ') # Add the statement.
    readme_information.write(readme_statement) # Write to the file.

    readme_information.close() # Close the file. 
    return()

# (4): write directory paths for the subsystem module. 
def write_simulation_dir(root_dir, subsystem, input_dir, output_dir, edge_transition_dir, failure_distribution_dir, failure_equipment_dir, kmps_dir, process_states_dir, system_false_alarm_dir, data_dir, figures_dir, system_odir, material_flow_odir, inventory_odir, false_alarm_odir, kmps_odir, muf_odir, equipment_failure_odir, system_gdir, material_flow_gdir, inventory_gdir, false_alarm_gdir, kmps_gdir, muf_gdir, equipment_failure_gdir):
    os.chdir(root_dir + '/simulation/meta.data') # Paths should be stored in 'meta.data'

    simulation_dir_filename = subsystem + '_simulation.dir.inp' #Open the file.
    simulation_dir_file = open(simulation_dir_filename,'w+') 

# Write directories
    simulation_dir_file.write(input_dir + ',' + output_dir + ',' + edge_transition_dir + ',' + failure_distribution_dir + ',' + failure_equipment_dir + ',' + kmps_dir + ',' + process_states_dir + ',' + system_false_alarm_dir + ',' + data_dir + ',' + figures_dir + ',' + system_odir + ',' + material_flow_odir + ',' + inventory_odir + ',' + false_alarm_odir + ',' + kmps_odir + ',' + muf_odir + ',' + equipment_failure_odir + ',' + system_gdir + ',' + material_flow_gdir + ',' + inventory_gdir + ',' + false_alarm_gdir + ',' + kmps_gdir + ',' + muf_gdir + ',' + equipment_failure_gdir)
# Close file
    simulation_dir_file.close()
    return()
	
# (5): make subdirectories
def make_subdirectory(working_dir, subdirectory):
    dummy_subdirectory = working_dir + '/' + subdirectory
    return(dummy_subdirectory)


# (6): copy input files from 'default directory' to 'simulation directory'
def copy_file(local_dir, destination_dir, default_dir):
    local_subdir = default_dir + '/' + local_dir # Set the local subdirectory.
    
    os.chdir(local_subdir) # Change the current location to 'local_subdir.'
    
    for files in os.listdir(local_subdir):  # Return a list in the directory. 
	    shutil.copy(files, destination_dir) # Copy lib files to simulation files; shutil.copy(src, dst): copy the file src to the file or directory dst.

# Return to default directory for input data 
    os.chdir(default_dir)
    return()

# (7): Write home directory information for a pyroprocessing simulation.
def write_home_dir(root_dir, lib_dir, simulation_dir):
    os.chdir(root_dir) # Change the current location to the root directory.
    dir_check = os.path.isdir(root_dir + '/simulation') # Check if there is the directory called 'simulation.'

    if(dir_check == False): # If it is false, then create one. 
	    os.makedirs('simulation') 

    home_dir = root_dir + '/simulation/' + simulation_dir # Set the home directory where all the simulation data will go. 
    
# Change the current location to root_dir/simulation.
    os.chdir('simulation')
    dir_check = os.path.isdir('meta.data') # Check if there is a 'meta.data' file.

    if(dir_check == False): # If there is no 'meta.data' file, create it. 
	    os.makedirs('meta.data') # This directory will store the simulation directory information for the process module.

    if(os.path.isdir(simulation_dir)): # If the directory exists, wipe and write over it.
        shutil.rmtree(simulation_dir) # Delete an entire directory tree.
    
	os.makedirs(simulation_dir) 
    os.chdir('meta.data') # Change the directory to 'meta.data.'

    home_dir_file = open('home.dir.inp','w+')
    home_dir_file.write(home_dir)
    home_dir_file.close()
    return(home_dir)

# EOF
