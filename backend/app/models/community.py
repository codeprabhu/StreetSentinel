from pydantic import BaseModel

class Community(BaseModel):

    name: str

    health_score: float

    road_score: float
    waste_score: float
    water_score: float
    lighting_score: float

    active_issues: int
    resolved_issues: int