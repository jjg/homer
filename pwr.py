# Initialize 

# Internal state variables
shutdown = False
simulation_time = 0

# Inputs
inputs = {
    "requested_rod_position": 0,
    "primary_pump_rpm": 0,
    "secondary_pump_rpm": 0,
    "condenser_pump_rpm": 0,
    "turbine_bypass": 0,
    "primary_relief_valve": False,
    "secondary_relief_valve": False,
}

# Outputs
outputs = { 
    "actual_rod_position": 0,
    "primary_temp": 0.0,
    "primary_pressure": 0.0,
    "secondary_temp": 0.0,
    "secondary_pressure": 0.0,
    "condenser_temp": 0.0,
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
MAX_TURBINE_RPM = 100
MAX_GENERATOR_CURRENT = 100


# Main loop
while not shutdown:

    # Calculate changes
    # Each pass through this loop represents one second of simulation time
    simulation_time += 1

    # Rods can move one unit per second
    if outputs["actual_rod_position"] >= inputs["requested_rod_position"]:
        outputs["actual_rod_position"] -= 1
    if outputs["actual_rod_position"] <= inputs["requested_rod_position"]:
        outputs["actual_rod_position"] += 1


    # Display current status
    print("---------------------------------------------")
    print(f"Simulation time: {simulation_time}")
    for k,v in outputs.items():
        print(f"{k}\t\t{v}")
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

