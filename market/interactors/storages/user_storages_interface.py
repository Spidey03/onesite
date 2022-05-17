import abc
from typing import List

from market.interactors.storages.dtos import UserDetailsDTO


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
    def add_user(self, user_details_dto: UserDetailsDTO):
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
