import pytest
import os
from pathlib import Path

@pytest.fixture(scope='session', autouse=True)
def data_dir() -> Path:
    '''
    Returns path to directory with data samples
    '''
    path = Path(os.path.abspath(__file__)).parent / 'data_samples'
    return path

@pytest.fixture(scope='session', autouse=True)
def map_data():
    values_north = [
        49, 50, 50, 49, 47, 46, 44, 43, 42, 41, 40, 39, 38, 38, 38, 37,
        36, 34, 31, 32, 33, 32, 31, 30, 32, 32, 32, 30, 31, 32, 34, 35,
        35, 35, 34, 34, 32, 33, 33, 33, 33, 32, 32, 31, 30, 30, 30, 30,
        31, 31, 30, 30, 33, 35, 34, 32, 31, 31, 34, 37, 38, 38, 38, 39,
        39, 39, 40, 42, 43, 44, 45, 44, 42
    ]
    values_equator = [ 
        217, 199, 156, 128, 99, 83, 84, 88, 88, 82, 85, 84, 78, 72, 63, 
        65, 70, 82, 94, 115, 127, 111, 114, 102, 88, 78, 70, 64, 55, 52, 
        58, 62, 65, 58, 47, 46, 52, 66, 96, 114, 117, 130, 149, 157, 171, 
        183, 192, 198, 204, 211, 223, 217, 219, 234, 259, 269, 288, 304, 
        313, 323, 340, 334, 317, 316, 298, 280, 269, 265, 264, 261, 252, 
        242, 220
    ]
    values_south = [
        128, 130, 132, 133, 126, 123, 120, 133, 144, 140, 143, 149, 153, 
        142, 140, 140, 137, 141, 127, 133, 147, 146, 142, 144, 139, 133, 
        126, 125, 126, 127, 127, 126, 128, 128, 126, 132, 134, 132, 124, 
        125, 135, 143, 143, 132, 127, 132, 145, 140, 134, 132, 129, 129, 
        128, 126, 121, 117, 115, 114, 112, 115, 122, 121, 126, 126, 124, 
        126, 128, 128, 127, 126, 128, 129, 129
    ]
    all_values = [values_north, values_equator, values_south]
    data = list()
    for lat, vals in zip([87.5, 0.0, -87.5], all_values):
        lon_range = list(range(-180, 181, 5))
        data.extend([(lat, lon, v) for lon, v in zip(lon_range, vals)])
    return data