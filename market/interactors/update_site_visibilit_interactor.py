from market.exceptions.exceptions import UserNotFoundException, SiteNotFoundException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import SiteDTO
from market.interactors.storages.site_storages_interface import SiteStorageInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface


class UpdateSiteVisibilityInteractor:
    def __init__(
        self, user_storage: UserStorageInterface, site_storage: SiteStorageInterface
    ):
        self.user_storage = user_storage
        self.site_storage = site_storage

    def update_site_visibility_wrapper(
        self, site_id: str, user_id: str, presenter: PresenterInterface
    ):
        try:
            self._update_site_visibility(site_id=site_id, owner_id=user_id)
            return presenter.add_site_details_success_response()
        except SiteNotFoundException:
            return presenter.get_site_not_found_exception_response(site_id=site_id)
        except UserNotFoundException:
            return presenter.user_not_present_response()

    def _update_site_visibility(self, site_id: str, owner_id: str):
        if not self.site_storage.check_site_exists(site_id=site_id):
            raise SiteNotFoundException()
        is_not_exists = not self.user_storage.check_user_exists(user_id=owner_id)
        if is_not_exists:
            raise UserNotFoundException()
        self.site_storage.is_user_owner(user_id=owner_id, site_id=site_id)
