from pathlib import Path

from app.vector import drop_columns, rename_columns, vector2gpd
from app.config import MappingTable, UserInput, Config
from geopandas import GeoDataFrame


def vector_preparation(path: Path, maptable: MappingTable, epsg: int, layer_name: str = None) -> GeoDataFrame:
    """Basic vector preparation common to all vectors data within the projects"""
    geodata = vector2gpd(path, layer_name=layer_name)
    geodata = drop_columns(geodata, columns=maptable.original_names, how='keep')
    geodata = rename_columns(geodata, src_names=maptable.original_names, trg_names=maptable.process_names)
    if geodata.crs.to_epsg() != epsg:
        geodata = geodata.to_crs(epsg=epsg)
    return geodata


def process(userinput: UserInput, config: Config):
    urban_atlas = vector_preparation(**userinput.urbanAtlas.dict(by_alias=True),
                                     maptable=config.urbanAtlas,
                                     epsg=config.setting.crs)

    urban_atlas_change = vector_preparation(**userinput.urbanAtlasChange.dict(by_alias=True),
                                            maptable=config.urbanAtlasChange,
                                            epsg=config.setting.crs)
