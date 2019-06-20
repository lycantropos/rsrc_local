import os
import shutil

import pytest
from hypothesis import (HealthCheck,
                        settings)

from tests.utils import temporary_directory_path_string

settings.register_profile('default',
                          max_examples=10,
                          deadline=None,
                          suppress_health_check=[HealthCheck.filter_too_much,
                                                 HealthCheck.too_slow])


@pytest.fixture(scope='session',
                autouse=True)
def bootstrap_and_cleanup() -> None:
    os.mkdir(temporary_directory_path_string)
    yield
    shutil.rmtree(temporary_directory_path_string,
                  ignore_errors=True)
