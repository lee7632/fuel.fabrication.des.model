**Process model**
<br>There is a time lapse for each vertex and edge set in preprocessing.
<br>System variables are listed in the glossary.
<ol>
<b>Preprocessing</b>
<li>Input parameters are read in, and data files are open. 
<li>storage_inventory_start is loaded into the storage buffer at TIME = 0.
<br><br><b>Operation</b>
<li>Batch preparation in the storage buffer
<li>Edge transition from the storage buffer to KMP0
<li>Batch weight measurement at KMP0
<li>Edge transition from KMP0 to the melter 
<li>Melter process.
<ul>
<li>Failure Test

If failure starts the maintenance loop.
<ul>
<li> Edge transition form the melter to KMP3
<li> Batch weight measurement at KMP3 and comparison of MUF to expected MUF
<br>If MUF is above an alarm threshold, material is transferred to recycle storage for further inspection.
<li> Edge transition from KMP3 to the recycle storage
<li> Edge transition from recycle storage to KMP3
<li> Batch weight measurement at KMP3 and comparison of MUF to the alarm threshold
<br>If MUF is above the alarm threshold, material is transferred to recycle storage for further inspection. 
<li> Edge transition from KMP3 to the melter
</ul>
</ul>
<li>Edge transtion from the melter to KMP1
<li>Batch weight measurement at KMP1 and comparision of MUF to the alarm threshold
<br>If MUF is above the alarm threshold, material is transferred to recycle storage from KMP1 directly.
<li>Edge transition from KMP1 to the trimmer
<li>The trimming process only adds its processing time.  
<li>Edge transition from the trimmer to KMP2
<li>Batch weight measurement at KMP2 and comparision of MUF to the alarm threshold
<br>If MUF is above the alarm threshold, material is transferred to recycle storage from KMP2 directly.
<li>Edge transition from KMP2 to the product storage
<li>After every camapaign, maintenance time is added, and the heel is removed.

***Cleaning procedure is conducted to extract heel (part of failure routine).**
<br>***Maintenance happens to install a new melter.**

<b>postprocessing</b>
<li>close data files
<li>make plots of false alarm probability
</ol>
Data is written continutally with the write_output function as the code steps through the processes.
KMP data is only recorded at a KMP event with the kmp_write function.
Probability density function data is also written separately.
Output writing is clearly indicated in the code.

