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
        
        
    def reload(self, obj, search_id=None):
        """
        Retrive data from database. If search_id is specified,
        get that document, else return the whole collection
        of that object

        Args:
            obj (object): object whose class database collection to search
            search_id (str): id to retrive a specific document

        Return:
            the quried document
        """

        collection = StorageDb.db[f"{obj.__class__.__name__}"] # Retrive collection according to class name

        if search_id is not None:
            try:
                found_doc = collection.find_one({"id": search_id})
                return StorageDb.stripObjectId(found_doc)
            except Exception as err:
                print(f"There was an error retriving the document: ERROR => {err}")
        else:
            try:
                cursor = collection.find()
                found_coll = []

                for cur in cursor:
                    found_coll.append(StorageDb.stripObjectId(cur))
                return found_coll
            except Exception as err:
                print(f"There was an error retriving the documents: ERROR => {err}")


    def remove(self, obj):
        """
        Erase objects from memory and database

        Args:
            obj (object): object to erase

        Return:
            True is successful else return False
        """

        collection = StorageDb.db[f"{obj.__class__.__name__}"] # Retrive collection according to class name

        if obj:
            collection.delete_one({'id': obj.id})
            i = 0

            for i in range(len(StorageDb.__memCache)):
                if StorageDb.__memCache[i] is obj:
                    del StorageDb.__memCache[i]
                    break
                i += 1
            return True
        else:
            return False
        
    
    def modify(self, obj):
        """
        Update an object in database

        Args:
            obj (object): the modified object to be used as update

        Return:
            Returns a boolen acknowledgement from server
        """

        if obj:
            collection = StorageDb.db[f"{obj['__class__']}"] # Retrive collection according to class name

            ack = collection.replace_one({'id': obj['id']}, obj)

            return ack.acknowledged #  Returns the acknowledgement


    @staticmethod
    def stripObjectId(docs):
        """
        Strips off `_id` attributes from db quuery response

        Args:
            docs: dictionary to work on

        Return:
            dictionary without `_id` attribute
        """

        new_obj = {}

        if docs:
            for key in docs:               
                if key != '_id':
                    new_obj[key] = docs[key]
            
            return new_obj
            






        
