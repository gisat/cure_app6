from pathlib import Path
from typing import Optional, Dict, List
from yaml import load
from yaml.loader import SafeLoader
from pydantic import BaseModel, Field

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


class Vector(BaseModel):
    path: Path
    layerName: Optional[str] = Field(alias='layer_name')


class Raster(BaseModel):
    path: Path
    band: int = Field(default=0)


class UserInput(BaseModel):
    urbanAtlas: Optional[Vector]
    urbanAtlasChange: Optional[Vector]
    gdd: Optional[List[Vector]]
    wsf: Optional[Raster]
    hand: Optional[Raster]

