"""
This module defines logic specific to users
who are cooks on the platform

"""

from models.users import UserBase
from importlib import import_module


class CooksModel(UserBase):
    """
    Defines attributes and methods unique to cooks

    """

    categories = {
            'cuisine': ["global", "regional", "dietary"],
            'dish': ["appetizers_and_snacks", "main_courses", "sides_and_soups", "desserts", "baking"],
            'cooking_style': ["classic", "modern", "healthy", "street_food"]
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize cooks class instances

        """
        super().__init__(*args, **kwargs) #  inherit init variables of UserBase

        if not kwargs:
            self.specialty = {}
            self.rank = 0
            self.available = True
            self.completed_orders = 0
            self.bio = ""

    
    def setStatus(self, bio="", **domain):
        """
        Setter to set cooks specialty and bio

        Args:
            bio (str): A short description of the cook
            
            domain (dict): Dictionary of cooks specialty by cuisine,
            by dish type and by cooking styles
        """

        tmp_dict = {}

        if domain: # if domain is not empty
            for option in domain: # for each key in the domain dictionary eg. 'cuisine', 'dish', 'cooking_style'
                if option in CooksModel.categories.keys(): # if that key can be found in `categories`
                    tmp_list = [] # create a new list to hold valid subcategories for a specific category--
                    for value in domain[option]:   # --> eg. 'cuisine': "global", "regional" etc
                        if value in CooksModel.categories[option]: # validates the subcategory
                            tmp_list.append(value)
                    tmp_dict[option] = tmp_list # creates a dictionary of valid category and subcategories

            self.specialty = tmp_dict # the sanitized dictionary is passed as value for the cook's specialty

        if bio != "":
            self.bio = bio

    
    def setRank(self):
        """
        Sets the rank of the cook according to `completed_orders`

        """

        if self.completed_orders >= 1 and self.completed_orders < 4:
            self.rank = 1
        elif self.completed_orders >= 4 and self.completed_orders < 7:
            self.rank = 2
        elif self.completed_orders >= 7 and self.completed_orders < 10:
            self.rank = 3
        elif self.completed_orders >= 10 and self.completed_orders < 16:
            self.rank = 4
        elif self.completed_orders >= 15:
            self.rank = 5


    def createPost(self, head, text, media_path=""):
        """
        Creates and saves a blog post

        Args:
            head (str): title of post
            text (str): text content of post
            media_path (str): path to media file

        Return:
            True if successful else return False
        """

        from models.posts import PostModel

        post = PostModel()

        usr = self.getUser()

        author = {
            'name': usr['UserName'],
            'id': usr['UserId']
        }

        content = {
            'text': text,
            'media': media_path
        }

        stats = post.makePost(author, head, content)

        if stats:
            result = post.save()

        return result