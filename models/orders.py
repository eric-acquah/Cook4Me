"""
Logic for orders are defined in this module

"""

from models.base import BaseModel


class OrderModel(BaseModel):
    """
    This class defines how client orders are processed

    """

    status = ['created', 'delivered', 'active', 'completed', 'cancelled']

    def __init__(self, *args, **kwargs):
        """
        Initialize order instances

        """
        
        super().__init__(*args, **kwargs)

        if not kwargs:
            self.client_id = None
            self.cook_id = None
            self.order_id = self.id
            self.request = {
                'request_head': "",
                'request_desc': ""
            }
            self.order_status = OrderModel.status[0]


    def createOrder(self, cookid, order_head, order_desc=""):
        """
        Creates and saves a new order

        Args:
            cookid: (str): id of cook whom the order goes to
            order_head (str): short description of the order
            order_desc (str): optional detailed description of order

        Return:
            True if successful else return False
        """

        if cookid:
            self.cook_id = cookid
            
            if order_head:
                self.request['request_head'] = order_head
                self.request['request_desc'] = order_desc

            stats = self.save(True) # save to database

            if stats:
                return True
        
        return False # Return false if cookid is not set, or saving operation was not successful

        
