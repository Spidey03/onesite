from market.interactors.presenters.presenter_interface import PresenterInterface
from market.interactors.storages.user_storages_interface import UserStorageInterface


class GetUserDetails:
    def __init__(self, user_id: str, storage: UserStorageInterface, presenter: PresenterInterface):
        self.user_id = user_id
        self.storage = storage
