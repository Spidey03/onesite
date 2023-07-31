import abc
from typing import List

from market.interactors.storages.dtos import UserDetailsDTO, SiteDTO


class SiteStorageInterface(abc.ABC):
    @abc.abstractmethod
    def get_site_details(self, site_id: str) -> SiteDTO:
        pass

    @abc.abstractmethod
    def get_sites_bulk(self) -> List[SiteDTO]:
        pass

    @abc.abstractmethod
    def add_site_details(self, site_dto: SiteDTO):
        pass

    @abc.abstractmethod
    def is_user_owner(self, user_id: str, site_id: str) -> bool:
        pass

    @abc.abstractmethod
    def check_site_exists(self, site_id: str) -> bool:
        pass

    @abc.abstractmethod
    def update_site_visibility(self, site_id: str, is_private: bool = True):
        pass
