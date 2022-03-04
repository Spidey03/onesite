import abc

from market.interactors.storages.dtos import UserDetailsDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_user(self, user_id: str) -> UserDetailsDTO:
        pass
