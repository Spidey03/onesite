from market.interactors.storages.user_storages_interface import UserStorageInterface


class ValidationMixin:
    @staticmethod
    def check_email_already_exists(email: str, user_storage: UserStorageInterface):
        from market.exceptions.exceptions import EmailAlreadyRegisteredException

        is_exists = user_storage.is_email_already_registered(email=email)
        if is_exists:
            raise EmailAlreadyRegisteredException()

    @staticmethod
    def check_email_pattern(email: str):
        import re
        from market.exceptions.exceptions import EmailInvalidPatternException

        regex = re.compile(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        )
        if not re.fullmatch(regex, email):
            raise EmailInvalidPatternException()

    def validate_email(self, email: str, user_storage: UserStorageInterface):
        self.check_email_pattern(email=email)
        self.check_email_already_exists(email=email, user_storage=user_storage)

    @staticmethod
    def validate_mobile_number(mobile_number, user_storage: UserStorageInterface):
        from market.exceptions.exceptions import MobileNumberAlreadyRegisteredException

        is_exists = user_storage.is_mobile_number_already_registered(
            mobile_number=mobile_number
        )
        if is_exists:
            raise MobileNumberAlreadyRegisteredException()

    @staticmethod
    def validate_password_pattern(password: str):
        import re
        from market.exceptions.exceptions import WeakPasswordException

        regex = re.compile(
            r'(?=^.{8,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
        )
        if not re.fullmatch(regex, password):
            raise WeakPasswordException()
