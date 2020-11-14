import homer.pwr

reactor = homer.pwr.PWR(55)

quit = False

while not quit:

    reactor.tick()

    print(f"----------------------------------")
    print(f"Simulation time: {reactor.simulation_time}")
    print(f"Rod position: {reactor.rod_position}")
    print(f"Primary temp: {reactor.primary_temp}")
    print(f"Secondary pressure: {reactor.secondary_pressure}")
    print(f"Turbine RPM: {reactor.turbine_rpm}")
    print(f"Generator current: {reactor.generator_current}")
    print(f"----------------------------------")
    
    command = input("command > ")
    if command == "quit":
        quit = True
    else:
        if command == "rod_position":
            reactor.set_rod_position(int(input("\tposition> ")))
        if command == "primary_pump":
            reactor.set_primary_pump_rpm(int(input("\trpm> ")))
        if command == "scram":
            reactor.scram()
