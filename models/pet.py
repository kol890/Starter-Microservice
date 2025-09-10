from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import date, datetime

from .person import UNIType

class PetBase(BaseModel):
    name: str = Field(
        ...,
        description="Given name.",
        json_schema_extra={"example": "Scooby"},
    )
    species: str = Field(
        ...,
        description="Type of pet.",
        json_schema_extra={"example": "Dog"},
    )
    breed: Optional[str] = Field(
        None,
        description="Breed of pet type.",
        json_schema_extra={"example": "Dachshund"},
    )
    weight: str = Field(
        ...,
        description="Weight of pet in pounds.",
        json_schema_extra={"example": "10"},
    )
    owner_uni: UNIType = Field(
        ...,
        description="Columbia uni of the Person who owns this pet.",
        json_schema_extra={"example": "abc2456"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Scooby",
                    "species": "Dog",
                    "breed": "Dachshund",
                    "weight": "15",
                    "owner_uni": "abc2456",
                }
            ]
        }
    }


class PetCreate(PetBase):
    """Creation payload for a pet."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Rover",
                    "species": "Dog",
                    "breed": "Labrador Retriever",
                    "weight": "20",
                    "owner_uni": "xy123",
                }
            ]
        }
    }


class PetUpdate(BaseModel):
    """Partial update for a Pet; supply only fields to change."""
    name: Optional[str] = Field(None, json_schema_extra={"example": "Bella"})
    species: Optional[str] = Field(None, json_schema_extra={"example": "Dog"})
    breed: Optional[str] = Field(None, json_schema_extra={"example": "Dalmatian"})
    weight: Optional[str] = Field(None, json_schema_extra={"example": "30"})
    owner_uni: Optional[str] = Field(None, json_schema_extra={"example": "abc123"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "weight": "25",
                    "owner_uni": "xy123",
                }
            ]
        }
    }


class PetRead(PetBase):
    """Server representation of a Pet returned to clients."""
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Pet ID.",
        json_schema_extra={"example": "99999999-1111-1111-8999-999999999999"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "name": "Mochi",
                    "species": "Cat",
                    "breed": "Siamese",
                    "weight": "12",
                    "owner_uni": "abc1234",
                    "created_at": "2025-09-08T16:22:30Z",
                    "updated_at": "2025-09-08T16:25:00Z",
                }
            ]
        }
    }
