from common.storage_implementation.dtos import ApplicationDTO


class Oauth2StorageImplementation:
    def get_or_create_default_application(self, user_id) -> (ApplicationDTO, bool):
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
                client_secret=settings.DEFAULT_OAUTH_CLIENT_SECRET,
                client_id=settings.DEFAULT_OAUTH_CLIENT_ID,
                client_type=AbstractApplication.CLIENT_CONFIDENTIAL,
                authorization_grant_type=AbstractApplication.GRANT_PASSWORD,
            )
            is_created = True
        application_dto = self._create_application_dto(application=application)
        return application_dto, is_created

    @staticmethod
    def _create_application_dto(application):
        return ApplicationDTO(id=application.id)
