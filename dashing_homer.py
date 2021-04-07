from blessed import Terminal
from dashing import * 

import homer.pwr

term = Terminal()
reactor = homer.pwr.PWR(55)

if __name__ == "__main__":

    # Create gauges for rod target, rod position, primary temp, secondary temp
    # turbine RPM and generator current
    ui = HSplit(
            HSplit(
                VGauge(val=0, border_color=2, title="Rod Pos."),
                VGauge(val=0, border_color=2, title="Pri Temp"),
                VGauge(val=0, border_color=2, title="Sec Temp"),
                VGauge(val=0, border_color=2, title="Turbine RPM"),
                VGauge(val=0, border_color=2, title="Gen Curr")
            ),
            title="Homer"
         )
    rod_pos = ui.items[0].items[0]
    pri_temp = ui.items[0].items[1]
    sec_temp = ui.items[0].items[2]
    turbine_rpm = ui.items[0].items[3]
    gen_curr = ui.items[0].items[4]

    ui.display()

    #print(f"{term.home}{term.clear}")
    #print("Reactor online.  Press 'q' to quit.")

    #print(f"----------------------------------")
    #print(f"Simulation time: {reactor.simulation_time}")
    #print(f"Rod position: {reactor.rod_position}")
    #print(f"Primary temp: {reactor.primary_temp}")
    #print(f"Secondary pressure: {reactor.secondary_pressure}")
    #print(f"Turbine RPM: {reactor.turbine_rpm}")
    #print(f"Generator current: {reactor.generator_current}")
    #print(f"----------------------------------")

    with term.cbreak():
        val = ""

        while val.lower() != "q":
            val = term.inkey(timeout=10)
            if not val:
                reactor.tick()

                # Update the UI
                rod_pos.value = reactor.rod_position
                pri_temp.value = reactor.primary_temp # = ui.items[0].items[1]
                sec_temp.value = reactor.secondary_pressure
                turbine_rpm.value = reactor.turbine_rpm
                gen_curr.value = reactor.generator_current

                ui.display()

                #print(f"{term.home}{term.clear}")
                #print(f"----------------------------------")
                #print(f"Simulation time: {reactor.simulation_time}")
                #print(f"Rod position: {reactor.rod_position}")
                #print(f"Primary temp: {reactor.primary_temp}")
                #print(f"Secondary pressure: {reactor.secondary_pressure}")
                #print(f"Turbine RPM: {reactor.turbine_rpm}")
                #print(f"Generator current: {reactor.generator_current}")
                #print(f"----------------------------------")

            elif val.is_sequence:
                print("got sequence: {0}.".format((str(val), val.name, val.code)))
            elif val: 
                if val == "r":
                    reactor.set_rod_position(int(input("\tposition> ")))
                if val == "p":
                    reactor.set_primary_pump_rpm(int(input("\trpm> ")))
                if val == "s":
                    reactor.scram()
