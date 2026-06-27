from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import uuid4

class Report(BaseModel):
    id: str = str(uuid4())

    issue_type: str
    description: str

    severity: str
    impact_score: int

    latitude: float
    longitude: float

    status: str = "Reported"

    recommended_department: str
    recommended_action: str

    verification_count: int = 0

    created_at: datetime = datetime.now()