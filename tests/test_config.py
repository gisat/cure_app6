from pathlib import Path
from tests.fixtures import *
from app.config import CONFIG_PATH, load_config, MappingTable, UserInput


def test_config(config):
    assert isinstance(config.urbanAtlas.columns, dict)
    assert isinstance(config.setting.crs, int)


def test_user_input_alias(urban_atlas_path, urban_atlas_layer_name):
    input = UserInput(**{'urbanAtlas': {'path': urban_atlas_path, 'layerName': urban_atlas_layer_name}})
    ouput = input.dict(by_alias=True)
    assert 'layer_name' in ouput.get('urbanAtlas')



