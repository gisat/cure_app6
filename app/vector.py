from pathlib import Path
from typing import Optional, List, Literal, Callable
from functools import partial
import geopandas
from geopandas import GeoDataFrame

from app.config import MappingTable
from app.base import compose


def vector2gpd(path: Path, layer_name: Optional[str] = None) -> GeoDataFrame:
    return geopandas.read_file(path, layer=layer_name)


def drop_columns(geodata: GeoDataFrame, columns: List[str], how: Literal['keep', 'drop']) -> GeoDataFrame:
    if how == 'keep':
        return geodata.drop(geodata.columns.difference(columns), 1)
    elif how == 'drop':
        return geodata.drop(columns, 1)


def rename_columns(geodata: GeoDataFrame, src_names: List[str], trg_names: List[str]) -> GeoDataFrame:
    return geodata.rename(columns={s: t for s, t in zip(src_names, trg_names)})


def prepare_vector_data(maptable: MappingTable) -> Callable:
    return compose(partial(drop_columns, columns=maptable.original_names, how='keep'),
                   partial(rename_columns, src_names=maptable.original_names, trg_names=maptable.process_names))