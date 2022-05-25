from common.storage_implementation.dtos import UserAuthTokensDTO
from market.exceptions.exceptions import (
    EmailAlreadyRegisteredException,
    EmailInvalidPatternException,
    MobileNumberAlreadyRegisteredException,
)
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class AddUserDetailsInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_user_details_wrapper(
        self, user_details_dto: UserDetailsDTO, presenter: PresenterInterface
    ):
        try:
            auth_token_dto = self._add_user_details(user_details_dto=user_details_dto)
            return presenter.add_user_details_success_response(
                auth_token_dto=auth_token_dto
            )
        except EmailInvalidPatternException:
            return presenter.email_pattern_invalid_response(
                email=user_details_dto.email
            )
        except EmailAlreadyRegisteredException:
            return presenter.email_already_register_response(
                email=user_details_dto.email
            )
        except MobileNumberAlreadyRegisteredException:
            return presenter.mobile_number_already_registered_response(
                mobile_number=user_details_dto.mobile_number
            )

    def _add_user_details(self, user_details_dto: UserDetailsDTO):
        self.validate_email(
            email=user_details_dto.email, user_storage=self.user_storage
        )
        self.validate_mobile_number(
            mobile_number=user_details_dto.mobile_number, user_storage=self.user_storage
        )
        user_id = self.user_storage.add_user(user_details_dto=user_details_dto)

        return self._get_auth_tokens(user_id=user_id)

    @staticmethod
    def _get_auth_tokens(user_id: str) -> UserAuthTokensDTO:
        from common.storage_implementation.oauth2_storage_implementation import (
            Oauth2StorageImplementation,
        )
        from common.services.oauth2_service import Oauth2Service

        oauth2storage = Oauth2StorageImplementation()
        oauth2service = Oauth2Service(oauth2storage=oauth2storage)
        return oauth2service.create_auth_tokens(user_id=user_id)
