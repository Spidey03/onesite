import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDetailsDTO:
    id: str
    first_name: str
    joined_at: str
    mobile_number: str
    email: str
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
