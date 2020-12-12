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
        self.fuel_rod_label = QLabel("Fuel Rod Control")
        self.fuel_rod_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.fuel_rod_position_gauge = QDial()
        self.fuel_rod_position_gauge.setRange(0,100)
        self.fuel_rod_position_gauge.setSingleStep(1)
        self.fuel_rod_position_gauge.setNotchesVisible(True)
        
        self.fuel_rod_position = QSpinBox()
        self.fuel_rod_position.setMinimum(0)
        self.fuel_rod_position.setMaximum(100)
        self.fuel_rod_position.setSingleStep(1)
        self.fuel_rod_position.valueChanged.connect(self.fuel_rod_position_changed)
        
        fuel_rod_layout = QVBoxLayout()
        fuel_rod_layout.addWidget(self.fuel_rod_label)
        fuel_rod_layout.addWidget(self.fuel_rod_position_gauge)
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
        
        self.primary_relief_valve = QPushButton("vent primary")
        self.primary_relief_valve.setCheckable(True)
        self.primary_relief_valve.clicked.connect(self.primary_relief_valve_clicked)
        
        primary_temp_layout = QVBoxLayout()
        primary_temp_layout.addWidget(self.primary_temp_label)
        primary_temp_layout.addWidget(self.primary_temp_gauge)
        primary_temp_layout.addWidget(self.primary_relief_valve)
        
        primary_temp_widget = QWidget()
        primary_temp_widget.setLayout(primary_temp_layout)
        
        
        # Layout all the controls
        main_layout = QGridLayout()
        # TODO: Fuel rods
        main_layout.addWidget(fuel_rod_widget, 0,0)
        # Primary loop
        main_layout.addWidget(primary_temp_widget, 0, 1)
        # TODO: Secondary loop
        # TODO: Condenser
        # TODO: Turbine
        
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
        #self.counter += 1
        #self.primary_temp_gauge.setValue(self.counter)
        
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
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
