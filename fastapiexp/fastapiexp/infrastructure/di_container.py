from .session.redis_store import RedisStore


class DIContainer:
    def __init__(self):
        self.session_store = RedisStore()


di_container = DIContainer()
