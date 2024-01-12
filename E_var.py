from pydantic_settings import BaseSettings ,SettingsConfigDict

class Settings(BaseSettings):
    bucket:str
    accesskey:str
    secretaccesskey:str
    expires:int
    server:str
    database:str
    model_config = SettingsConfigDict(env_file=".env")
