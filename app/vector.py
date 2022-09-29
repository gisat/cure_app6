from pathlib import Path
from typing import Optional, List, Literal, Callable, Union, Any
from functools import partial
import geopandas
from geopandas import GeoDataFrame, GeoSeries
import pandas
from app.config import MappingTable
from app.base import compose
from shapely.geometry.base import BaseGeometry

# constants
SPATIAL_PREDICTATE = ['intersects', 'contains', 'within', 'touches', 'crosses', 'overlaps']


# functions
def vector2gpd(path: Path, layer_name: Optional[str] = None) -> GeoDataFrame:
    return geopandas.read_file(path, layer=layer_name)


def drop_columns(geodata: GeoDataFrame, columns: List[str], how: Literal['keep', 'drop']) -> GeoDataFrame:
    if how == 'keep':
        return geodata.drop(geodata.columns.difference(columns), 1)
    elif how == 'drop':
        return geodata.drop(columns, 1)


def rename_columns(geodata: GeoDataFrame, src_names: List[str], trg_names: List[str]) -> GeoDataFrame:
    return geodata.rename(columns={s: t for s, t in zip(src_names, trg_names)})


def as_representative_points(geodata: GeoDataFrame) -> GeoDataFrame:
    new = geodata.copy(deep=True)
    new.geometry = new.representative_point()
    return new


def spatial_join(left: GeoDataFrame, right: GeoDataFrame, how: Literal['left', 'right', 'inner'],
                 predictate: SPATIAL_PREDICTATE) -> GeoDataFrame:
    new = left.copy(deep=True)
    return new.sjoin(right, how=how, op=predictate)


# todo: reneme function
def add_columns(geodata: GeoDataFrame, columns_name: Union[str, List[str]],
                value: Optional[Union[Any,List[Any]]] = None) -> GeoDataFrame:
    new = geodata.copy()
    new[columns_name] = value
    return new


def merge_vectors(*args: GeoDataFrame, ignore_index=True) -> GeoDataFrame:
    return GeoDataFrame(pandas.concat(args, ignore_index=ignore_index))


def clip_vector(geodata: GeoDataFrame, mask: Union[GeoDataFrame, GeoSeries, BaseGeometry],
                keep_geom_type=False) -> GeoDataFrame:
    return geopandas.clip(geodata, mask=mask, keep_geom_type=keep_geom_type)


# pipes
def prepare_vector_data(maptable: MappingTable) -> Callable:
    return compose(partial(drop_columns, columns=maptable.original_names, how='keep'),
                   partial(rename_columns, src_names=maptable.original_names, trg_names=maptable.process_names))