from dataclasses import dataclass


@dataclass
class ApplicationDTO:
    id: str


@dataclass
class RefreshTokenDTO:
    token: str
    access_token: str
    user_id: str
    revoked: bool
