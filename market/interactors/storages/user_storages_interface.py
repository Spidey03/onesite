import abc
from typing import List, Union, Optional

from market.interactors.storages.dtos import (
    UserDetailsDTO,
    AddUserDetailsDTO,
    LoginUserDTO,
)


class UserStorageInterface(abc.ABC):
    @abc.abstractmethod
    def get_user(self, user_id: str) -> UserDetailsDTO:
        pass

    @abc.abstractmethod
    def get_users_bulk(self, user_ids: List[str]):
        pass

    @abc.abstractmethod
    def check_user_exists(self, user_id: str):
        pass

    @abc.abstractmethod
    def is_email_already_registered(self, email: str) -> bool:
        pass

    @abc.abstractmethod
    def add_user(self, user_details_dto: AddUserDetailsDTO):
        pass

    @abc.abstractmethod
    def add_users_bulk(self, user_details_dto_list: List[AddUserDetailsDTO]):
        pass

    @abc.abstractmethod
    def is_mobile_number_already_registered(self, mobile_number: str) -> bool:
        pass

    @abc.abstractmethod
    def update_user(self, user_details_dto):
        pass

    @abc.abstractmethod
    def delete_user(self, user_id):
        pass

    @abc.abstractmethod
    def check_username_already_exists(self, username: str) -> bool:
        pass

    @abc.abstractmethod
    def is_account_disabled(
        self, username: Optional[str] = '', user_id: Optional[str] = ''
    ) -> bool:
        pass

    @abc.abstractmethod
    def authenticate_user(self, user_dto: LoginUserDTO) -> (Union[str, None], bool):
        pass

    @abc.abstractmethod
    def validate_email_already_exist_bulk(self, email_list: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_mobile_number_already_exist_bulk(
        self, mobile_numbers: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_username_already_exist_bulk(self, usernames: List[str]) -> List[str]:
        pass
