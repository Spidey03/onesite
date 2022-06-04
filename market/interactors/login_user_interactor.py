from common.storage_implementation.dtos import UserAuthTokensDTO
from market.exceptions.exceptions import UsernameNotFoundException, LoginFailedException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import LoginUserDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class LoginUserInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def login_wrapper(self, user_dto: LoginUserDTO, presenter: PresenterInterface):
        try:
            auth_token_dto = self._login_user(user_dto=user_dto)
            return presenter.login_success_response(auth_token_dto=auth_token_dto)
        except UsernameNotFoundException:
            return presenter.username_not_found_response(username=user_dto.username)
        except LoginFailedException:
            return presenter.login_failed_response()

    def _login_user(self, user_dto: LoginUserDTO):
        self._validate_account_with_username(user_dto)
        user_id, authenticated = self.user_storage.authenticate_user(user_dto=user_dto)
        if not authenticated:
            raise LoginFailedException()

        return self._get_auth_tokens(user_id=user_id)

    def _validate_account_with_username(self, user_dto):
        username_not_exists = not self.check_username_exists(
            user_storage=self.user_storage, username=user_dto.username
        )
        account_disabled = self.is_account_disabled(
            user_storage=self.user_storage, username=user_dto.username
        )
        if username_not_exists or account_disabled:
            raise UsernameNotFoundException()

    @staticmethod
    def _get_auth_tokens(user_id: str) -> UserAuthTokensDTO:
        from common.storage_implementation.oauth2_storage_implementation import (
            Oauth2StorageImplementation,
        )
        from common.services.oauth2_service import Oauth2Service

        oauth2storage = Oauth2StorageImplementation()
        oauth2service = Oauth2Service(oauth2storage=oauth2storage)
        return oauth2service.create_auth_tokens(user_id=user_id)
