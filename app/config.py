from pydantic import BaseModel
import yaml
from pathlib import Path


class ColumnsNames(BaseModel):
    id: str
    code: str
    area: str
    geometry: str

    @property
    def reverse(self):
        return {v: k for k, v in self.__dict__.items()}

    @property
    def keys(self):
        return self.__dict__.keys()


class UrbanAtlas(BaseModel):
    columnNames: ColumnsNames


class Input(BaseModel):
    urbanAtlas: UrbanAtlas


class AppConfig(BaseModel):
    input: Input


def load_config(path: str) -> BaseModel:
    with open(path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return AppConfig(**data)

config_path = Path.cwd() / 'config.yaml'
config = load_config(config_path)
pass
