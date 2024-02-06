"""
Within this module is defined all database storage logic

"""

from pymongo import MongoClient


class StorageDb:
    """
    Handles all storage logic

    """
    __memCache = [] #  memory for storing objects temporarily

    # connect to Atlas database

    connection_str = "mongodb+srv://kojo:kojomongo@cluster0.ohsb4cl.mongodb.net/?retryWrites=true&w=majority"

    try:
        client = MongoClient(connection_str)
        
        db = client.cook4medb # create/retrive database
    except Exception as err:
        print(f"An error occured whiles trying to connect: ERROR => {err}")

    def show_cache(self):
        """
        Return objects saved in memory

        """
        return StorageDb.__memCache

    def load(self, obj, todb=False):
        """
        Load object into memory. If `todb` is true,
        then save the object to database

        Args:
            obj (object): object to be saved into memory
            todb (bool): if true, save object to database instead of memory only
        
        Return:
            True if succesful, else return False
        """

        if obj:
            StorageDb.__memCache.append(obj)

            if todb is True:
                save_obj = StorageDb.__memCache[-1] #  Retrive object from memmory

                if save_obj:
                    obj_dict = save_obj.dictify() #  convert to dictionary representation

                    # create/retrive a database collection according to the class of the object
                    collection = obj_dict['__class__'] #  obtain class name

                    collection = StorageDb.db[f"{collection}"] #  create/retrive the collection
                    # print(collection)

                    try:
                        ok = collection.insert_one(obj_dict).inserted_id
                        print(ok)
                    except Exception as err:
                        print(f"There was an error trying to insert: ERROR => {err}")
                        
                        return False # if there was an error with insertion
                else:
                    return False # if no object is found in memory
            
            return True # if object exist but todb is False
        
        else:
            return False # if no object was found in memory



        
