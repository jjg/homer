import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QDial, QPushButton, QLabel, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Homer")
        
        # Primary loop controls
        self.primary_temp_label = QLabel("Primary Coolant Temp")
        self.primary_temp_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.primary_temp_gauge = QDial()
        self.primary_temp_gauge.setRange(0,100)
        self.primary_temp_gauge.setSingleStep(1)
        self.primary_temp_gauge.setNotchesVisible(True)
        
        self.primary_relief_valve = QPushButton("vent primary")
        
        primary_temp_layout = QVBoxLayout()
        primary_temp_layout.addWidget(self.primary_temp_label)
        primary_temp_layout.addWidget(self.primary_temp_gauge)
        primary_temp_layout.addWidget(self.primary_relief_valve)
        
        primary_temp_widget = QWidget()
        primary_temp_widget.setLayout(primary_temp_layout)
        
        
        # Layout all the controls
        main_layout = QVBoxLayout()
        main_layout.addWidget(primary_temp_widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        
        self.setCentralWidget(main_widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
