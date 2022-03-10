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
