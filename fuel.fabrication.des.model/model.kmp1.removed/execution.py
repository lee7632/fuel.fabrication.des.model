# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 11:15:21 2017
@author: Jieun

This file is to automatically run the mainflow.py 1000 times. 

"""
import global_vars
import os



def simplecount(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    return lines

j = 1
k = 1
l = 1
c = 1

for i in range(0,1000):
    
    execfile("mainflow.py")
    
    # system_info output
    os.chdir(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/system')

    n = simplecount('system_info.out')
    #print n # This it for counting the total number of lines. 
    
    
    original_file = open(root_dir + '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/system/system_info.out',"r")
    copy_file = open(root_dir+ '/simulation/1000.test.runs/final_output',"a")
    
    lines = original_file.readlines()
    copy_file.write(str(j) +'\t'+ lines[n-1])
    j = j + 1     
        
    original_file.close()   
    copy_file.close()
    
    
    # melter failure data output
    os.chdir(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/equipment.failure')

    n2 = simplecount('melter_failure_data.out')
    #print n2
    
    
    original_file_2 = open(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/equipment.failure/melter_failure_data.out',"r")
    copy_file_2 = open(root_dir + '/simulation/1000.test.runs/melter_failure',"a")
    
    lines_2 = original_file_2.readlines()
    
    copy_file_2.write(str(k) +'\t'+ lines_2[n2-1])
    k = k + 1
    
    original_file_2.close()   
    copy_file_2.close()
    
    
    #muf data 
    os.chdir(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/kmps')

    n3 = simplecount('muf_check.out')
    #print n3
    
    
    original_file_3 = open(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/kmps/muf_check.out',"r")
    copy_file_3 = open(root_dir + '/simulation/1000.test.runs/muf',"a")
    
    lines_3 = original_file_3.readlines()
    
    copy_file_3.write(str(l) + '\t' + lines_3[n3-1])
    l = l + 1
    
    original_file_3.close()
    copy_file_3.close()
    
    # processed material data 
    os.chdir(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/inventory')
    
    n4 = simplecount('product_storage.out')
    #print n4
    
    
    original_file_4 = open(root_dir+ '/simulation/' + simulation_dir + '/fuel.fabrication/output/data/inventory/product_storage.out',"r")
    copy_file_4 = open(root_dir+ '/simulation/1000.test.runs/product_storage',"a")

    lines_4 = original_file_4.readlines()
    
    copy_file_4.write(str(c) +'\t' + lines_4[n4-1])
    c = c + 1
    
    original_file_4.close()
    copy_file_4.close()
    
    os.chdir(root_dir)
   
