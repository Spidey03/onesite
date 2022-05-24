import enum


class StatusCode(enum.Enum):
    BadRequest = 400
    NotFound = 404
    Forbidden = 403
    Success = 200
    Created_Success = 201


SITE_TYPE = (('Home', 'home'), ('Site', 'site'))
site_types = [x[0] for x in SITE_TYPE]
