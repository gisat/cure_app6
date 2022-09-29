from pathlib import Path

from app.vector import drop_columns, rename_columns, vector2gpd
from app.base import compose
from functools import partial
from app.config import MappingTable
from geopandas import GeoDataFrame

def urban_atlas_preparation(path: Path, maptable: MappingTable, layer_name: str = None) -> GeoDataFrame:
    geodata = vector2gpd(path, layer_name=layer_name)
    pipe = [partial(drop_columns, columns=maptable.original_names, how='keep'),
            partial(rename_columns, src_names=maptable.original_names, trg_names=maptable.process_names)]

    return compose(partial(drop_columns, columns=maptable.original_names, how='keep'),
                   partial(rename_columns, src_names=maptable.original_names, trg_names=maptable.process_names))