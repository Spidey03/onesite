import abc
from typing import List

from market.interactors.storages.dtos import UserDetailsDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_user(self, user_id: str) -> UserDetailsDTO:
        pass

    def get_users_bulk(self, user_ids: List[str]):
        pass
