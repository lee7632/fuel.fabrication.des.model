**MUF**
<br>
<ul>
<li>MUF stands for 'material unaccounted for'. It is also called 'inventory difference'.
<li>At KMP
<li>At the end of campaign
<li>On melter failure at KMP3 
</ul>

This will not be the case once diversion is introduced into the model since it would not be known if the MUF was in the melter or diverted. 
MUF is calculated by subtracting input data by output data.
<br>
<ul>
<b>At each KMP</b>
<li>MUF = weight measurement before the process - weight measurement after the process
<li>For the material balance area installed around the melter, MUF = batch weight at KMP0 - batch weight at KMP 1.
<li>We do not involve inventories since we assume materials are not stored in the material balance area for the melter. 
</ul>
<ul>
<b>Failure</b>
<li>MUF is also calculated at KMP3. 
<li>KMP3 records material transferred out of melter to recycle storage.
<li>MUF = batch weight at KMP0 - batch weight at KMP3
<li>or, MUF = batch weight at KMP3 - batch weight at KMP3 (when material is transferred back to recycle storage.)
</ul>
When the melter fails, it is cleaned, and the total batch including heel is removed. MUF is accounted at KMP3, and the material is transferred to recycle storage until maintenance is completed.
<br>
<br>
<ul>
<b>Note that MUF calculation at KMP3 is needed twice.</b>
<li>KMP3 measures batch from melter
<li>KMP3 also measures batch from recycle storage (After maintenance, batch is moved back to the melter from recycle storage. 
</ul>
The heel is the amount of material that accumulates in the melter (crucible), randomly during each melting event.
<br>Maintenance is conducted.
<ul>
<br>
<b>When MUF is above a threshold, an alarm is raised, and the material is moved to recycle storage.</b> 
<li>Confirm all the material is in the recycle storage, and MUF = 0.
<li>An default alarm thresholds are set so that the false alarm probability is equal to 0.05. 
<li>Heel is not accumulated after a campaign (Later on, heel must be accumulated throughout the operation time.)
</ul>
<ul>
<b>Accumulation of sequential IDs happens every campaign, and the alarm threshold is 2.4 kg of Pu.
</ul>