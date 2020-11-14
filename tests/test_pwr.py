import pytest

import homer.pwr as pwr

def test_tick():
    foo = pwr.PWR(55)
    foo.tick()
    assert(foo.simulation_time == 1)
