"""
Alien contact logging system using Pydantic validation.
Defines contact records and applies business validation rules.
"""

from enum import Enum
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


class ContactType(Enum):
    """
    Enumeration representing the possible types of alien contact.
    """
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class ModelValidator(BaseModel):
    """
    Model representing a validated alien contact record.

    Attributes:
        contact_id (str): Unique identifier for the contact (start with 'AC').
        timestamp (datetime): Date and time when the contact occurred.
        location (str): Geographic location of the contact.
        contact_type (ContactType): Type of contact event.
        signal_strength (float): Strength of the detected signal (0.0–10.0).
        duration_minutes (int): Duration of the contact in minutes.
        witness_count (int): Number of witnesses present.
        message_received (Optional[str]): Message captured during the contact.
        is_verified (bool): Indicates whether the contact has been verified.

    Validation Rules:
        - Contact ID must start with 'AC'.
        - Physical contact must be verified.
        - Telepathic contact requires at least 3 witnesses.
        - Signal strength above 7 requires a recorded message.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_model(self) -> 'ModelValidator':
        """
        Performs cross-field validation to enforce business rules.
        
        Returns:
            The validated model instance
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Hola")
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Error")
        if self.contact_type is ContactType.TELEPATHIC and \
                self.witness_count < 3:
            raise ValueError("Error")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Error")
        return self


def main() -> None:
    """
    Entry point of the program.

    Demonstrates the creation of valid and invalid alien contact
    records and shows how validation errors are handled.
    """
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        valid_contact = ModelValidator(
            contact_id="AC12345",
            timestamp=datetime.fromisoformat("2026-02-14T12:00:00"),
            location="Madrid",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=60,
            witness_count=5,
            message_received="Hello from outer space",
            is_verified=True
        )
        print("Valid contact created:")
        print(f"Contact ID: {valid_contact.contact_id}")
        print(f"Timestamp: {valid_contact.timestamp}")
        print(f"Location: {valid_contact.location}")
        print(f"Contact Type: {valid_contact.contact_type.value}")
        print(f"Signal Strength: {valid_contact.signal_strength}")
        print(f"Duration (minutes): {valid_contact.duration_minutes}")
        print(f"Witness Count: {valid_contact.witness_count}")
        print(f"Message Received: {valid_contact.message_received}")
        print(f"Is Verified: {valid_contact.is_verified}")
    except ValueError as e:
        print(f"Validation error: {e}")

    print("=" * 40)

    try:
        ModelValidator(
            contact_id="AC54321",
            timestamp=datetime.fromisoformat("2026-02-14T12:00:00"),
            location="Madrid",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=60,
            witness_count=2,
            message_received=None,
            is_verified=True
        )
    except ValueError as e:
        print("Expected validation error:")
        print({e})


if __name__ == "__main__":
    main()
