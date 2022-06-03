import enum


class StatusCode(enum.Enum):
    BadRequest = 400
    NotFound = 404
    Forbidden = 403
    Success = 200
    Created_Success = 201


class ActionStatusChoices(enum.Enum):
    TODO = 'TODO'
    PENDING = 'PENDING'
    DISCARDED = 'DISCARDED'
    DONE = 'DONE'
    FAILED = 'FAILED'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


SITE_TYPE = (('Home', 'home'), ('Site', 'site'))
site_types = [x[0] for x in SITE_TYPE]
