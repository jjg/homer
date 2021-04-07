from blessed import Terminal

import homer.pwr

term = Terminal()
reactor = homer.pwr.PWR(55)

print(f"{term.home}{term.clear}")
print("Reactor online.  Press 'q' to quit.")

print(f"----------------------------------")
print(f"Simulation time: {reactor.simulation_time}")
print(f"Rod position: {reactor.rod_position}")
print(f"Primary temp: {reactor.primary_temp}")
print(f"Secondary pressure: {reactor.secondary_pressure}")
print(f"Turbine RPM: {reactor.turbine_rpm}")
print(f"Generator current: {reactor.generator_current}")
print(f"----------------------------------")

with term.cbreak():
    val = ""

    while val.lower() != "q":
        val = term.inkey(timeout=10)
        if not val:
            reactor.tick()

            print(f"{term.home}{term.clear}")
            print(f"----------------------------------")
            print(f"Simulation time: {reactor.simulation_time}")
            print(f"Rod position: {reactor.rod_position}")
            print(f"Primary temp: {reactor.primary_temp}")
            print(f"Secondary pressure: {reactor.secondary_pressure}")
            print(f"Turbine RPM: {reactor.turbine_rpm}")
            print(f"Generator current: {reactor.generator_current}")
            print(f"----------------------------------")

        elif val.is_sequence:
            print("got sequence: {0}.".format((str(val), val.name, val.code)))
        elif val: 
            if val == "r":
                reactor.set_rod_position(int(input("\tposition> ")))
            if val == "p":
                reactor.set_primary_pump_rpm(int(input("\trpm> ")))
            if val == "s":
                reactor.scram()
