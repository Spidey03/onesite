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
