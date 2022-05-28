from market.exceptions.exceptions import (
    EmailAlreadyRegisteredException,
    EmailInvalidPatternException,
    MobileNumberAlreadyRegisteredException,
    WeakPasswordException,
    UsernameAlreadyTakenException,
)
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO, AddUserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class AddUserDetailsInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_user_details_wrapper(
        self, user_details_dto: AddUserDetailsDTO, presenter: PresenterInterface
    ):
        try:
            user_dto = self._add_user_details(user_details_dto=user_details_dto)
            return presenter.add_user_details_success_response(user_dto=user_dto)
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
        except UsernameAlreadyTakenException:
            return presenter.username_already_taken_response(
                username=user_details_dto.username
            )
        except WeakPasswordException:
            return presenter.weak_password_exception_response()

    def _add_user_details(self, user_details_dto: AddUserDetailsDTO):
        self.validate_email(
            email=user_details_dto.email, user_storage=self.user_storage
        )
        self.validate_mobile_number(
            mobile_number=user_details_dto.mobile_number, user_storage=self.user_storage
        )
        if self.check_username_exists(
            user_storage=self.user_storage, username=user_details_dto.username
        ):
            raise UsernameAlreadyTakenException()
        self.validate_password_pattern(password=user_details_dto.password)
        user_id = self.user_storage.add_user(user_details_dto=user_details_dto)
        user_dto = self.user_storage.get_user(user_id=user_id)

        return user_dto
