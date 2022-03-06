from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.site_storages_interface import SiteStorageInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface


class GetSiteBulkInteractor:
    def __init__(
            self,
            site_storage: SiteStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.site_storage = site_storage
        self.user_storage = user_storage

    def get_site_bulk_wrapper(self, presenter: PresenterInterface):
        site_dto_list = self.site_storage.get_sites_bulk()
        owner_ids = list(set([site_dto.owner_id for site_dto in site_dto_list]))
        self.user_storage.get_users_bulk(user_ids=owner_ids)
