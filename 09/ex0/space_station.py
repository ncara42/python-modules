"""Module for validating space station data using Pydantic models."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    """
    Represents a space station with validated attributes.

    Attributes:
        station_id (str): Unique identifier for the station (3-10 characters).
        name (str): Name of the station (1-50 characters).
        crew_size (int): Number of crew members (1-20).
        power_level (float): Power level as a percentage (0.0-100.0).
        oxygen_level (float): Oxygen level as a percentage (0.0-100.0).
        last_maintenance (datetime): Date and time of the last maintenance.
        is_operational (bool): Operational status
        of the station (default: True).
        notes (Optional[str]): Additional notes
        about the station (max 200 characters).
    """
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    """
    Demonstrates the validation of space station data.

    This function:
        - Creates a valid space station and prints its details.
        - Attempts to create an invalid space station
        and prints the validation error.
    """
    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-02-01T12:00:00"),
            notes="Station in low Earth orbit."
        )
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print("Status: Operational")
    except Exception as e:
        print(f"Error creating valid station: {e}")

    print("=" * 40)

    try:
        SpaceStation(
            station_id="ISS002",
            name="Space Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime.fromisoformat("2026-02-01T12:00:00"),
            notes=None
        )
    except Exception as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
