from pydantic import BaseModel

class SummaryRequest(BaseModel):
    text: str
    max_length: int = 130
    min_length: int = 30

class SummaryResponse(BaseModel):
    original_text: str
    formatted_original: str
    summary: str
    processing_time: float