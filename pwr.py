# Initialize 

# Base initial system temps off ambient temperature
# TODO: Read this from a sensor
AMBIENT_TEMP = 15.0
STEAM_GENERATOR_EFFICIENCY = 0.5
GENERATOR_EFFICIENCY = 0.75
MIN_STEAM_GENERATOR_TEMP = 25
MIN_TURBINE_PRESSURE = 10 
MIN_GENERATOR_RPM = 20

# Internal state variables
shutdown = False
simulation_time = 0

# Inputs
# TODO: Find a way to initialize RPMs to zero w/o causing divide by zero...
inputs = {
    "requested_rod_position": 1,
    "primary_pump_rpm": 1,
    "secondary_relief_valve": False,
}

# Outputs
outputs = { 
    "actual_rod_position": 1,
    "primary_temp": AMBIENT_TEMP,
    "secondary_pressure": 0.0,
    "turbine_rpm": 0,
    "generator_current": 0.0,
}


# Main loop
while not shutdown:

    # Display current status
    print("---------------------------------------------")
    print(f"Simulation time: {simulation_time}")
    for k,v in outputs.items():
        print(f"{k}\t\t{round(v,1)}")
    print("---------------------------------------------")

    # Get inputs
    for k,v in inputs.items():
        print(f"{k}\t{v}")
    param = input("What would you like to change? ")
    if param:
        inputs[param] = int(input("What would you like to change it to? "))
        # TODO: Test if requested value exceeds threshold

    if input("Ready to quit yet? ") == "yes":
        shutdown = True


    # Calculate changes
    # Each pass through this loop represents one second of simulation time
    simulation_time += 1

    # Rods can move one unit per second
    if outputs["actual_rod_position"] > inputs["requested_rod_position"]:
        outputs["actual_rod_position"] -= 1
    if outputs["actual_rod_position"] < inputs["requested_rod_position"]:
        outputs["actual_rod_position"] += 1

    # primary temp
    outputs["primary_temp"] = outputs["primary_temp"] + outputs["actual_rod_position"]
    # Subtract pump effect
    outputs["primary_temp"] = outputs["primary_temp"] - inputs["primary_pump_rpm"]
    # TODO: Subtract for fuel depletion
    # Never fall below ambient temp
    if outputs["primary_temp"] < AMBIENT_TEMP:
        outputs["primary_temp"] = AMBIENT_TEMP

    # secondary pressure
    # TODO: pressure should drop when primary temp drops
    if outputs["primary_temp"] > MIN_STEAM_GENERATOR_TEMP:
        outputs["secondary_pressure"] += (outputs["primary_temp"] * STEAM_GENERATOR_EFFICIENCY) / (100 - inputs["primary_pump_rpm"]) 

    # turbine rpm
    if outputs["secondary_pressure"] > MIN_TURBINE_PRESSURE:
        outputs["turbine_rpm"] = round(outputs["secondary_pressure"])
    else:
        outputs["turbine_rpm"] = 0

    # generator current
    outputs["generator_current"] = (outputs["turbine_rpm"] * GENERATOR_EFFICIENCY)
