from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon, QPixmap

from QRoundProgressbar import RoundProgressbar


class RoundProgressbarPlugin(QPyDesignerCustomWidgetPlugin):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.initialized = False

	def initialize(self, core):
		if self.initialized:
			return
		self.initialized = True

	def isInitialized(self):
		return self.initialized

	def createWidget(self, parent):
		return RoundProgressbar(parent=parent)

	def name(self):
		return "RoundProgressbar"

	def group(self):
		return "Display Widgets"

	def icon(self):
		return QIcon(_logo_pixmap)

	def toolTip(self):
		return "Round Progressbar"

	def whatsThis(self):
		return ""

	def isContainer(self):
		return False

	def domXml(self):
		return (
			'<widget class="RoundProgressbar" name="RoundProgressbar">\n'
			"</widget>\n"
		)

	def includeFile(self):
		return "QRoundProgressbar"


_logo_16x16_xpm = []
_logo_pixmap = QPixmap(_logo_16x16_xpm)
