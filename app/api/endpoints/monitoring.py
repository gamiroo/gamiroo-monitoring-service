from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from datetime import datetime

from app.api.dependencies import get_db
from app.schemas import monitoring as monitoring_schemas
from app.services import monitoring_service

router = APIRouter()

@router.get("/metrics", response_model=List[monitoring_schemas.MetricRecordResponse])
async def get_metrics(
    service_name: Optional[str] = Query(None),
    metric_name: Optional[str] = Query(None),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve system metrics records, optionally filtering by service, metric, or time range.
    """
    records = await monitoring_service.get_metrics(db, service_name, metric_name, start_date, end_date)
    return records
