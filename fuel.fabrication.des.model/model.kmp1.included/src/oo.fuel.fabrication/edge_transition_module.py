########################################################################
# Jieun Lee, R.A. Borrelli
# 05/28/2018
# v1.2
########################################################################
#
# See class description
#
########################################################################

import numpy as np
from facility_component_module import facility_component_class



class edge_transition_class(facility_component_class):
    """
    The edge transition serves as both the physical means by which the nuclear material travels from vertex to 
    vertex (component to component), but also as the communication link between components. In spite of the
    facility being set up in a hierchical decomposition, this is the one liaison that allows components
    to communicate laterally with each other.

    It also causes the appropriate time delay for that particular transition.

    The edge transition input file allows to put different time values for different edges, thus
    it is required to delineate which edge is being created.

    Edge number is indexed by zero.

    #######
    # Variables 
    #######
    
    time_delay = amount of time in days it takes for this specific edge to move the batch.
    
    """

    def __init__(self, facility, edge_number):
        self.time_delay = np.loadtxt(facility.edge_transition_dir + '/edge.transition.inp', usecols=[1])[edge_number] # 30 mins = 0.0208 days
        facility_component_class.__init__(self, "edge_transition", "manager", None) #inheritance
        
       
    def edge_transition(self, facility, batch, object1, object2):
        """
        This method is used to increment the time it takes to pass the physical batch from one object to another.

        Take a special note that when an object passes the batch, it resets
        its own batch weight to zero.
		
        """
        
        self.write_to_log(facility,'Edge transition: \nMoving %s from %s to %s \n\n'%(batch.description, 
            object1.description, object2.description))

        object2.batch.batch_get(object1.batch.batch_pass()) # 20 kg of a batch is passed. 
        
        print '\ntrue weight (previous): ' + str(object1.batch.weight)
        print 'true weight (after): ' + str(object2.batch.weight) +'\n'
        self.increment_operation_time(facility, self.time_delay) # Increment the time for the edge transition.
        
        
        
        
        
         
      