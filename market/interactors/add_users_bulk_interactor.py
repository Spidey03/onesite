from typing import List

from market.exceptions.exceptions import (
    EmailInvalidPatternException,
    WeakPasswordException,
)
from market.interactors.storages.dtos import AddUserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface
from market.interactors.validation_mixin import ValidationMixin


class AddUserDetailsBulkInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def add_user_details_bulk(self, user_details: List[AddUserDetailsDTO]):
        self._add_user_details_bulk(user_details_dto_list=user_details)

    def _add_user_details_bulk(self, user_details_dto_list: List[AddUserDetailsDTO]):
        valid_emails, valid_mobile_numbers, valid_usernames = self._get_valid_fields(
            user_details_dtos=user_details_dto_list
        )

        valid_user_dtos = []
        for user_details_dto in user_details_dto_list:
            if (
                user_details_dto.email in valid_emails
                and user_details_dto.mobile_number in valid_mobile_numbers
                and user_details_dto.username in valid_usernames
            ):
                valid_user_dtos.append(user_details_dto)
        self.user_storage.add_users_bulk(user_details_dto_list=valid_user_dtos)

    def _get_valid_fields(self, user_details_dtos: List[AddUserDetailsDTO]):
        emails = []
        mobile_numbers = []
        usernames = []
        for user_details_dto in user_details_dtos:
            try:
                self.check_email_pattern(email=user_details_dto.email)
                if user_details_dto.password:
                    self.validate_password_pattern(password=user_details_dto.password)
            except (EmailInvalidPatternException, WeakPasswordException) as e:
                print(f'Ignored {user_details_dto.username} for {e}')
                continue
            emails.append(user_details_dto.email)
            mobile_numbers.append(user_details_dto.mobile_number)
            usernames.append(user_details_dto.username)
        valid_emails = self.user_storage.validate_email_already_exist_bulk(
            email_list=emails
        )
        valid_mobile_numbers = (
            self.user_storage.validate_mobile_number_already_exist_bulk(
                mobile_numbers=mobile_numbers
            )
        )
        valid_usernames = self.user_storage.validate_username_already_exist_bulk(
            usernames=usernames
        )
        return valid_emails, valid_mobile_numbers, valid_usernames
