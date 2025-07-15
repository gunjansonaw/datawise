from models.dataset import Dataset
from utils.database import get_db
from datetime import datetime
from bson import ObjectId

class DatasetService:
    def create_dataset(self, data):
        dataset_data = data.copy()
        dataset_data['created_at'] = datetime.now()
        dataset_data['updated_at'] = datetime.now()
        dataset = Dataset(**dataset_data)
        db = get_db()
        result = db.datasets.insert_one(dataset.dict())
        return {"id": str(result.inserted_id)}

    def get_datasets(self, owner=None, tag=None):
        db = get_db()
        query = {"is_deleted": False}
        if owner:
            query["owner"] = owner
        if tag:
            query["tags"] = tag

        datasets = list(db.datasets.find(query))
        for dataset in datasets:
            dataset["_id"] = str(dataset["_id"])
        return datasets

    def get_dataset(self, dataset_id):
        db = get_db()
        dataset = db.datasets.find_one({"_id": ObjectId(dataset_id), "is_deleted": False})
        if dataset:
            dataset["_id"] = str(dataset["_id"])
        return dataset

    def update_dataset(self, dataset_id, data):
        db = get_db()
        data['updated_at'] = datetime.now()
        result = db.datasets.update_one(
            {"_id": ObjectId(dataset_id)},
            {"$set": data}
        )
        if result.modified_count:
            return self.get_dataset(dataset_id)
        return None

    def delete_dataset(self, dataset_id):
        db = get_db()
        result = db.datasets.update_one(
            {"_id": ObjectId(dataset_id)},
            {"$set": {"is_deleted": True}}
        )
        if result.modified_count:
            return {"message": "Dataset soft deleted successfully"}
        return None
