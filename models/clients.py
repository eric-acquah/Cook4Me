"""
This module defines a class unique to users who are not
cooks on the platform

"""

from models.users import UserBase
from importlib import import_module


class ClientModel(UserBase):
    """
    Defines a class for clients

    """


    def makeOrder(self, cookid, head, desc):
        """
        Creates a new order for the client

        Args:
            cookid (str): the cook to whom the order goes to
            head (str): short description of the order
            desc (str): detailed description of the order

        Return:
            True if successful else return False
        """

        order = import_module("models.orders", package="Cook4Me")
        order = order.OrderModel()

        clientId = self.getUser()
        order.client_id = clientId['UserId']

        stats = order.createOrder(cookid, head, desc)

        return stats
