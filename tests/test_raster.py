from app.raster import get_sample
from app.vector import as_representative_points
from tests.fixtures import *


def test_sampling(wsf, urban_atlas):
    points = as_representative_points(urban_atlas)
    samples = get_sample(points, wsf, column_name='point')
    assert samples['point'].max() == 2015
