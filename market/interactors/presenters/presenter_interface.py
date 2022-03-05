import abc
from typing import Optional

from market.interactors.storages.dtos import UserDetailsDTO, SiteDTO


class PresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_user_details(self, user_details_dto: UserDetailsDTO):
        pass

    @abc.abstractmethod
    def get_user_not_found_response(self, user_id: Optional[str] = None):
        pass

    def get_site_details_response(self, site_dto: SiteDTO, owner_dto: UserDetailsDTO):
        pass

    def get_site_not_found_exception_response(self, site_id):
        pass
