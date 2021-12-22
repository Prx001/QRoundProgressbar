import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QPushButton, QCheckBox, QSpinBox, QColorDialog, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor

from QRoundProgressbar import RoundProgressbar


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(600, 400)
		self.setWindowTitle("Circular Progress Bar")
		self.progressbar = RoundProgressbar()
		self.progressbar.resize(120, 120)
		self.slider = QSlider(Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setValue(self.progressbar.get_value())
		self.slider.setToolTip("This slider sets the progress bar value")
		self.slider.valueChanged.connect(lambda: self.progressbar.set_value(self.slider.value()))
		self.thickness_spinbox = QSpinBox()
		self.thickness_spinbox.setValue(self.progressbar.thickness)
		self.thickness_spinbox.setToolTip("This number defines the progress bar thickness")
		self.thickness_spinbox.valueChanged.connect(lambda: self.progressbar.set_thickness(self.thickness_spinbox.value()))
		self.round_edge_checkbox = QCheckBox("Round edge")
		self.round_edge_checkbox.setToolTip("Leaving this option checked, will make the progress bar edges round")
		self.round_edge_checkbox.clicked.connect(lambda: self.progressbar.set_round_edge(True) if self.round_edge_checkbox.isChecked() else self.progressbar.set_round_edge(False))
		self.change_color_button = QPushButton("Change color")
		self.change_color_button.setToolTip("Select a color for the progress bar")
		self.change_color_button.clicked.connect(lambda: self.open_dialog(self.progressbar, 0))
		self.change_bg_circle_color_button = QPushButton("Change background circle color")
		self.change_bg_circle_color_button.setToolTip("Select a color for the progress bar background")
		self.change_bg_circle_color_button.clicked.connect(lambda: self.open_dialog(self.progressbar, 1))
		self.fill_bg_circle_checkbox = QCheckBox("Fill background circle center")
		self.fill_bg_circle_checkbox.setToolTip(
			"Leaving this option checked, will fill the background of the progress bar"
		)
		self.fill_bg_circle_checkbox.clicked.connect(lambda: self.progressbar.set_fill_bg_circle(True) if self.fill_bg_circle_checkbox.isChecked() else self.progressbar.set_fill_bg_circle(False))
		self.vertical_box = QVBoxLayout()
		self.vertical_box.addWidget(self.progressbar)
		self.vertical_box.addWidget(self.slider)
		self.vertical_box.addWidget(self.thickness_spinbox)
		self.vertical_box.addWidget(self.round_edge_checkbox)
		self.vertical_box.addWidget(self.change_color_button)
		self.vertical_box.addWidget(self.change_bg_circle_color_button)
		self.vertical_box.addWidget(self.fill_bg_circle_checkbox)
		self.main_horizontal_box = QHBoxLayout()
		self.main_horizontal_box.addLayout(self.vertical_box)
		self.setLayout(self.main_horizontal_box)
		self.show()

	def open_dialog(self, widget, color_index):
		color = QColorDialog.getColor(
			initial=widget._color if color_index == 0 else widget._bg_circle_color,
			options=QColorDialog.ShowAlphaChannel
		)
		if color.isValid():
			if color_index == 0:
				widget.set_color(color)
			elif color_index == 1:
				widget.set_bg_circle_color(color)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
