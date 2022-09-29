from pathlib import Path
from numpy import concatenate
from geopandas import GeoDataFrame
from rasterio import open, DatasetReader
from app.errors import check_projections


def open_raster(path: Path) -> DatasetReader:
    return open(path)


def get_sample(geodata: GeoDataFrame, raster: DatasetReader, column_name: str = 'sample') -> GeoDataFrame:
    """Function returns for given Geodaframe containing """
    if check_projections(geodata, raster):
        new = geodata.copy(deep=True)
        coords = [(point.x, point.y) for index, point in geodata.geometry.iteritems()]
        new[column_name] = [x for x in raster.sample(coords)]
        new[column_name] = concatenate([x for x in raster.sample(coords)])
        return new