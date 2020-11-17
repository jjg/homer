import pytest

import homer.pwr as pwr

reactor = pwr.PWR(55)

def test_tick():
    reactor.tick()
    assert(reactor.simulation_time == 1)

def test_rod_position():
    reactor.set_rod_position(25)
    reactor.tick()
    assert(reactor.rod_position == 1)

def test_primary_pump():
    reactor.set_primary_pump_rpm(20)
    reactor.tick()
    assert(reactor.primary_pump_rpm == 20)

def test_primary_relief_valve():
    reactor.open_primary_relief_valve()
    reactor.tick()
    assert(reactor.primary_relief_valve)
    reactor.close_primary_relief_valve()
    reactor.tick()
    assert(reactor.primary_relief_valve == False)

def test_secondary_pump():
    reactor.set_secondary_pump_rpm(25)
    reactor.tick()
    assert(reactor.secondary_pump_rpm == 25)

def test_secondary_relief_valve():
    reactor.open_secondary_relief_valve()
    reactor.tick()
    assert(reactor.secondary_relief_valve)
    reactor.close_secondary_relief_valve()
    reactor.tick()
    assert(reactor.secondary_relief_valve == False)

def test_condenser_pump():
    reactor.set_condenser_pump_rpm(69)
    reactor.tick()
    assert(reactor.condenser_pump_rpm == 69)

def test_scram():
    reactor.scram()
    reactor.tick()
    assert(reactor.rod_position == 0)

# Rod position should never go out of range (0-100)
def test_rod_range():
    reactor.set_rod_position(0)
    reactor.tick()
    reactor.set_rod_position(101)
    for i in range(0,105):
        reactor.tick()
    assert(reactor.rod_position == 100)

# TODO: Temperatures should never go below ambient
# TODO: RPMs should always be positive
# TODO: Generator current should always be positive
