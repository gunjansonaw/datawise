from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class QualityLog(BaseModel):
    id: Optional[str] = None
    dataset_id: str
    status: str
    details: str
    timestamp: datetime = datetime.now()

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
