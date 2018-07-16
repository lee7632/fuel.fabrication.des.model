########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2
########################################################################
#
# See class description
#
########################################################################

# Import modules
import pdb # python debugger 

import numpy as np 
import matplotlib.pyplot as plt
import math

from matplotlib import rc


from product_storage_module import product_storage_class
from storage_buffer_module import storage_buffer_class
from key_measurement_point_module import key_measurement_point_class as kmp_class
from edge_transition_module import edge_transition_class
from melter_module import melter_class
from trimmer_module import trimmer_class
from recycle_storage_module import recycle_storage_class

from batch_module import batch_class
from data_output_module import data_output_class

class facility_command_class:
    """
    This class represents the entire facility.  

    Initializing this object in a script starts up the entire facility, 
    which includes a large number of initializations that are derived from the input 
    files set by 'command and control'.

    #######
    # Variables 
    #######
    
    operation_time = current amount of time in days that have passed. Each method increments this by some
    amount.
    
    total_campaign = essentially the number of batches that have been processed. Each time a batch goes through
    the entire fuel fabrication process, this number gets incremented.

    measured_muf = used to determine how much muf resides in the MBA unit as calculated
    by the deficit in the material coming in and out.

    false_alarm_count = number of times that a false alarm has been triggered.  This number is particularly
    important for our results. 
    
    melter_did_fail = boolean to let the facility know whether or not the melter has failed in the
    given campaign.  
    
    did_conduct_inspection = boolean flag set when an inspection was conducted. 

    log_file = file where every important activity gets written to. This is the main file used to determine
    how operations occurr after the program is run.

    root_dir = main directory which contains all associated files.

    subsystem = subsystem of the entire facility. For now, this can only
    be fuel fabrication.

    total_operation_time = total amount of time in days that the facility will run for. Once operation time
    has reached this number, the program will stop.

    end_of_campaign_time_delay = amount of time it takes to conduct inspections at the end of each campaign.  

    end_of_campaign_alarm_threshold = weight of SNM in kg that will trigger the alarm. This number is
    compared to the accumulated sequential MUFs.  

    facility_inspection_time = amount of time in days it takes to inspect the entire facility when an alarm
    is triggered.

    system_time_ouput = output file where just the operation time is written to. Used for plotting.

    campaign_output = same as above only for the campaign number.

    initial_inventory = total amont of SNM used at the beginning. 

    """ 
    
    def __init__(self, root_dir, subsystem):
        
        """
        Although large, all this part does is to read in the number of input files required to start up the
        facility. 
        
        """
        # variable initiation
        self.operation_time = 0
        self.total_campaign = 1
        
        self.measured_muf = 0
        self.false_alarm_count = 0
        self.melter_did_fail = False
        self.did_conduct_inspection = False 
                
        self.log_file = open(root_dir + '/log.txt','w')
        self.root_dir = root_dir
        self.subsystem = subsystem
       
        self.sequential_muf = 0.0
        self.failure_check = False
        self.total_muf_cal = 0
        self.muf_cal_1 = 0 
        self.muf_cal_2 = 0
        self.muf_cal_3 = 0 
        
        self.false_alarm_count_1 = 0
        self.false_alarm_count_2 = 0 
        self.false_alarm_count_3 = 0 
        self.melter_failure_count = 0 
        # Begin Preprocessing
        self.log_file.write('Fuel fabrication \n\nPREPROCESSING\n')
       
        
        # Get a home directory path. 
        home_dir = open(self.root_dir+'/simulation/meta.data/home.dir.inp').read()  
        
        # Get directory paths. 
        directory_path_file = open(self.root_dir+'/simulation/meta.data/fuel.fabrication_simulation.dir.inp').readlines() 
        
        directory_paths=directory_path_file[0].split(',') #split path data and set directories.
        
        # Get directory paths for input & output files. 
        self.input_dir = directory_paths[0]
        self.output_dir = directory_paths[1]
        
        # Get paths for subdirectories in 'input' directory.
        self.edge_transition_dir = directory_paths[2]
        self.failure_distribution_dir = directory_paths[3]
        self.failure_equipment_dir = directory_paths[4]
        self.kmps_dir = directory_paths[5]
        self.process_states_dir = directory_paths[6]
        self.system_false_alarm_dir = directory_paths[7]
        
        # Get paths for directories in 'output' directory.
        self.data_dir = directory_paths[8]
        self.figures_dir = directory_paths[9]
        
        # Get paths for directories in 'data' directory.
        self.system_odir = directory_paths[10]
        self.material_flow_odir = directory_paths[11]
        self.inventory_odir = directory_paths[12]
        self.false_alarm_odir = directory_paths[13]
        self.kmps_odir = directory_paths[14]
        self.muf_odir = directory_paths[15]
        self.equipment_failure_odir = directory_paths[16]
        
        # Get paths for directories in 'figures' directory.
        self.system_gdir = directory_paths[17]
        self.material_flow_gdir = directory_paths[18]
        self.inventory_gdir = directory_paths[19]
        self.false_alarm_gdir = directory_paths[20]
        self.kmps_gdir = directory_paths[21]
        self.muf_gdir = directory_paths[22]
        self.equipment_failure_gdir = directory_paths[23]
        
        
        # Read input data 
        self.total_operation_time = np.loadtxt(self.process_states_dir+'/facility.operation.inp') #250 days, np.loadtxt loads data from a text file.   
        self.end_of_campaign_time_delay = np.loadtxt(self.system_false_alarm_dir+'/system.inspection.time.inp', usecols=[1]) # End of campaign inspection time: 4 hours = 0.1667 days. 'usecols' defines which columns to read.
        self.end_of_campaign_alarm_threshold = np.loadtxt(self.system_false_alarm_dir+'/eoc.alarm.threshold.inp') # Threshold = 2.4kg.
        self.facility_inspection_time = np.loadtxt(self.system_false_alarm_dir+'/facility.inspection.time.inp') # 4 hours = 0.1667 days
        self.initial_inventory = np.loadtxt(self.process_states_dir+'/unprocessed.storage.inventory.inp') # 10,000 KG
  
       
    
        # Open output files
        self.system_time_output = open(self.system_odir+'/facility.operation.time.out','w+') # facility operation time output file
        self.system_info_output = open(self.system_odir+'/system_info.out','w+') # facility operation time, # of campaign, # of false alarms
        self.muf_check_output =  open(self.kmps_odir+'/muf_check.out', 'w+') # muf info
        
        
        
        # Write data to output files  
        self.system_time_output.write('%.4f\n'%(self.operation_time))
        self.system_info_output.write('%.4f\t%i\t%i\n'%(self.operation_time, self.total_campaign, self.false_alarm_count))

        
         # Initialize facility components 
        self.storage_buffer = storage_buffer_class(self, self.initial_inventory)
        self.melter = melter_class(self)
        self.trimmer = trimmer_class(self)                
        self.product_storage = product_storage_class(self)       
        self.recycle_storage = recycle_storage_class(self)
 
                
        # Initialize the edge transition. 
        self.edge = edge_transition_class(self, 0)
		 
                
		 # Initialize key measurement points.
        self.kmp = []
        for n in range(4): # 0,1,2,3
            self.kmp.append(kmp_class(self, n))
        
        # total amount of heel + batch initilization 
        
        self.total = batch_class(0, "total")
        
        
        # Log end of Preprocess
        self.log_file.write('\n\nEND PREPROCESSING \n\n\n')

       
        
             
