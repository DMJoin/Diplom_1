import pytest


class TestBun:

    def test_bun_name_and_price_return_correct(self, mock_bun_data):
        assert mock_bun_data.get_name() == "Ржаная"
        assert mock_bun_data.get_price() == 150
    