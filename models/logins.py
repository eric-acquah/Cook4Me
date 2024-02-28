"""
Defines classes for user login

"""

from models.base import BaseModel


class LoginModel(BaseModel):
    """
    Calss for logins

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes custom login values
        """
        super().__init__(*args, **kwargs)

        self.usrIdentity = {
            'usrName': "",
            'usrPasswd': "",
            'usrObjId': "",
            'usrClass': "",
        }