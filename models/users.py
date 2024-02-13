"""
This module defines the base class for all app
users

"""

from models.base import BaseModel
from shortuuid import uuid

class UserBase(BaseModel):
    """
    Base class for all users

    """

    __user_credentials = {}

    def __init__(self, *args, **kwargs):
        """
        Defines all fundamental user data

        Args:
            args (tuple): used for adding updates to user attributes
            kwargs (dict): key-value pair for recreating and existing object

        """
        super().__init__(*args, **kwargs) #  Inherits BaseModel init variables

        if not kwargs:  # This prevents it from overiding the recreation of objects
            self.__user_credentials = {
                'UserId': uuid(),
                'UserName': None,
                'UserPasswd': None
            }

            self.user_contact = {
                'phone': None,
                'whatsappNum': None,
                'email': None
            }

            self.user_location = None
            self.user_gender = None
            self.user_age = None

    def setUser(self, name, passwd):
        """
        Set user credentials

        Args:
            name (str): name of user
            passwd (str): user password
        """

        self.__user_credentials['UserName'] = name
        self.__user_credentials['UserPasswd'] = passwd


    def getUser(self):
        """
        Retrives user credentials

        Return:
            dictionary of username, userpasswd and userid
        """

        return self.__user_credentials
    
    
    def usrInfo(self):
        """
        Get every info about a user

        """

        return self.dictify()

    
## Test ##

# obj = UserBase()

# obj.setUser("Kojo", "1234")

# print(f"Getter -> {obj.getUser()}")

# print(obj)
# print("\n\n")

# can = obj.dictify()

# new_obj = UserBase(**can)

# print(new_obj)