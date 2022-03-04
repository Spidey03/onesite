import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDetailsDTO:
    id: str
    first_name: str
    middle_name: Optional[str]
    last_name = Optional[str]
    joined_at = datetime.datetime
    mobile_number = str
    email = str
