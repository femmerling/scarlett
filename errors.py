class ScarlettError(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)

        self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload


class BadRequestError(Exception):

    def __init__(self, message):
        ScarlettError.__init__(message=message, status_code=400)

        self.status_code = 400
        self.message = message
