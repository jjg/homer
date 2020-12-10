import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QDial, QPushButton, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.counter = 0
        
        self.setWindowTitle("Homer")
        
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
        main_layout.addWidget(primary_temp_widget, 0, 0)
        
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
        self.counter += 1
        self.primary_temp_gauge.setValue(self.counter)
        
    def primary_temp_value_changed(self, i):
        print(i)
        
    def primary_relief_valve_clicked(self, checked):
        print(checked)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
