from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel,Field


class CreateChat(BaseModel):
    companyName: str 
    sessionID: str
    message: str
    timestamp: datetime
    by: str = Field(default="user",description="Specify the conversation turn either user or gpt")

    class Config:
        schema_extra = {
                "companyName": "probe",
                "sessionId": "12344",
                "message": "Hi,there",
                "timestamp":"20-05-2023",
                "by":"gpt"
            }


