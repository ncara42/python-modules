"""
Space mission management system using Pydantic models.
Defines crew members, missions, and validation rules.
"""


from enum import Enum
from typing import List
from datetime import datetime
from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    """
    Enumeration representing the hierarchical ranks
    assigned to space crew members.
    """
    CADET = "Cadet"
    OFFICER = "Officer"
    LIEUTENANT = "Lieutenant"
    CAPTAIN = "Captain"
    COMMANDER = "Commander"


class CrewMember(BaseModel):
    """
    Model representing an individual crew member
    participating in a space mission.

    Attributes:
        member_id (str): Unique identifier for the crew member.
        name (str): Full name of the crew member.
        rank (Rank): Rank assigned within the mission hierarchy.
        age (int): Age of the crew member (must be between 18 and 80).
        specialization (str): Area of expertise.
        years_experience (int): Number of years of professional experience.
        is_active (bool): Indicates whether the crew member is active.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """
    Model representing a space mission with its operational details
    and assigned crew members.

    Attributes:
        mission_id (str): Unique mission identifier (must start with 'M').
        mission_name (str): Official name of the mission.
        destination (str): Target destination of the mission.
        launch_date (datetime): Scheduled launch date.
        duration_days (int): Duration of the mission in days.
        crew (List[CrewMember]): List of assigned crew members.
        mission_status (str): Current status of the mission.
        budget_millions (float): Mission budget in millions of dollars.

    Validation Rules:
        - Mission ID must start with 'M'.
        - At least one crew member must be assigned.
        - At least one crew member must hold the rank of Commander.
        - All crew members must be active.
        - For missions longer than 365 days, at least half of the crew
          must have 5 or more years of experience.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field()
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_model(self) -> 'SpaceMission':
        """
        Performs cross-field validation to ensure mission integrity
        and compliance with business rules.
        
        Returns:
            The validated model instance
        """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not self.crew:
            raise ValueError("A mission must have at least one crew member")
        if not any(member.rank is Rank.COMMANDER for member in self.crew):
            raise ValueError("A mission must have at least one commander")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            xp = sum(1 for member in self.crew if member.years_experience >= 5)
            if xp < len(self.crew) / 2:
                raise ValueError("Error")
        return self


def main() -> None:
    """
    Entry point of the program.

    Demonstrates the creation of crew members and a space mission,
    including validation handling and output display.
    """
    print("Space Crew and Mission Models Initialized")
    print("=" * 40)

    crew_list = [
        CrewMember(member_id="SC001",
                   name="Sarah Connor",
                   rank=Rank.COMMANDER,
                   age=45,
                   specialization="Mission Command",
                   years_experience=20),

        CrewMember(member_id="JS002",
                   name="John Smith",
                   rank=Rank.LIEUTENANT,
                   age=35,
                   specialization="Navigation",
                   years_experience=10),

        CrewMember(member_id="AJ003",
                   name="Alice Johnson",
                   rank=Rank.OFFICER,
                   age=30,
                   specialization="Engineering",
                   years_experience=8)
    ]

    try:
        print("Valid mission created:")
        mission = SpaceMission(
            mission_id="M1234",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 5, 1),
            duration_days=720,
            crew=crew_list,
            mission_status="planned",
            budget_millions=500.0
        )
        print("Mission: Mars Colony Establishment")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("Crew members:")
    for member in crew_list:
        print(f"- {member.name} "
              f" ({member.rank.value}) - {member.specialization}")

    print("=" * 40)

    try:
        mission = SpaceMission(
            mission_id="M1234",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2025, 5, 1),
            duration_days=720,
            crew=crew_list,
            mission_status="planned",
            budget_millions=500.0
        )
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
