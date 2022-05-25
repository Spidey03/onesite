import datetime
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


@dataclass
class AccessTokenDTO:
    token: str
    access_token_id: str
    expires: int


@dataclass
class UserAuthTokensDTO:
    user_id: str
    access_token: str
    refresh_token: str
    expires: datetime
