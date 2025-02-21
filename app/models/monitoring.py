from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class MetricRecord(Base):
    __tablename__ = "metric_records"
    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String, nullable=False)
    metric_name = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
