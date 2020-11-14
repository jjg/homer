class PWR:

    MIN_STEAM_GENERATOR_TEMP = 25
    MIN_TURBINE_PRESSURE = 10
    MIN_GENERATOR_RPM = 20

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
        generator_current = 0

    def tick(self):
        simulation_time++
        
        # Update rod position
        if self.rod_position < self.target_rod_position:
            self.rod_position++
        if self.rod_position > self.target_rod_position:
            self.rod_position--

        # TODO: Compute primary temp
        # TODO: Compute primary pressure
        # TODO: Compute secondary temp
        # TODO: Compute secondary pressure
        # TODO: Compute condenser temp
        # TODO: Compute turbine RPM
        # TODO: Compute generator current

    def set_rod_position(self, position):
        self.target_rod_position = position

    def set_primary_pump_rpm(self, rpm):
        self.primary_pump_rpm = rpm

    def open_primary_relief_valve(self):
        self.primary_relief_valve = True

    def close_primary_relief_valve(self):
        self.primary_relief_valve = False

    def set_secondary_pump_rpm(self,rpm):
        self.secondary_pump_rpm = rpm

    def open_secondary_relief_valve(self):
        self.secondary_relief_valve = True

    def close_secondary_reief_valve(self):
        self.secondary_relief_valve = False

    def set_condenser_pump_rpm(self, rpm):
        self.condenser_pump_rpm = rpm

    def scram(self):
        self.rod_position = 0
