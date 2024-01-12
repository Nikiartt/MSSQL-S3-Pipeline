from pydantic_settings import BaseSettings ,SettingsConfigDict

class Settings(BaseSettings):#Class takes data from .env and returns it accordingly to scheme
    bucket:str
    accesskey:str
    secretaccesskey:str
    expires:int
    server:str
    database:str
    model_config = SettingsConfigDict(env_file=".env")