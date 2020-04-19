class validate(object):
    _should_validate = True

    def __init__(self, should_validate):
        self._old = validate._should_validate
        validate._should_validate = should_validate

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        validate._should_validate = self._old
