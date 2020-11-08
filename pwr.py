# Initialize 

# Base initial system temps off ambient temperature
# TODO: Read this from a sensor
AMBIENT_TEMP = 15.0

# Internal state variables
shutdown = False
simulation_time = 0

# Inputs
# TODO: Find a way to initialize RPMs to zero w/o causing divide by zero...
inputs = {
    "requested_rod_position": 1,
    "primary_pump_rpm": 1,
    "secondary_pump_rpm": 1,
    "condenser_pump_rpm": 1,
    "turbine_bypass": 0.0,
    "primary_relief_valve": False,
    "secondary_relief_valve": False,
}

# Outputs
outputs = { 
    "actual_rod_position": 1,
    "primary_temp": AMBIENT_TEMP,
    "primary_pressure": 0.0,
    "secondary_temp": AMBIENT_TEMP,
    "secondary_pressure": 0.0,
    "condenser_temp": AMBIENT_TEMP,
    "turbine_rpm": 0,
    "generator_current": 0.0,
}

# Thresholds
MAX_PRIMARY_TEMP = 100
MAX_SECONDARY_TEMP = 100
MAX_CONDENSER_TEMP = 100
MAX_PRIMARY_PRESSURE = 100
MAX_SECONDARY_PRESSURE = 100
MAX_PUMP_RPM = 100
MIN_TURBINE_PRESSURE = 50
MAX_TURBINE_PRESSURE = 100
MAX_TURBINE_RPM = 100
MIN_GENERATOR_RPM = 25
MAX_GENERATOR_RPM = 100
MAX_GENERATOR_CURRENT = 100


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
    outputs["primary_temp"] = (outputs["primary_temp"] + outputs["actual_rod_position"]) - .1
    if outputs["primary_temp"] < AMBIENT_TEMP:
        outputs["primary_temp"] = AMBIENT_TEMP

    # primary pressure
    outputs["primary_pressure"] = (outputs["primary_temp"] / inputs["primary_pump_rpm"])

    # secondary temp
    outputs["secondary_temp"] += (outputs["primary_temp"] / 2)
    if outputs["secondary_temp"] > outputs["primary_temp"]:
        outputs["secondary_temp"] = outputs["primary_temp"]
    if outputs["secondary_temp"] < AMBIENT_TEMP:
        outputs["secondary_temp"] = AMBIENT_TEMP

    # secondary pressure
    outputs["secondary_pressure"] = (outputs["primary_temp"] / inputs["secondary_pump_rpm"])

    # condenser temp
    outputs["condenser_temp"] = (outputs["secondary_temp"] / 2)

    # turbine rpm
    if outputs["secondary_pressure"] > MIN_TURBINE_PRESSURE:
        outputs["turbine_rpm"] = round(outputs["secondary_pressure"])
    else:
        outputs["turbine_rpm"] = 0

    # generator current
    outputs["generator_current"] = (outputs["turbine_rpm"] * .09)


