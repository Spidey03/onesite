from market.exceptions.exceptions import (
    EmailInvalidPatternException,
    EmailAlreadyRegisteredException,
    MobileNumberAlreadyRegisteredException,
    UserNotExistsException,
)
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class UpdateUserDetailsInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def update_user_wrapper(
        self, user_details_dto: UserDetailsDTO, presenter: PresenterInterface
    ):
        try:
            self._update_user(user_details_dto=user_details_dto)
            return presenter.update_user_details_success_response()
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
        except UserNotExistsException:
            return presenter.user_not_present_response()

    def _update_user(self, user_details_dto: UserDetailsDTO):
        if not self.user_storage.check_user_exists(user_id=user_details_dto.id):
            raise UserNotExistsException()
        self.validate_email(
            email=user_details_dto.email, user_storage=self.user_storage
        )
        self.validate_mobile_number(
            mobile_number=user_details_dto.mobile_number, user_storage=self.user_storage
        )
        self.user_storage.update_user(user_details_dto=user_details_dto)
