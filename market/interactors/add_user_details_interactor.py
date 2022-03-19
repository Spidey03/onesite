from market.exceptions.exceptions import EmailAlreadyRegisteredException, EmailInvalidPatternException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class AddUserDetailsInteractor(ValidationMixin):

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_user_details_wrapper(
            self,
            user_details_dto: UserDetailsDTO,
            presenter: PresenterInterface
    ):
        try:
            self._add_user_details(user_details_dto=user_details_dto)
        except EmailInvalidPatternException:
            return presenter.email_pattern_invalid_response(email=user_details_dto.email)
        except EmailAlreadyRegisteredException:
            return presenter.email_already_register_response(email=user_details_dto.email)

    def _add_user_details(self, user_details_dto: UserDetailsDTO):
        self.check_email_already_exists(
            email=user_details_dto.email,
            user_storage=self.user_storage
        )


        # validate phone number

        pass
