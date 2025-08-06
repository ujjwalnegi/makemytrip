from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup")
class BaseTest:
    driver = None