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


@dataclass
class SiteDTO:
    id: str
    owner_id: str
    district: str
    state: str
    country: str
    type: str
    price: float
    availability: bool = True
    is_private: bool = False
    location_coordinates: Optional[str] = None
    street_name: Optional[str] = None
    village: Optional[str] = None
    city: Optional[str] = None
