from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Report(BaseModel):

    id: str

    image_path: str

    latitude: float
    longitude: float

    issue_type: Optional[str] = None
    description: Optional[str] = None

    severity: Optional[str] = None
    impact_score: Optional[int] = None

    road_type: Optional[str] = None
    traffic_level: Optional[str] = None

    duplicate_probability: Optional[float] = None

    recommended_department: Optional[str] = None
    recommended_action: Optional[str] = None

    status: str = "Reported"

    created_at: datetime