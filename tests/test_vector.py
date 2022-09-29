import pytest
from geopandas import GeoDataFrame
from app.vector import vector2gpd, drop_columns, rename_columns, prepare_vector_data, add_columns, merge_vectors
from tests.fixtures import *


def test_gpkg(urban_atlas_path, urban_atlas_layer_name):
    geodata = vector2gpd(urban_atlas_path)
    assert isinstance(vector2gpd(urban_atlas_path), GeoDataFrame)
    return geodata


def test_gpkg_with_name(urban_atlas_path, urban_atlas_layer_name):
    assert isinstance(vector2gpd(urban_atlas_path, layer_name=urban_atlas_layer_name), GeoDataFrame)


def test_keep_columns(config, urban_atlas):
    columns = config.urbanAtlas.original_names
    geodata = drop_columns(geodata=urban_atlas, columns=columns, how='keep')
    assert all([v in columns for v in geodata.columns])


def test_drop_columns(config, urban_atlas):
    columns = config.urbanAtlas.original_names
    geodata = drop_columns(geodata=urban_atlas, columns=columns, how='drop')
    assert all([v not in columns for v in geodata.columns])


def test_rename_columns(config, urban_atlas):
    geodata = rename_columns(geodata=urban_atlas, src_names=config.urbanAtlas.original_names,
                             trg_names=config.urbanAtlas.process_names)
    assert all([v in geodata.columns for v in config.urbanAtlas.process_names])


def test_add_columns(urban_atlas, config):
    # test add columns with nonw
    geodata = add_columns(urban_atlas, columns_name=config.urbanAtlas.process_names)
    assert all(name in geodata.columns for name in config.urbanAtlas.process_names)
    # test add column with defined value
    geodata = add_columns(urban_atlas, columns_name=config.urbanAtlas.process_names, value=[1, 1, 1, 1])
    assert geodata.loc[0, config.urbanAtlas.process_names[0]] == 1
    geodata = add_columns(urban_atlas, columns_name='new', value=urban_atlas['code_2018'].astype('int').round(-4))
    assert geodata.loc[0, 'new'] == 20000


def test_merge(gdd1, gdd2):
    geodata = merge_vectors(gdd1, gdd2)
    assert len(geodata) == len(gdd1) + len(gdd2)


def test_data_preparation(config, urban_atlas):
    pipe = prepare_vector_data(config.urbanAtlas)
    ua = pipe(urban_atlas)
    assert len(ua.columns) == len(config.urbanAtlas.process_names)
    assert all([v in ua.columns for v in config.urbanAtlas.process_names])