from pydantic import BaseModel
from datetime import datetime

class MetricRecordBase(BaseModel):
    service_name: str
    metric_name: str
    value: float

class MetricRecordCreate(MetricRecordBase):
    pass

class MetricRecordResponse(MetricRecordBase):
    id: int
    recorded_at: datetime

    class Config:
        orm_mode = True
