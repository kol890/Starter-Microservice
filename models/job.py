from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date, datetime

from .person import UNIType

class JobBase(BaseModel):
    title: str = Field(
        ...,
        description="Title of the job.",
        json_schema_extra={"example": "Software Engineer"},
    )
    description: Optional[str] = Field(
        None,
        description="Optional description of the job.",
        json_schema_extra={"example": "Develop and maintain backend APIs."},
    )
    start_date: Optional[date] = Field(
        None,
        description="Job start date.",
        json_schema_extra={"example": "2025-09-15"},
    )
    end_date: Optional[date] = Field(
        None,
        description="Job end date, if applicable.",
        json_schema_extra={"example": "2026-09-15"},
    )
    owner_uni: UNIType = Field(
        ...,
        description="Columbia UNI of the person associated with this job.",
        json_schema_extra={"example": "abc1234"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Software Engineer",
                    "description": "Develop backend APIs.",
                    "start_date": "2025-09-15",
                    "end_date": "2026-09-15",
                    "owner_uni": "abc1234",
                }
            ]
        }
    }

class JobCreate(JobBase):
    """Payload for creating a job."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Data Analyst",
                    "description": "Analyze business data.",
                    "start_date": "2025-10-01",
                    "end_date": None,
                    "owner_uni": "xy123",
                }
            ]
        }
    }

class JobUpdate(BaseModel):
    """Partial update for a job; only provide fields to change."""
    title: Optional[str] = Field(None, json_schema_extra={"example": "Backend Engineer"})
    description: Optional[str] = Field(None, json_schema_extra={"example": "Maintain API services."})
    start_date: Optional[date] = Field(None, json_schema_extra={"example": "2025-09-15"})
    end_date: Optional[date] = Field(None, json_schema_extra={"example": "2026-09-15"})
    owner_uni: Optional[UNIType] = Field(None, json_schema_extra={"example": "abc1234"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"title": "Machine Learning Engineer"},
                {"description": "Work on predictive models."},
                {"end_date": "2026-12-31"},
            ]
        }
    }

class JobRead(JobBase):
    """Server representation of a job returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Job ID.",
        json_schema_extra={"example": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-09-10T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-09-10T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "title": "Software Engineer",
                    "description": "Develop backend APIs.",
                    "start_date": "2025-09-15",
                    "end_date": "2026-09-15",
                    "owner_uni": "abc1234",
                    "created_at": "2025-09-10T10:20:30Z",
                    "updated_at": "2025-09-10T12:00:00Z",
                }
            ]
        }
    }