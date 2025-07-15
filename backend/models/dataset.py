from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class Dataset(BaseModel):
    id: Optional[str] = None
    name: str
    owner: str
    description: str
    tags: List[str]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    is_deleted: bool = False

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
