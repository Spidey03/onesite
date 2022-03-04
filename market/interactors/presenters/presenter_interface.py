import abc

from market.interactors.storages.dtos import UserDetailsDTO


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_user_details(self, user_details_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user_not_found_response(self, user_id: str):
        pass
