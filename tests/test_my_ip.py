import pytest
from main import GetIP


class TestIP:

    def test_four_ip_octet(self):
        ip_addr = GetIP()
        octets = ip_addr.split(".")
        my_len = len(octets)
        assert my_len == 4

    def test_ip_range(self):
        ip_addr = GetIP()
        octets = ip_addr.split(".")
        for octet in octets:
            assert 0 <= int(octet) < 255
