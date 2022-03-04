from market.interactors.storages.dtos import UserDetailsDTO
from market.interactors.storages.user_storages_interface import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):

    def get_user(self, user_id: str) -> UserDetailsDTO:
        from market.models import User
        from market.exceptions.exceptions import UserNotFoundException

        if not User.objects.filter(id=user_id).exists():
            raise UserNotFoundException()
