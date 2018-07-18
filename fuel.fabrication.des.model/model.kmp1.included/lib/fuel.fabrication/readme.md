**Input file description**
<br>
* The directory tree should be the same for each subsystem so the functions can be the same.
<br><br>
**edge.transition.inp**
<br>
* Time elapsed on an edge
<br>
* No state change
<br>
* starting.edge.location to ending.edge.location | edge transition time [d]
<br><br>
**weibull.beta.inp**
<br>
* Weibull: failure distribution used for the injection casting equipment 
<br>
* '1/lambda' is a failure rate parameter given for a specific equipment.
<br>
* failure type | beta value
<br><br>
**melter.failure.data.inp**
<br>
* It simulates melter failure.
<br>
* failure rate [1/d] | maintenance time [d] | cleaning time [d]
<br><br>
**key.measurement.points.inp**
<br>
* KMP activity
<br>
* kmp# | measurement time [d] | measurement uncertainty | measurement threshold
<br><br>
**batch.inp**
<br>
* Batch size for injection casting equipment
<br>
* batch size [kg]
<br><br>
**facility.operation.inp**
<br>
* Total operating days of the facility per year
<br>
* operating time [d]
<br><br>
**melter.crucible.fraction.inp**
<br>
* A random amount of material is always left in the crucible after operation.
<br>
* expected quantity [kg]
<br>
* upper limit of true quantity [kg]
<br>
* lower limit of true quantity [kg]
<br><br>
**process.operation.time**
<br>
* Time of operation for each vertex
<br>
* vertex | operation time [d]
<br><br>
**unprocessed.storage.inventory.inp**
<br>
* Starting with some amount of material in the storage buffer in the full pyroprocessing facility.
<br>
* This would be 10,000 kg at the beginning of operation.
<br>
* unprocessed material [kg]
<br><br>
**false.alarm.threshold.inp**
<br>
* Threshold to trigger a false alarm as part of operation
<br>
* operation event | threshold
<br><br>
**inspection.time.inp**
<br>
* Inspection time associated with each false alarm event
<br>
* operation event | inspection time [d]
