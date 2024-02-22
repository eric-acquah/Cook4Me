"""
This is the module for all user reviews

"""


from models.base import BaseModel


class ReviewModel(BaseModel):
    """
    Defines all attributes and Logic for all user reviews

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes all attributes unique to reviews
        """
        super().__init__(*args, **kwargs)

        if not kwargs:
            self.name = ""
            self.email = ""
            self.review = ""