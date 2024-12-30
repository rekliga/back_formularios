from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='my_prefix_', env_file='.env')

    database_url: str
    
    

settings = Settings()
