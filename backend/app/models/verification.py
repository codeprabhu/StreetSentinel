from pydantic import BaseModel

class Verification(BaseModel):

    report_id: str

    user_vote: bool

    confidence: float