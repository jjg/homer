import pytest

import homer.pwr as pwr

def test_tick():
    reactor = pwr.PWR(55)
    reactor.tick()
    assert(reactor.simulation_time == 1)

def test_rod_position():
    reactor = pwr.PWR(55)
    reactor.set_rod_position(25)
    reactor.tick()
    assert(reactor.rod_position == 1)

def test_primary_pump():
    reactor = pwr.PWR(55)
    reactor.set_primary_pump_rpm(20)
    reactor.tick()
    assert(reactor.primary_pump_rpm == 20)

def test_primary_relief_valve():
    reactor = pwr.PWR(55)
    reactor.open_primary_relief_valve()
    reactor.tick()
    assert(reactor.primary_relief_valve)
    reactor.close_primary_relief_valve()
    reactor.tick()
    assert(reactor.primary_relief_valve == False)

def test_secondary_pump():
    reactor = pwr.PWR(55)
    reactor.set_secondary_pump_rpm(25)
    reactor.tick()
    assert(reactor.secondary_pump_rpm == 25)

def test_secondary_relief_valve():
    reactor = pwr.PWR(55)
    reactor.open_secondary_relief_valve()
    reactor.tick()
    assert(reactor.secondary_relief_valve)
    reactor.close_secondary_relief_valve()
    reactor.tick()
    assert(reactor.secondary_relief_valve == False)

def test_condenser_pump():
    reactor = pwr.PWR(55)
    reactor.set_condenser_pump_rpm(69)
    reactor.tick()
    assert(reactor.condenser_pump_rpm == 69)

def test_scram():
    reactor = pwr.PWR(55)
    reactor.scram()
    reactor.tick()
    assert(reactor.rod_position == 0)

# Rod position should never go out of range (0-100)
def test_rod_range():
    reactor = pwr.PWR(55)
    reactor.set_rod_position(101)
    for i in range(0,105):
        reactor.tick()
    assert(reactor.rod_position == 100)

# Temperatures should never go below ambient
def test_min_temp():
    ambient_temp = 55
    reactor = pwr.PWR(ambient_temp)
    reactor.tick()
    assert(reactor.primary_temp >= ambient_temp 
        and reactor.secondary_temp >= ambient_temp
        and reactor.condenser_temp >= ambient_temp
    )

# RPMs should always be positive
def test_min_rpm():
    reactor = pwr.PWR(55)
    reactor.set_rod_position(50)
    reactor.set_primary_pump_rpm(25)
    reactor.set_secondary_pump_rpm(10)
    while reactor.turbine_rpm < 10:
        reactor.tick()
    reactor.set_rod_position(0)
    reactor.set_primary_pump_rpm(-1)
    reactor.set_secondary_pump_rpm(-1)
    assert(reactor.primary_pump_rpm > -1
        and reactor.secondary_pump_rpm > -1
        and reactor.turbine_rpm > -1
    )

# TODO: Generator current should always be positive
