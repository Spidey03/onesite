from market.exceptions.exceptions import UserNotFoundException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import SiteDTO
from market.interactors.storages.site_storages_interface import SiteStorageInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface


class AddSiteDetailsInteractor:
    def __init__(
            self,
            user_storage: UserStorageInterface,
            site_storage: SiteStorageInterface
    ):
        self.user_storage = user_storage
        self.site_storage = site_storage

    def add_site_details_wrapper(
            self, site_dto: SiteDTO, presenter: PresenterInterface
    ):
        try:
            self.add_site_details(site_dto=site_dto)
            return presenter.add_site_details_success_response()
        except UserNotFoundException:
            return presenter.get_user_not_found_response(user_id=site_dto.owner_id)

    def add_site_details(self, site_dto: SiteDTO):
        is_not_exists = not self.user_storage.check_user_exists(user_id=site_dto.owner_id)
        if is_not_exists:
            raise UserNotFoundException()
        self.site_storage.add_site_details(site_dto=site_dto)
