**Introduction**
<br><br>This is the discrete event simulation (DES) module for the fuel fabrication system in pyroprocessing.
<br>U, TRU, and Zr arrive into a storage buffer first.
<br>Materials are melted by injection casting to form metal rods.
<br>The metal rods are trimmed to make fuel slugs.
<br>The fuel slugs are 'processed' and stored in a final storage bufer.
<br><br>The fuel fabrication process is complex due to measurement events at KMPs, equipment failures, subsequent maintenance, false alarms, etc.
The code tracks inventories, batch weight per campaign, materials unaccounted for (MUF), along with all the above.
<br><br>The operation goal is to process as many products within the operation time. Equipment failures would affect operational goals due to maintenance delays.
Safeguardability comes in because plutonium is being processed in the facility. While processing as much material as possible, minimizing potential false alarms with reasonable false alarm probilities would be needed. 
<br><br>It is largely a matter of materials accounting and tracking operation time. Accurate materials accounting is essential to safeguardability. It is intended that this initial code is a test run for fuel fabrication and DES.
Later, this will integrate other pyroprocessing subsystems to form the full safeguardability assessment model.


**Simulation notes**
<br>One campaign = processing of one batch.
<br>1 time unit = 1 day.
<br>Mass is based on kg.
<br>Results: number of processed material, number of campaigns, false alarm probabilities, number of melter failure

**Vertices** 
<br>0. storage
<br>1. melter / injection casting 
<br>2. trimmer
<br>3. recycle
<br>4. product
<br>x. maintenance
<br><br>State changes only occur at these vertices. In reality, the true weight is unknown. Maintence is outside of the main process loop because it is triggered on an equipment failure. 
Currently, material would not flow to maintenance. Cleaning is needed to remove the heel from the melter. Equipment cannot be removed for maintenance unless SNM is cleaned out.

**System diagram**
<br>It contains the flow diagram of the facility and includes various results obtained by performing sensitivity analyses on differnet facility input parameters. 
<br><br>KMP(0): storage transfer to melter
<br>KMP(1): melter to trimmer
<br>KMP(2): trimmer to final processing
<br>KMP(3): melter to recycle
<br>or, KMP(3): recycle back to melter
<br><br>The KMPs will eventually be able to be turned 'on' or 'off' for different facility configurations.
<br>Then, the model is run to quantify the safeguardability of each design proposal. 

