from market.interactors.storages.user_storages_interface import UserStorageInterface


class GetUserDetails:
    def __init__(self, user_id: str, storage: UserStorageInterface):
        self.user_id = user_id
        self.storage = storage
