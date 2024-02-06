#!/usr/bin/python3

"""
App entry point. Mainly used for testing classes

"""

from models.base import BaseModel
from models.users import UserBase
from models.storage_engine.db_storage import StorageDb

ins = StorageDb()

obj = UserBase()
obj1 = BaseModel()

obj.setUser("Jill", "1234")
# print(obj)

print(f"For obj -> {obj.save(db=True)}")
# print(f"For obj1 -> {obj1.save(db=True)}")

results = obj.fetch("2bea24e7-3ebe-463a-8e3f-7aefe1631741")

print(results)
# for result in results:
#     print(result)

# print(ins.show_cache())