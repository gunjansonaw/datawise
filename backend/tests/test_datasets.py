import pytest
from services.dataset_service import DatasetService
from models.dataset import Dataset
from datetime import datetime

@pytest.fixture
def dataset_service():
    return DatasetService()

def test_create_dataset(dataset_service, monkeypatch):
    def mock_insert_one(*args, **kwargs):
        return {"inserted_id": "507f1f77bcf86cd799439011"}

    monkeypatch.setattr('utils.database.get_db().datasets.insert_one', mock_insert_one)

    data = {
        "name": "Test Dataset",
        "owner": "Test Owner",
        "description": "Test Description",
        "tags": ["test", "dataset"]
    }

    result = dataset_service.create_dataset(data)
    assert result["id"] == "507f1f77bcf86cd799439011"

def test_get_datasets(dataset_service, monkeypatch):
    def mock_find(*args, **kwargs):
        return [
            {
                "_id": "507f1f77bcf86cd799439011",
                "name": "Test Dataset",
                "owner": "Test Owner",
                "description": "Test Description",
                "tags": ["test", "dataset"],
                "created_at": datetime.now(),
                "updated_at": datetime.now(),
                "is_deleted": False
            }
        ]

    monkeypatch.setattr('utils.database.get_db().datasets.find', mock_find)

    datasets = dataset_service.get_datasets()
    assert len(datasets) == 1
    assert datasets[0]["name"] == "Test Dataset"
