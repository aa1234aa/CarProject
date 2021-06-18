import pytest

from utils.UtilsDriver import UtilsDriver


@pytest.mark.run(order=100)
class TestEnd:
    def test_end(self):
        UtilsDriver._quit_driver = True
        UtilsDriver.quit_driver()