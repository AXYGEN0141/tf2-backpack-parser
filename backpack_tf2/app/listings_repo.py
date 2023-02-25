from backpack_tf2.app.setup import db
from backpack_tf2.app.entities import ListingObject
import pymongo


class ListingsRepository:
    collection_hats = "unusualHats"

    def __init__(self):
        self.collection_hats: pymongo.collection.Collection = db[self.collection_hats]

    def get_by_filter(self, getfilter: dict) -> ListingObject | None:
        """
        Get info about ListingObject using MongoDB find filter.
        If ListingObject record exists -> return ListingObject instance.
        If ListingObject record doesn't exist -> return None.
        """
        data = self.collection_hats.find_one(getfilter)
        if data is not None:
            return ListingObject(**data)
        return None

    def create(self, instance: ListingObject) -> ListingObject:
        """
        Receive ListingObject instance without id.
        Add record to db.
        """
        instance_to_dict = instance.dict()
        self.collection_hats.insert_one(instance_to_dict)
        return instance
