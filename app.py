#!/usr/bin/python3

"""
App entry point. Mainly used for testing classes

"""

from models.base import BaseModel
from models.users import UserBase
from models.cooks import CooksModel
from models.clients import ClientModel
from models.posts import PostModel
from api.v1.app import app
from models.storage_engine.db_storage import StorageDb



if __name__ == '__main__':
    app.run(debug=True)

