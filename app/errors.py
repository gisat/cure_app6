class ProjectionError(Exception):
    """Raised when wrong projection is used"""

    def __init__(self, message):
        super().__init__(message)


def check_projections(geodata, raster) -> bool:
    if raster.crs.to_epsg() != geodata.crs.to_epsg():
        raise ProjectionError(f'Raster (crs: {raster.crs.to_epsg()}) and vector (crs: {geodata.crs.to_epsg()} '
                              f'projections are not same ')
    else:
        return True
