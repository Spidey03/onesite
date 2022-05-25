import datetime

from common.storage_implementation.dtos import (
    ApplicationDTO,
    RefreshTokenDTO,
    AccessTokenDTO,
)


class Oauth2StorageImplementation:
    def get_or_create_default_application(self, user_id: str) -> (ApplicationDTO, bool):
        from django.conf import settings
        from oauth2_provider.models import Application
        from oauth2_provider.models import AbstractApplication

        is_application_created = False
        application_name = settings.DEFAULT_OAUTH_APPLICATION_NAME
        try:
            application = Application.objects.get(name=application_name)
        except Application.DoesNotExist:
            application = Application.objects.create(
                user_id=user_id,
                name=application_name,
                client_secret=settings.DEFAULT_OAUTH_SECRET_KEY,
                client_id=settings.DEFAULT_OAUTH_CLIENT_ID,
                client_type=AbstractApplication.CLIENT_CONFIDENTIAL,
                authorization_grant_type=AbstractApplication.GRANT_PASSWORD,
            )
            is_application_created = True
        application_dto = self._create_application_dto(application=application)
        return application_dto, is_application_created

    @staticmethod
    def _create_application_dto(application):
        return ApplicationDTO(id=application.id)

    def create_refresh_token(
        self, user_id: str, application_id: str, access_token_id: str
    ) -> RefreshTokenDTO:
        from oauth2_provider.models import RefreshToken

        refresh_token = self._generate_token()
        refresh_token_obj = RefreshToken.objects.create(
            user_id=user_id,
            token=refresh_token,
            access_token_id=access_token_id,
            application_id=application_id,
        )

        return RefreshTokenDTO(
            token=refresh_token_obj.token,
            access_token=refresh_token_obj.access_token,
            user_id=refresh_token_obj.user_id,
            revoked=refresh_token_obj.revoked,
        )

    def create_access_token(
        self, user_id: str, application_id: str, scopes: str, expire_in_seconds: int
    ) -> AccessTokenDTO:
        from oauth2_provider.models import AccessToken

        access_token = self._generate_token()
        expires = datetime.datetime.now() + datetime.timedelta(
            seconds=expire_in_seconds
        )
        access_token_obj = AccessToken.objects.create(
            user_id=user_id,
            token=access_token,
            application_id=application_id,
            expires=expires,
            scope=scopes,
        )

        return AccessTokenDTO(
            access_token_id=access_token_obj.id,
            token=access_token_obj.token,
            expires=access_token_obj.expires,
        )

    @staticmethod
    def _generate_token():
        import string
        import random

        size = 30
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(size))
