from typing import Any, Optional

import redis

from fastapiexp.domain.exceptions import StoreError

from ..environments import get_environments

_environments = get_environments()
client = redis.Redis(_environments.redis_url, port=_environments.redis_port, db=0)


class RedisStore:
    def store(self, key: str, value: Any, expire: int):
        if not client.set(key, value, ex=expire):
            raise StoreError(f"failed to store value in redis, key: {key}")

    def get_value(self, key: str) -> Optional[Any]:
        try:
            return client.get(key)
        except Exception:
            raise StoreError(f"failed to get value from redis, key: {key}")
