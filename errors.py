class InvalidPlayer(Exception):
    """Raised when the user cannot be found in the API"""
    pass

class InvalidServer(Exception):
    """Raised when the server cannot be reached"""
    pass

class APIError(Exception):
    """Raised when an error occurs in the API"""
    pass
