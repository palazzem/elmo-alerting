from .exceptions import InvalidSession


def require_session(func):
    """Decorator applied to functions that require a valid Session.
    The session ID is verified in the instance for the attribute
    `_session_id`.

    Raises:
        InvalidSession: if a `session_id` is not available or expired.
    """

    def func_wrapper(*args, **kwargs):
        self = args[0]
        if self._session_id is None:
            raise InvalidSession("Session not available or expired")
        else:
            return func(*args, **kwargs)

    return func_wrapper
