**Equipment is a subset of process.**
**Processes are assembled into the system.**
<br>**System > Processes > Equipment**
<br><br>
**Process variables**
<br>Variables are listed in alphabetical order.
<br>A dummy variable means ones that are called in the function; i.e., multi-use.
<br>Variable list is for all files for the fuel fabrication model.
<br><br>true = actual material flow (unknown in reality)
<br>expected = expected material flow based on prior data cohorts
<br>measured = material flow recorded at each KMP
<br><br>**Postprocessing variable notes**
<br>Variables in postprocessing are mainly for making plots and not listed here.
<br>They are xmin, ymin, title, etc., and should be self-explanatory.
<br><br>
<ul>
<b>A</b>
<li>alarm_test = dummy for false alarm testing
</ul>
<ul>
<b>B</b>
</ul>
<ul>
<b>C</b>
<li>crucible_fraction = expected heel limits
</ul>
<ul>
<b>D</b>
<li>delay = dummy variable used in the functions for the time delays
<li>_dir = directory (*o = output, *g = figures)
<li>directory_path_file = contains the directory paths for input and output data
</ul>
<ul>
<b>E</b>
<li>end_of_campaign_inspection_time = end of campaign inspection time
<li>edge_transition = transfer time along each edge
<li>equipment_ = dummy variable for various equipment modules
<li>expected_quantity = dummy variable for expected weight measurements
<li>expected_kmpx = data file stores expected quantities at each KMP
<li>expected_storage_inventory = total expected mass in storage buffer
<li>expected_heel = expected material left in the crucible
<li>expected_processed_inventory = total expected mass processed
<li>_expected_muf = expected material unaccounted for per subsystem/equipment
<li>_equipment_time = time elapsed at each equipment/vertex 
<li>equipment_failure_event = boolean to indicate if a equipment failure occurred
<li>equipment_failure_number = number of failures that could occur in the equipment
<li>equipment_cleaning_time = time delay for the equipment to be cleaned
<li>equipment_failure_probability = associated probability for each equipment failure
<li>equipment_failure_maintenance_time = time for maintenance for each failure
</ul>
<ul>
<b>F</b>
<li>facility_operation = total number of days per year of facility operation 
<li>failure_event = boolean to indicate if a failure occurred
<li>failure_inspection_time = time to inspect due to failure
<li>_false_alarm_threshold = threshold to trigger a false alarm 
<li>_false_alarm_filename = name of file to output
<li>_failure_time = time recorded to determine equipment failure; if there is a failure, failure_time resets to 0; i.e., there is a new probability distribution
<li>file_= part of the file names for saving, opening, writing, etc.; i.e., file_tree is a directory structure
</ul>
<ul> 
<b>G</b>
<li>_graph = data files needed for plots
</ul>
<ul>
<b>H</b>
</ul>
<ul>
<b>I</b>
<li>inspection_time = time to inspect at end of campaign or upon failure
<li>inspection_time = contains all inspection times
<li>injection_casting_time = injecting casting normal operation time
</ul>
<ul>     
<b>J</b>
</ul>
<ul>
<b>K</b>
<li>kmp_time = time at each KMP to conduct a measurement
<li>kmp_identifier = for identifying the KMP locations
<li>kmp_threshold = threshold at each KMP determining a false alarm raise 
<li>kmp_uncertainty = uncertainty at KMP 
</ul>
<ul>
<b>L</b>
</ul>
<ul>
<b>M</b>
<li>maximum_kmp = maximum number of KMPs based on total processes
<li>measured_quantity = KMP measurements used for the false alarm tests
<li>measured_kmpx = stores quantities at each KMP
<li>measured_weight = measured weight of material
<li>measured_heel = measured material left in the crucible
<li>measured_storage_inventory = total measured mass in storage buffer 
<li>measured_processed_inventory = total measured mass processed
<li>_measured_muf = measured MUF per subsystem/equipment
</ul> 
<ul>
<b>N</b>
</ul>
<ul>
<b>O</b>
<li>_output is for output data files.
<li>operation_time = operation time of the facility (0 < T < facility_operation)
<li>_equipment_time = vertex operation times
</ul>
<ul>
<b>P</b>
<li>plot = data files needed to make plots
</ul>
<ul>
<b>Q</b>
</ul>
<ul>
<b>R</b>
</ul>
<ul>
<b>S</b>
<li>storage_inventory = current inventory in the storage buffer at time = T
<li>slug_trimming_time = slug trimming normal operation time
</ul>
<ul>
<b>T</b>
<li>threshold = MUF threshold (for alarms)
<li>total_failure = total counted failures
<li>total_campaign = total campaigns processed over facility_operation
<li>total_batch = total batches processed during facility_operation
<li>true_kmpx = stores true quantities at each KMP
<li>true_storage_inventory = total true mass in storage buffer
<li>true_heel = true material left in the crucible
<li>true_weight = true weight of material transferred through the system
<li>true_processed_inventory = total mass processed 
<li>_true_muf = true material unaccounted for per subsystem/equipment
<li>time_delay = time variable
<li>total_batch = batch size to be processed
</ul>
<ul>
<b>U</b>
<li>uncertainty = measurement uncertainty
<li>unprocessed_storage_inventory = total initial amount of material in the storage buffer
</ul>
<ul>
<b>V</b>
</ul>
<ul>
<b>W</b>
<li>weibull_beta_melter = beta parameter for the weibull distribution for failure testing
<li>weibull_eta_melter = eta parameter for the weibull distribution for failure testing
</ul>
<ul>
<b>X</b>
</ul>
<ul>
<b>Y</b>
</ul>
<ul>
<b>Z</b>
</ul>
