from pathlib import Path
from tests.fixtures import *
from app.config import CONFIG_PATH, load_config, MappingTable


def test_congif(config):
    assert isinstance(config.urbanAtlas.columns, dict)
    assert isinstance(config.setting.crs, int)




