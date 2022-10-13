from pytest import fixture
from app.config import load_config, CONFIG_PATH, Config
from app.vector import vector2gpd
from app.raster import open_raster
from pathlib import Path
from geopandas import GeoDataFrame


@fixture(autouse=True)
def urban_atlas_gpkg_path() -> Path:
    return Path(r"C:\michal\gisat\projects\Cure\app\app06\EL004L1_IRAKLEIO_UA2018_v013"
                r"\Data\EL004L1_IRAKLEIO_UA2018_v013.gpkg")


@fixture(autouse=True)
def urban_atlas_layer_name() -> str:
    return 'EL004L1_IRAKLEIO_UA2018'


@fixture(autouse=True)
def urban_atlas_gpkg(urban_atlas_gpkg_path) -> GeoDataFrame:
    return vector2gpd(urban_atlas_gpkg_path)


@fixture(autouse=True)
def urban_atlas_path() -> str:
    return r'C:\michal\gisat\projects\Cure\app\app06\test_data\urban_atlas.geojson'


@fixture(autouse=True)
def urban_atlas(urban_atlas_path) -> GeoDataFrame:
    return vector2gpd(Path(urban_atlas_path))


@fixture(autouse=True)
def config()-> Config:
    return load_config(CONFIG_PATH)


@fixture(autouse=True)
def gdd1_path() -> str:
    return r'C:\michal\gisat\projects\Cure\app\app06\test_data\gpd1.geojson'


@fixture(autouse=True)
def gdd1(gdd1_path) -> GeoDataFrame:
    return vector2gpd(Path(gdd1_path))


@fixture(autouse=True)
def gdd2_path() -> str:
    return r'C:\michal\gisat\projects\Cure\app\app06\test_data\gpd2.geojson'


@fixture(autouse=True)
def gdd2(gdd2_path) -> GeoDataFrame:
    return vector2gpd(Path(gdd2_path))


@fixture(autouse=True)
def wsf_path() -> str:
    return r"C:\michal\gisat\projects\Cure\app\app06\CURE_Heraklion_v06_data\Heraklion_WSF_evolution_3035.tif"


@fixture(autouse=True)
def wsf(wsf_path):
    return open_raster(Path(wsf_path))
