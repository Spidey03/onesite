class UserNotFoundException(Exception):
    pass


class SiteNotFoundException(Exception):
    pass


class EmailAlreadyRegisteredException(Exception):
    pass


class EmailInvalidPatternException(Exception):
    pass


class WeakPasswordException(Exception):
    def __str__(self):
        return 'Weak password: A minimum 8 characters password contains a combination of uppercase and lowercase letter and number'

    pass


class MobileNumberAlreadyRegisteredException(Exception):
    pass


class UserNotExistsException(Exception):
    pass


class UsernameAlreadyTakenException(Exception):
    pass


class UsernameNotFoundException(Exception):
    pass


class LoginFailedException(Exception):
    pass


class UserIsNotOwnerOfSite(Exception):
    def __init__(self, site_id: str, user_id: str):
        self.site_id = site_id
        self.user_id = user_id
