from blessed import Terminal
from dashing import * 

import homer.pwr

term = Terminal()
reactor = homer.pwr.PWR(55)
reactor.tick()

if __name__ == "__main__":

    # Create gauges for rod target, rod position, primary temp, secondary temp
    # turbine RPM and generator current
    ui = VSplit(
            HSplit(
                VGauge(val=0, border_color=2, title="Rod Pos."),
                VGauge(val=0, border_color=2, title="Pri Temp"),
                VGauge(val=0, border_color=2, title="Sec Temp"),
                VGauge(val=0, border_color=2, title="Turbine RPM"),
                VGauge(val=0, border_color=2, title="Gen Curr")
            ),
            VSplit(
                HGauge(val=0, border_color=6, color=5, title="Rod Target Position"),
                HGauge(val=0, border_color=6, color=5, title="Primary Pump RPM")
                #Log(title="Rod Set Position", border_color=6, color=5),
                #Log(title="Primary Pump RPM", border_color=6, color=5)
            ),
            title="Homer"
         )
    rod_pos = ui.items[0].items[0]
    pri_temp = ui.items[0].items[1]
    sec_temp = ui.items[0].items[2]
    turbine_rpm = ui.items[0].items[3]
    gen_curr = ui.items[0].items[4]
    target_rod_pos = ui.items[1].items[0]
    pri_pump_rpm = ui.items[1].items[1]

    ui.display()

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
                target_rod_pos = reactor.target_rod_position
                pri_pump_rpm = reactor.primary_pump_rpm

                ui.display()

            elif val.is_sequence:
                print("got sequence: {0}.".format((str(val), val.name, val.code)))
            elif val: 
                if val == "r":
                    reactor.set_rod_position(reactor.target_rod_position - 1)
                if val == "R":
                    reactor.set_rod_position(reactor.target_rod_position + 1)
                if val == "p":
                    reactor.set_primary_pump_rpm(reactor.primary_pump_rpm - 1)
                if val == "P":
                    reactor.set_primary_pump_rpm(reactor.primary_pump_rpm + 1)
                if val == "s":
                    reactor.scram()
