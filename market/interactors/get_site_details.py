from typing import Tuple

from market.exceptions.exceptions import SiteNotFoundException, UserNotFoundException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import SiteDTO, UserDetailsDTO
from market.interactors.storages.site_storages_interface import SiteStorageInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface


class GetSiteInteractor:
    def __init__(
        self, site_storage: SiteStorageInterface, user_storage: UserStorageInterface
    ):
        self.site_storage = site_storage
        self.user_storage = user_storage

    def get_site_details_wrapper(self, site_id: str, presenter: PresenterInterface):
        try:
            site_dto, owner_dto = self._get_site_details(site_id)
            return presenter.get_site_details_response(
                site_dto=site_dto, owner_dto=owner_dto
            )
        except SiteNotFoundException:
            return presenter.get_site_not_found_exception_response(site_id=site_id)
        except UserNotFoundException:
            return presenter.get_user_not_found_response()

    def _get_site_details(self, site_id: str) -> (SiteDTO, UserDetailsDTO):
        site_dto = self.site_storage.get_site_details(site_id=site_id)

        owner_id = site_dto.owner_id
        owner_dto = self.user_storage.get_user(user_id=owner_id)

        return site_dto, owner_dto
