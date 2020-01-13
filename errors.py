"""Custom exceptions that might happen."""

class ResponseError(Exception):
    """Raised when the returned web object does not have the 200 status code."""
    pass

class TokenError(Exception):
    """Raised when the auth token needs refreshing."""
    pass
    