from secrets import token_urlsafe

from ..infrastructure.di_container import DIContainer


class SessionApplication:
    def __init__(self, di_container: DIContainer):
        self.session_store = di_container.session_store

    def store_session(self, expire: int) -> str:
        session_id = token_urlsafe(32)
        self.session_store.store(session_id, "session_id", expire)
        return session_id
