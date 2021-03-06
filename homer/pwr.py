import logging

# Constants
# By default all parameters range between 0-100%,
# but some components only function within a 
# subset of this percentage range
STEAM_GENERATOR_EFFICIENCY = 0.5
GENERATOR_EFFICIENCY = 0.75
MIN_STEAM_GENERATOR_TEMP = 25
MIN_TURBINE_PRESSURE = 10
MIN_GENERATOR_RPM = 20

class PWR:

    def __init__(self, ambient_temp):
        self.ambient_temp = ambient_temp
        self.simulation_time = 0
        self.rod_position = 0
        self.target_rod_position = 0
        self.primary_pump_rpm = 0
        self.primary_relief_valve = False
        self.primary_temp = self.ambient_temp
        self.primary_pressure = 0
        self.secondary_pump_rpm = 0
        self.secondary_relief_valve = False
        self.secondary_temp = self.ambient_temp
        self.secondary_pressure = 0
        self.condenser_pump_rpm = 0
        self.condenser_temp = self.ambient_temp
        self.turbine_rpm = 0
        self.generator_current = 0
        self.scram_status = False

    def tick(self):
        self.simulation_time += 1
       
        # Update SCRAM status
        if self.target_rod_position == 0:
            self.scram_status = False

        # Update rod position
        # TODO: Don't let rods go out of range (0-100%)
        if self.rod_position < self.target_rod_position:
            self.rod_position += 1
        if self.rod_position > self.target_rod_position:
            self.rod_position -= 1
        # If the reactor is SCRAMed, force operator to manually reset
        # rods before resuming operation
        if self.scram_status:
            logging.error("Reactor is SCRAMed, reset rod position to 0!")
            self.rod_position = 0

        # Compute primary temp
        # TODO: Don't let temp go below ambient temp
        # TODO: Set alarm if temp exceeds 100%
        # TODO: Compensate for fuel depletion
        self.primary_temp = self.primary_temp + self.rod_position
        self.primary_temp = self.primary_temp - self.primary_pump_rpm

        # TODO: Compute primary pressure

        # TODO: Compute secondary temp

        # Compute secondary pressure
        # TODO: Set alarm if pressure exceeds 100%
        if self.primary_temp > MIN_STEAM_GENERATOR_TEMP:
            self.secondary_pressure += self.primary_temp * (STEAM_GENERATOR_EFFICIENCY) / (100 - self.primary_pump_rpm)
        else:
            self.secondary_pressure = 0

        # TODO: Compute condenser temp

        # Compute turbine RPM
        # TODO: Set alarm if RPM exceeds 100%
        if self.secondary_pressure > MIN_TURBINE_PRESSURE:
            self.turbine_rpm = round(self.secondary_pressure)
        else:
            self.turbine_rpm = 0

        # Compute generator current
        # TODO: Set alarm if current exceeds 100%
        if self.turbine_rpm > MIN_GENERATOR_RPM:
            self.generator_current = self.turbine_rpm * GENERATOR_EFFICIENCY

        # TODO: Set alarm if any parameter exceeds its threshold

    def set_rod_position(self, position):
        if position in range(0,100):
            self.target_rod_position = position
        else:
            return f"Rod position {position} is invalid, must be between 0 and 100"

    def set_primary_pump_rpm(self, rpm):
        if rpm in range(0,100):
            self.primary_pump_rpm = rpm

    def open_primary_relief_valve(self):
        self.primary_relief_valve = True

    def close_primary_relief_valve(self):
        self.primary_relief_valve = False

    def set_secondary_pump_rpm(self,rpm):
        if rpm in range(0,100):
            self.secondary_pump_rpm = rpm

    def open_secondary_relief_valve(self):
        self.secondary_relief_valve = True

    def close_secondary_relief_valve(self):
        self.secondary_relief_valve = False

    def set_condenser_pump_rpm(self, rpm):
        if rpm in range(0,100):
            self.condenser_pump_rpm = rpm

    def scram(self):
        self.scram_status = True
        self.rod_position = 0
