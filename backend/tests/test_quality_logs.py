import pytest
from services.quality_log_service import QualityLogService
from models.quality_log import QualityLog
from datetime import datetime

@pytest.fixture
def quality_log_service():
    return QualityLogService()

def test_add_quality_log(quality_log_service, monkeypatch):
    def mock_insert_one(*args, **kwargs):
        return {"inserted_id": "507f1f77bcf86cd799439011"}

    monkeypatch.setattr('utils.database.get_db().quality_logs.insert_one', mock_insert_one)

    data = {
        "status": "PASS",
        "details": "Test Quality Log"
    }

    result = quality_log_service.add_quality_log("507f1f77bcf86cd799439011", data)
    assert result["id"] == "507f1f77bcf86cd799439011"

def test_get_quality_logs(quality_log_service, monkeypatch):
    def mock_find(*args, **kwargs):
        return [
            {
                "_id": "507f1f77bcf86cd799439011",
                "dataset_id": "507f1f77bcf86cd799439011",
                "status": "PASS",
                "details": "Test Quality Log",
                "timestamp": datetime.now()
            }
        ]

    monkeypatch.setattr('utils.database.get_db().quality_logs.find', mock_find)

    quality_logs = quality_log_service.get_quality_logs("507f1f77bcf86cd799439011")
    assert len(quality_logs) == 1
    assert quality_logs[0]["status"] == "PASS"