########################################################################

  
    def process_batch(self):
               
        """
        Method that processes the batch.  This acts as a liason between the component modules that
        do all the leg work.
        """
        
        batch = self.storage_buffer.batch_preparation(self) # Get the batch class with the size and the description. 
        self.edge.edge_transition(self, batch, self.storage_buffer, self.kmp[0]) 
       
        batch0 = self.kmp[0].process_batch(self) # measure the weight of the batch.
        self.edge.edge_transition(self, batch0, self.kmp[0], self.melter)
        
        self.failure_check, batchm, heelm = self.melter.process_batch(self)
        # print 'batchm.weight' + str(batchm.weight)
        
        if  self.failure_check == True: 
            print "melter fails!"
            self.melter_failure_count = self.melter_failure_count + 1 
            
            self.equipment_failure(self, batchm, heelm) 
        
        else: 
            self.edge.edge_transition(self, batchm, self.melter, self.kmp[1])
            #print self.melter.batch.weight 
            #print self.kmp[1].batch.weight
        
            batch1 = self.kmp[1].process_batch(self)
            
            muf_check1 = self.kmp[1].muf_check(self)
            print "alarm: " + str(muf_check1) 
            print "total_alarm: " + str(self.false_alarm_count)     
            
            if muf_check1 == True: 
                self.edge.edge_transition(self, batch1, self.kmp[1], self.recycle_storage)
                batchr = self.recycle_storage.process_batch(self)
                self.recycle_storage.store_batch(self, batchr)
                
                batchr.weight = 0.0
                batch.weight = 20.0
                heelm.weight = 0.0                 
                
            else: 
                self.edge.edge_transition(self, batch1, self.kmp[1], self.trimmer)
                batcht = self.trimmer.process_batch(self)
                print "true weight (trimmer): " + str(batcht.weight)
                self.edge.edge_transition(self, batcht, self.trimmer, self.kmp[2])
                    
                batch2 = self.kmp[2].process_batch(self)
        
                muf_check2 = self.kmp[2].muf_check(self)
                print "alarm: " + str(muf_check2)
                print "total_alarm: " + str(self.false_alarm_count)
            
                if muf_check2 == True:
                    self.edge.edge_transition(self, batch2, self.kmp[2], self.recycle_storage)
                    batchr = self.recycle_storage.process_batch(self)
                    self.recycle_storage.store_batch(self, batchr)
                    
                    batchr.weight = 0.0
                    batch.weight = 20.0
                    heelm.weight = 0.0                 
                
                else:
                    self.edge.edge_transition(self, batch2, self.kmp[2], self.product_storage) 
                    self.product_storage.process_batch(self)
        
                    batch.weight = 20.0 # initialization
                    heelm.weight = 0.0
        
        
        print "sequential muf: " + str(self.sequential_muf)
        print "total heel weight: " + str(self.melter.sum) 
        
        print "total muf check: " + str(self.total_muf_cal)
        print "muf 1 check: " + str(self.muf_cal_1)
        print "muf 2 check: " + str(self.muf_cal_2)
        print "muf 3 check: " + str(self.muf_cal_3) 
        
        print "total alarms at kmp 1: " + str(self.false_alarm_count_1) 
        print "total alarms at kmp 2: " + str(self.false_alarm_count_2) 
        print "total alarms at kmp 3: " + str(self.false_alarm_count_3)
        print "total alarms: " + str(self.false_alarm_count)
        
        print "total melter failure counts: " + str(self.melter_failure_count)
        
        self.muf_check_output.write('%i\t%i\t%i\t%i\t%i\t%i\t%i\t%i\n'%(self.total_muf_cal, self.muf_cal_1, self.muf_cal_2, self.muf_cal_3, self.false_alarm_count_1, self.false_alarm_count_2, self.false_alarm_count_3, self.false_alarm_count))
      
        if self.sequential_muf > 2.4: 
            sys.exit("Sequential ID is above 2.4 kg")  
        
        self.sequential_muf = 0.0
        
        
    def equipment_failure(self, facility, batchm, heelm):
      
        """
        The routine that occurs when the melter fails.  The 'batch + heel' is sent to the recycle storage, and the melter is fixed.
        Afterwards, the 'batch + heel' is back to the melter, and normal operation starts.
                
        """
        self.total.weight = batchm.weight + heelm.weight 
        self.melter.clean_material(self)
        self.edge.edge_transition(self, self.total, self.melter, self.kmp[3])
        batch3 = self.kmp[3].process_batch(self)
        
        variable = self.kmp[3].measured_weight # previous check up may be needed. 
                
        muf_check3 = self.kmp[3].muf_check(self)
        print "alarm: " + str(muf_check3)
        print "total_alarm: " + str(self.false_alarm_count)
        
        if muf_check3 == True: 
            self.edge.edge_transition(self, self.total, self.kmp[3], self.recycle_storage)
            batchr = self.recycle_storage.process_batch(self)
            self.recycle_storage.store_batch(self, batchr)
            self.melter.repair(self)
            
            batchr.weight = 0.0
            self.storage_buffer.batch.weight = 20.0
            heelm.weight = 0.0
 
        else:
            self.edge.edge_transition(self, self.total, self.kmp[3], self.recycle_storage)
            batchr_2_melter = self.recycle_storage.process_batch(self)
            self.recycle_storage.store_batch_2_melter(self, batchr_2_melter)
            self.melter.repair(self)
                      
            self.edge.edge_transition(self, batchr_2_melter, self.recycle_storage, self.kmp[3])
            batch3_2_melter = self.kmp[3].process_batch(self)
            
            muf_check_2_melter = self.kmp[3].muf_check_2_melter(self, variable)
            print "alarm: " + str(muf_check_2_melter)
            print "total_alarm: " + str(self.false_alarm_count)
            
            if muf_check_2_melter == True:
                self.edge.edge_transition(self, batch3_2_melter, self.kmp[3], self.recycle_storage)
                batchr = self.recycle_storage.process_batch(self)
                self.recycle_storage.store_batch(self, batchr)
                
                batchr.weight = 0.0
                self.storage_buffer.batch.weight = 20.0
                heelm.weight = 0.0
                
            else:
                self.edge.edge_transition(self, batch3_2_melter, self.kmp[3], self.melter)
                batchm2, heelm2 = self.melter.process_batch_without_failure_checkup(self)          
                self.edge.edge_transition(self, batchm2, self.melter, self.kmp[1])
            
                #print self.melter.batch.weight 
                #print self.kmp[1].batch.weight
        
                batch1 = self.kmp[1].process_batch(self)
            
                muf_check1 = self.kmp[1].muf_check(self)
                print "alarm: " + str(muf_check1) 
                print "total_alarm: " + str(self.false_alarm_count)     
            
                if muf_check1 == True: 
                    self.edge.edge_transition(self, batch1, self.kmp[1], self.recycle_storage)
                    batchr = self.recycle_storage.process_batch(self)
                    self.recycle_storage.store_batch(self, batchr)
             
                    self.storage_buffer.batch.weight = 20.0
                    heelm.weight = 0.0
                    batchr.weight = 0.0
                    heelm2.weight = 0.0
                
                else: 
                    self.edge.edge_transition(self, batch1, self.kmp[1], self.trimmer)
                    batcht = self.trimmer.process_batch(self)
                    print "true weight (trimmer): " + str(batcht.weight)
                    self.edge.edge_transition(self, batcht, self.trimmer, self.kmp[2])
                    
                    batch2 = self.kmp[2].process_batch(self)
        
                    muf_check2 = self.kmp[2].muf_check(self)
                    print "alarm: " + str(muf_check2)
                    print "total_alarm: " + str(self.false_alarm_count)
            
                    if muf_check2 == True:
                        self.edge.edge_transition(self, batch2, self.kmp[2], self.recycle_storage)
                        batchr = self.recycle_storage.process_batch(self)
                        self.recycle_storage.store_batch(self, batchr)
             
                        self.storage_buffer.batch.weight = 20.0
                        heelm.weight = 0.0 
                        batchr.weight = 0.0
                        heelm2.weight = 0.0
                
                    else:
                        self.edge.edge_transition(self, batch2, self.kmp[2], self.product_storage)
                        self.product_storage.process_batch(self)
                        
                        self.storage_buffer.batch.weight = 20.0 # initialization
                        heelm.weight = 0.0
                        heelm2.weight = 0.0
    
    
    def cumuf_check(self):
         
        print "\n\ntrue inventory (storage buffer): " + str(self.storage_buffer.inventory) 
        print "initial measured inventory (storage buffer): " + str(self.storage_buffer.measured_inventory)
        self.storage_buffer.measured_inventory_calculation(self)
        print "final measured inventory (storage buffer): " + str(self.storage_buffer.measured_inventory)
        print "\n\n"        
        
        
        #print "true inventory (recycle storage): " + str(self.recycle_storage.inventory) 
        #print "measured inventory (recycle storage): " + str(self.recycle_storage.measured_inventory)
                
        
    def write_to_log(self, message):
       
        #Self explanatory method.  A simple way to quickly write to the log file.
        self.log_file.write(message)
        
        
    
    def close_files(self):
        """
        Close the files used for logging events and data output.
        """
        
        self.log_file.close()
        self.system_time_output.close()
        self.system_info_output.close()
        self.melter.failure_data_output.output_file.close()
        self.kmp[1].muf_data_output1.close() 
        self.kmp[2].muf_data_output2.close()
        self.kmp[3].muf_data_output3.close() 
        self.recycle_storage.inventory_muf_output.close()
        self.recycle_storage.inventory_2_melter_output.close()
       # self.recycle_storage.inventory_output.close()
        
        
        self.storage_buffer.data_output.output_file.close() 
        self.product_storage.data_output.output_file.close()
        self.muf_check_output.close() 
        
    
    def makePlots(self):
        
        #Routine that will get called by mainflow that causes the facility to make all relevant plots.
        
        #xData = np.loadtxt(self.system_odir+'/facility.campaign.out',usecols=[0])
        #yData = np.loadtxt(self.system_odir+'/facility.campaign.out',usecols=[1])
        #xData = np.loadtxt(self.equipment_failure_odir+'/melter_failure_data.out',usecols=[0])
        #yData = np.loadtxt(self.equipment_failure_odir+'/melter_failure_data.out',usecols=[5])
        #self.plotData(xData, "Operation Time (days)", yData, "# of failures", 
        #    r'Melter failure count: $\lambda$ = %.3f (fails/day)'\
        #        %(self.fuel_fabricator.melter.failure_rate))
        xData = np.loadtxt(self.system_odir+'/system_info.out',usecols=[0])
        yData = np.loadtxt(self.system_odir+'/system_info.out',usecols=[2])
        self.plotData(xData, "Operation Time (days)", yData, "# of false alarms", 
            r'False alarm count: $\lambda$ = %.3f (fails/day)'%(self.melter.failure_rate)) 
            #$\Delta_{threshold}$ = %.2f (kg)'\
            #    %(self.melter.failure_rate, self.kmp[0].uncertainty, self.end_of_campaign_alarm_threshold))

    def plotData(self, xData, xLabel, yData, yLabel, plotTitle):
        
       # Plots the data
        
        plt.plot(xData, yData)
        plt.title(plotTitle)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.axis([xData[0], xData[-1], yData[0], yData[-1] + 1])
        plt.show()


 