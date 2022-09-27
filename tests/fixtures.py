from pytest import fixture
from app.config import load_config, CONFIG_PATH, Config
from app.vector import vector2gpd
from pathlib import Path


@fixture(autouse=True)
def urban_atlas_path() -> Path:
    return Path(r"C:\michal\gisat\projects\Cure\app\app06\EL004L1_IRAKLEIO_UA2018_v013"
                r"\Data\EL004L1_IRAKLEIO_UA2018_v013.gpkg")


@fixture(autouse=True)
def urban_atlas_layer_name() -> str:
    return 'EL004L1_IRAKLEIO_UA2018'


@fixture(autouse=True)
def urban_atlas(urban_atlas_path)-> Config:
    return vector2gpd(urban_atlas_path)


@fixture(autouse=True)
def config()-> Config:
    return load_config(CONFIG_PATH)

