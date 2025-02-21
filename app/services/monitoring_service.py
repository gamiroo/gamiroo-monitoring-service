from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from typing import Optional, List
from app.models import monitoring as monitoring_models

async def get_metrics(
    db: AsyncSession,
    service_name: Optional[str] = None,
    metric_name: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None
) -> List[monitoring_models.MetricRecord]:
    query = select(monitoring_models.MetricRecord)
    if service_name:
        query = query.filter(monitoring_models.MetricRecord.service_name == service_name)
    if metric_name:
        query = query.filter(monitoring_models.MetricRecord.metric_name == metric_name)
    if start_date:
        query = query.filter(monitoring_models.MetricRecord.recorded_at >= start_date)
    if end_date:
        query = query.filter(monitoring_models.MetricRecord.recorded_at <= end_date)
    
    result = await db.execute(query)
    records = result.scalars().all()
    return records
