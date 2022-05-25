class UserNotFoundException(Exception):
    pass


class SiteNotFoundException(Exception):
    pass


class EmailAlreadyRegisteredException(Exception):
    pass


class EmailInvalidPatternException(Exception):
    pass


class WeakPasswordException(Exception):
    pass


class MobileNumberAlreadyRegisteredException(Exception):
    pass


class UserNotExistsException(Exception):
    pass


class UsernameAlreadyTakenException(Exception):
    pass
