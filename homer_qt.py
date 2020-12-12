import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QDial, QPushButton, QLabel, QWidget, QSpinBox

import homer.pwr

reactor = homer.pwr.PWR(10)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
                
        self.setWindowTitle("Homer")
        
        # Fuel rods
        self.fuel_rod_label = QLabel("Fuel Rod Position")
        self.fuel_rod_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.fuel_rod_position_gauge = QDial()
        self.fuel_rod_position_gauge.setRange(0,100)
        self.fuel_rod_position_gauge.setSingleStep(1)
        self.fuel_rod_position_gauge.setNotchesVisible(True)
        
        self.fuel_rod_target_label = QLabel("Fuel Rod Position Target")
        self.fuel_rod_target_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.fuel_rod_position = QSpinBox()
        self.fuel_rod_position.setMinimum(0)
        self.fuel_rod_position.setMaximum(100)
        self.fuel_rod_position.setSingleStep(1)
        self.fuel_rod_position.valueChanged.connect(self.fuel_rod_position_changed)
        
        fuel_rod_layout = QVBoxLayout()
        fuel_rod_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        fuel_rod_layout.addWidget(self.fuel_rod_label)
        fuel_rod_layout.addWidget(self.fuel_rod_position_gauge)
        fuel_rod_layout.addWidget(self.fuel_rod_target_label)
        fuel_rod_layout.addWidget(self.fuel_rod_position)
        
        fuel_rod_widget = QWidget()
        fuel_rod_widget.setLayout(fuel_rod_layout)
        
        # Primary loop controls
        self.primary_temp_label = QLabel("Primary Coolant Temp")
        self.primary_temp_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.primary_temp_gauge = QDial()
        self.primary_temp_gauge.setRange(0,100)
        self.primary_temp_gauge.setSingleStep(1)
        self.primary_temp_gauge.setNotchesVisible(True)
        self.primary_temp_gauge.valueChanged.connect(self.primary_temp_value_changed)

        self.primary_pressure_label = QLabel("Primary Coolant Pressure")
        self.primary_pressure_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.primary_pressure_gauge = QDial()
        self.primary_pressure_gauge.setRange(0,100)
        self.primary_pressure_gauge.setSingleStep(1)
        self.primary_pressure_gauge.setNotchesVisible(True)
        
        self.primary_pump_rpm_label = QLabel("Primary Pump RPM")
        self.primary_pump_rpm_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.primary_pump_rpm = QSpinBox()
        self.primary_pump_rpm.setMinimum(0)
        self.primary_pump_rpm.setMaximum(100)
        self.primary_pump_rpm.setSingleStep(1)
        self.primary_pump_rpm.valueChanged.connect(self.primary_pump_rpm_changed)
        
        self.primary_relief_valve = QPushButton("vent primary")
        self.primary_relief_valve.setCheckable(True)
        self.primary_relief_valve.clicked.connect(self.primary_relief_valve_clicked)
        
        primary_loop_layout = QVBoxLayout()
        primary_loop_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        primary_loop_layout.addWidget(self.primary_temp_label)
        primary_loop_layout.addWidget(self.primary_temp_gauge)
        primary_loop_layout.addWidget(self.primary_pressure_label)
        primary_loop_layout.addWidget(self.primary_pressure_gauge)
        primary_loop_layout.addWidget(self.primary_pump_rpm_label)
        primary_loop_layout.addWidget(self.primary_pump_rpm)
        primary_loop_layout.addWidget(self.primary_relief_valve)
        
        primary_loop_widget = QWidget()
        primary_loop_widget.setLayout(primary_loop_layout)
        
        # Secondary loop controls
        self.secondary_temp_label = QLabel("Secondary Coolant Temp")
        self.secondary_temp_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.secondary_temp_gauge = QDial()
        self.secondary_temp_gauge.setRange(0,100)
        self.secondary_temp_gauge.setSingleStep(1)
        self.secondary_temp_gauge.setNotchesVisible(True)
        self.secondary_temp_gauge.valueChanged.connect(self.secondary_temp_value_changed)
        
        self.secondary_pressure_label = QLabel("Secondary Coolant Pressure")
        self.secondary_pressure_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.secondary_pressure_gauge = QDial()
        self.secondary_pressure_gauge.setRange(0,100)
        self.secondary_pressure_gauge.setSingleStep(1)
        self.secondary_pressure_gauge.setNotchesVisible(True)
        
        self.secondary_pump_rpm_label = QLabel("Secondary Pump RPM")
        self.secondary_pump_rpm_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.secondary_pump_rpm = QSpinBox()
        self.secondary_pump_rpm.setMinimum(0)
        self.secondary_pump_rpm.setMaximum(100)
        self.secondary_pump_rpm.setSingleStep(1)
        self.secondary_pump_rpm.valueChanged.connect(self.secondary_pump_rpm_changed)
        
        self.secondary_relief_valve = QPushButton("vent secondary")
        self.secondary_relief_valve.setCheckable(True)
        self.secondary_relief_valve.clicked.connect(self.secondary_relief_valve_clicked)
        
        secondary_loop_layout = QVBoxLayout()
        secondary_loop_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        secondary_loop_layout.addWidget(self.secondary_temp_label)
        secondary_loop_layout.addWidget(self.secondary_temp_gauge)
        secondary_loop_layout.addWidget(self.secondary_pressure_label)
        secondary_loop_layout.addWidget(self.secondary_pressure_gauge)
        secondary_loop_layout.addWidget(self.secondary_pump_rpm_label)
        secondary_loop_layout.addWidget(self.secondary_pump_rpm)
        secondary_loop_layout.addWidget(self.secondary_relief_valve)
        
        secondary_loop_widget = QWidget()
        secondary_loop_widget.setLayout(secondary_loop_layout)
        
        # Turbine/generator
        self.turbine_rpm_label = QLabel("Turbine RPM")
        self.turbine_rpm_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.turbine_rpm_gauge = QDial()
        self.turbine_rpm_gauge.setRange(0,100)
        self.turbine_rpm_gauge.setSingleStep(1)
        self.turbine_rpm_gauge.setNotchesVisible(True)
        
        self.generator_current_label = QLabel("Generator Current")
        self.generator_current_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.generator_current_gauge = QDial()
        self.generator_current_gauge.setRange(0,100)
        self.generator_current_gauge.setSingleStep(1)
        self.generator_current_gauge.setNotchesVisible(True)
        
        turbine_layout = QVBoxLayout()
        turbine_layout.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        turbine_layout.addWidget(self.turbine_rpm_label)
        turbine_layout.addWidget(self.turbine_rpm_gauge)
        turbine_layout.addWidget(self.generator_current_label)
        turbine_layout.addWidget(self.generator_current_gauge)
        
        turbine_layout_widget = QWidget()
        turbine_layout_widget.setLayout(turbine_layout)
        
        
        # Layout all the controls
        main_layout = QGridLayout()
        # Fuel rods
        main_layout.addWidget(fuel_rod_widget, 0,0)
        # Primary loop
        main_layout.addWidget(primary_loop_widget, 0, 1)
        # Secondary loop
        main_layout.addWidget(secondary_loop_widget,0,2)
        # TODO: Condenser
        # Turbine
        main_layout.addWidget(turbine_layout_widget,0,3)
        
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # timer
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()
        
    # Event handlers
    def recurring_timer(self):
        reactor.tick()
        self.fuel_rod_position_gauge.setValue(reactor.rod_position)
        self.primary_temp_gauge.setValue(reactor.primary_temp)
        self.primary_pressure_gauge.setValue(reactor.primary_pressure)
        self.secondary_temp_gauge.setValue(reactor.secondary_temp)
        self.secondary_pressure_gauge.setValue(reactor.secondary_pressure)
        self.turbine_rpm_gauge.setValue(reactor.turbine_rpm)
        self.generator_current_gauge.setValue(reactor.generator_current)
        
    def fuel_rod_position_changed(self, i):
        reactor.set_rod_position(i)
        
    def primary_temp_value_changed(self, i):
        print(i)
        
    def primary_relief_valve_clicked(self, checked):
        print(checked)
        if checked:
            reactor.open_primary_relief_valve()
        else:
            reactor.close_primary_relief_valve()
            
    def primary_pump_rpm_changed(self, i):
        reactor.set_primary_pump_rpm(i)
        
    def secondary_temp_value_changed(self, i):
        print(i)
        
    def secondary_relief_valve_clicked(self, checked):
        print(checked)
        if checked:
            reactor.open_secondary_relief_valve()
        else:
            reactor.close_secondary_relief_valve()
            
    def secondary_pump_rpm_changed(self, i):
        reactor.set_secondary_pump_rpm(i)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
