import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass
class UserDTO:
    id: str
    first_name: str
    username: str
    email: str


@dataclass
class UserDetailsDTO(UserDTO):
    date_joined: Optional[str] = ''
    last_name: Optional[str] = None
    mobile_number: Optional[str] = None


@dataclass
class AddUserDetailsDTO(UserDTO):
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = False
    date_joined: Optional[str] = ''
    last_name: Optional[str] = None
    mobile_number: Optional[str] = None


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
