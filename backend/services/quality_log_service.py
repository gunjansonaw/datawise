from models.quality_log import QualityLog
from utils.database import get_db
from datetime import datetime
from bson import ObjectId

class QualityLogService:
    def add_quality_log(self, dataset_id, data):
        log_data = data.copy()
        log_data['dataset_id'] = dataset_id
        log_data['timestamp'] = datetime.now()
        quality_log = QualityLog(**log_data)
        db = get_db()
        result = db.quality_logs.insert_one(quality_log.dict())
        return {"id": str(result.inserted_id)}

    def get_quality_logs(self, dataset_id):
        db = get_db()
        quality_logs = list(db.quality_logs.find({"dataset_id": dataset_id}))
        for log in quality_logs:
            log["_id"] = str(log["_id"])
        return quality_logs
