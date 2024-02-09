#!/usr/bin/python3

"""
App entry point. Mainly used for testing classes

"""

from models.base import BaseModel
from models.users import UserBase
from models.cooks import CooksModel
from models.storage_engine.db_storage import StorageDb

ins = StorageDb()

#obj = UserBase()
#obj1 = BaseModel()

#obj.setUser("Jill", "1234")
# print(obj)

#print(f"For obj -> {obj.save(db=True)}")
# print(f"For obj1 -> {obj1.save(db=True)}")

#results = obj.fetch("2bea24e7-3ebe-463a-8e3f-7aefe1631741")

#print(results)
# for result in results:
#     print(result)

# print(ins.show_cache())

cook = CooksModel()

# print(cook)

# print("--")

cook.setUser("Esi", "locked")

gift = {
    'cuisine': ["regional", "street"],
    'cooking_style': ["classic", "modern", "healthy"],
    'dish': ["main_courses", "sides_and_soups", "desserts"]
}

bio = "I am a very awsome cook!"

cook.setStatus(bio, **gift)

# print(cook)

cook.completed_orders = 20

cook.setRank()

head = "My first blog post!"

body = "Testing blog posting feature of app."

print(cook.createPost(head, body))

cook.save()

# print(cook.usrInfo())

for obj in ins.show_cache():
    print(obj)
