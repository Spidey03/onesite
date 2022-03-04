from market.exceptions.exceptions import UserNotFoundException
from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.dtos import UserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface


class GetUserDetailsInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def get_user_details_wrapper(
            self, user_id: str,
            presenter: PresenterInterface
    ):
        try:
            user_details_dto = self._get_user_details(user_id=user_id)
            return presenter.get_user_details(user_details_dto=user_details_dto)
        except UserNotFoundException:
            return presenter.get_user_not_found_response(user_id=user_id)

    def _get_user_details(self, user_id) -> UserDetailsDTO:
        user_details_dto = self.storage.get_user(user_id=user_id)
        return user_details_dto
