"""
 Defines class for posts that will be accessible for all
 cooks

"""

from models.base import BaseModel


class PostModel(BaseModel):
    """
    Defines methods for cooks to make blog posts

    """

    def __init__(self, *args, **kwargs):
        """
        Initialize base attributes for all post instances

        """

        super().__init__(*args, **kwargs)

        if not kwargs:
        
            self.author = {
                'name': None,
                'id': None
            }
            self.content = {
                'text': "",
                'media': "file_path"
            }

            self.post_title = ""

    
    def makePost(self, author, title, post_content):
        """
        Creates a post

        Args:
            author (dict): name and id of the author of the post
            title (str): title of post
            post_content (dict): contents of the post

        Return:
            True if successful else return false
        """

        if author and post_content:
            self.author['name'] = author.get('name')
            self.author['id'] = author.get('id')

            self.content['text'] = post_content.get('text')
            self.content['media'] = post_content.get('media')

            if title:
                self.post_title = title

            return True
        else:
            return False