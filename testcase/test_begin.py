import pytest
from utils.UtilsDriver import UtilsDriver


@pytest.mark.run(order=1)
class TestBegin:
	def test_begin(self):
		UtilsDriver._quit_driver = False