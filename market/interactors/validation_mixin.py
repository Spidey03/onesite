from market.interactors.storages.user_storages_interface import UserStorageInterface


class ValidationMixin:

    @staticmethod
    def check_email_already_exists(email: str, user_storage: UserStorageInterface):
        from market.exceptions.exceptions import EmailAlreadyRegisteredException
        is_exists = user_storage.is_email_already_registered(email=email)
        if is_exists:
            raise EmailAlreadyRegisteredException()

    def check_email_pattern(self, email: str):
        pass