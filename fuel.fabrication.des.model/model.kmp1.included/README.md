**DES modeling for the pyroprocessing system**
<br>
**Discrete event simulation description**
* In DES, each 'event' happens at a 'vertex.'
* There are state changes at vertices.
* State changes are assigning values to a variable or solving an equation.
* Parameters are variables needed to make state changes.
* DES steps discretely in time through each vertex via an 'edge.'
* At each vertex, the equations are run and the state variables change.
* The edges are dynamic and provide logical relationships between events.
* DES should readily lend itself to modeling of batch systems like pyroprocessing.
* Python is a natural fit for DES due to its modularity.

**Fuel fabrication v1.0**
* This is a 'bare bones' build, just to get the model working.
* Many assumptions are made and listed in the comments.

**Fuel fabrication v1.1**
* Upgraded to simulate the melter failure.

**Fuel fabrication v1.2**
* Upgraded to simulate the melter failure with the Weibull distribution.
* This version is ready for testing cases. 

**Fuel fabrication v1.3**
* Several sensitivity analyses varying facility input parameters were performed to verify the safeguardability of facility designs.  
* MUF calculation is optional at each KMP. 


**Command and control v1.0**
* This file controls directory creation and default input file transfers for all modules.


