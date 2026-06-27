from pydantic import BaseModel

class Dashboard(BaseModel):

    total_reports: int

    active_reports: int

    resolved_reports: int

    critical_reports: int

    community_health_score: float