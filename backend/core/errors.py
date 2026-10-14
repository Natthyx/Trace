class AppError(Exception):
    """Base class for all domain exceptions.

    Carries the HTTP status code so FastAPI can translate it to a response
    via a single registered handler. Concrete exceptions should inherit one
    of the semantic subclasses below (``NotFoundError``, ``ForbiddenError``,
    ``BadRequestError``, ``ConflictError``) rather than ``AppError`` directly.
    """

    status_code: int = 500

    def __init__(self, message: str | None = None):
        super().__init__(message or self.__class__.__name__)


class NotFoundError(AppError):
    status_code = 404


class ForbiddenError(AppError):
    status_code = 403


class BadRequestError(AppError):
    status_code = 400


class ConflictError(AppError):
    status_code = 409
