from django.conf import settings

from common.storage_implementation.dtos import UserAuthTokensDTO
from common.storage_implementation.oauth2_storage_implementation import (
    Oauth2StorageImplementation,
)


class Oauth2Service:
    def __init__(self, oauth2storage: Oauth2StorageImplementation):
        self.oauth2storage = oauth2storage

    def create_auth_tokens(self, user_id: str) -> UserAuthTokensDTO:
        (
            application_dto,
            is_created,
        ) = self.oauth2storage.get_or_create_default_application(user_id=user_id)
        access_token_dto = self.oauth2storage.create_access_token(
            user_id=user_id,
            application_id=application_dto.id,
            scopes=settings.DEFAULT_OAUTH_SCOPES,
            expire_in_seconds=settings.DEFAULT_ACCESS_TOKEN_EXPIRY_TIME,
        )

        refresh_token_dto = self.oauth2storage.create_refresh_token(
            user_id=user_id,
            application_id=application_dto.id,
            access_token_id=access_token_dto.access_token_id,
        )

        return UserAuthTokensDTO(
            user_id=user_id,
            access_token=access_token_dto.token,
            refresh_token=refresh_token_dto.token,
            expires=access_token_dto.expires,
        )
