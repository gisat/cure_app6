from pathlib import Path
from typing import Optional, Dict, List
from yaml import load
from yaml.loader import SafeLoader
from pydantic import BaseModel

CONFIG_PATH = Path(__file__).parent.parent / 'config.yaml'


class MappingTable(BaseModel):
    columns: Dict

    @property
    def original_names(self) -> List[str]:
        return [name for name in self.columns.values()]

    @property
    def process_names(self) -> List[str]:
        return [name for name in self.columns.keys()]


class Setting(BaseModel):
    crs: int


class Config(BaseModel):
    setting: Setting
    urbanAtlas: Optional[MappingTable]
    urbanAtlasChange: Optional[MappingTable]
    gdd: Optional[MappingTable]


def load_config(path: Path) -> Config:
    with open(path, 'r') as file:
        return Config(**load(file, SafeLoader))


