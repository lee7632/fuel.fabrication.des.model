########################################################################
# Jieun Lee, R. A. Borrelli
# 05/28/2018
# v1.2**
########################################################################
#
# See class description
#
########################################################################

class batch_class:
    """
    This represents the bundle of SNM that gets passed from module to module.

    #######
    # Variables 
    #######
    
    weight = amount of SNM in batch (kg)
    description = string to aid in keeping track of what the batch is during logging. 
    
    """

    def __init__(self, weight, description):
        self.weight = weight
        self.description = description

    def add_weight(self, weight_2add):
        """
        Routine that changes the state variable. Can add a negative weight.
        """
        self.weight = self.weight + weight_2add
    
    def batch_pass(self):
        """
        This method is called up by the edge transition to help pass the amount of batch weight. 
        It returns the batch weight it's passing, then
        resets the batch weight to zero since it no longer has such.
        """
        batch_2_pass = self.weight
        self.weight = 0

        return batch_2_pass
    
    def batch_get(self, incoming_expected_batch_weight):
        """
        Like batch pass, this method is used by the edge transition to transfer the batch weight
        into the next object in the facility.
        """
        self.weight = incoming_expected_batch_weight
        
