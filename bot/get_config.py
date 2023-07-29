#from typing import Optional
from pydantic import BaseModel, validator, SecretStr, RedisDsn,DirectoryPath
from os import getenv

class Settings(BaseModel):
    tg_secret: SecretStr
    log_level: str
    app_logs:DirectoryPath
    #redis: Optional[RedisDsn]
    """
    @validator("fsm_mode")
    def fsm_type_check(cls, v):
        if v not in ("memory", "redis"):
            raise ValueError("Incorrect fsm_mode. Must be one of: memory, redis")
        return v

    @validator("redis")
    def skip_validating_redis(cls, v, values):
        if values["fsm_mode"] == "redis" and v is None:
            raise ValueError("Redis config is missing, though fsm_type is 'redis'")
        return v
    """


config = Settings(**{el:getenv(el) for el in ['tg_secret','log_level','app_logs']})