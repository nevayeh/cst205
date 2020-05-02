from PyQt5.QtWidgets import QApplication, QWidget, \
	QVBoxLayout, QHBoxLayout, \
	QTextEdit, QComboBox, QPushButton, QLabel, QMessageBox, QFrame
from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtGui import QPixmap, QIcon # not necessary (for now)
#from PIL import Image #not necessary (for now)
import sys
import voice_engine

class Window(QWidget):
	def __init__(self):
		super().__init__()
		# ------------------------------------
		#   GENERAL VARIABLE INITIALIZATION
		# ------------------------------------
		
		self.header_label_text = "Welcome!"
		self.instructions_label_text = "Enter text below:"
		self.options = ["Text To Speech", "Speech To Speech", "Text to Text", "Speech to Text"]
		
		# (TEMPORARY) Dev Panel variables		
		self.dev_title_label_text = "[TEMP] Developer Panel"
		self.dev_results_label_text = "Results:"
		
		# ------------------------------------
		#			 	HEADER
		# ------------------------------------
		
		self.header = QFrame()
		self.header_layout = QHBoxLayout()
		self.header.setLayout(self.header_layout)
		
		self.header_label = QLabel()
		self.header_label.setText(self.header_label_text)
		
		self.header_layout.addWidget(self.header_label)	
		
		
		# ------------------------------------
		#			   TEXTBOX
		# ------------------------------------

		self.textbox = QFrame()
		self.textbox_layout = QVBoxLayout()
		self.textbox.setLayout(self.textbox_layout)
		
		# Instructions (text can be changed above)
		self.instructions_label = QLabel()
		self.instructions_label.setText(self.instructions_label_text)
		
		self.text_area = QTextEdit()
		
		self.textbox_layout.addWidget(self.instructions_label)
		self.textbox_layout.addWidget(self.text_area)
		
		# ------------------------------------
		#			   BUTTONS
		# ------------------------------------

		self.buttons = QFrame()
		self.buttons_layout = QHBoxLayout()
		self.buttons.setLayout(self.buttons_layout)
		
		self.options_combo_box = QComboBox()
		for i in range(len(self.options)):
			self.options_combo_box.addItem(self.options[i])
		
		self.go_button = QPushButton("Go")
		self.go_button.clicked.connect(self.go)

		self.buttons_layout.addWidget(self.options_combo_box)
		self.buttons_layout.addWidget(self.go_button)

		# ------------------------------------
		#			RESULTS (placeholder)
		# ------------------------------------
		
		# Nothing here yet (results going into dev panel for now)
		
		# ------------------------------------
		#			  DEV TESTING
		# ------------------------------------
		
		self.dev = QFrame()
		self.dev_layout = QVBoxLayout()
		self.dev.setLayout(self.dev_layout)

		self.dev_title_label = QLabel()
		self.dev_title_label.setText(self.dev_title_label_text)
		
		self.dev_results_label = QLabel()
		self.dev_results_label.setText(self.dev_results_label_text)
		
		self.dev_results = QLabel() #where results go (for now)
		
		self.dev_clear_button = QPushButton("Clear Results")
		self.dev_clear_button.clicked.connect(self.dev_clear)
		
		self.dev_layout.addWidget(self.dev_title_label)
		self.dev_layout.addWidget(self.dev_results_label)
		self.dev_layout.addWidget(self.dev_results)
		self.dev_layout.addWidget(self.dev_clear_button)
		
		
		# ------------------------------------
		#	  PUTTING EVERYTHING TOGETHER
		# ------------------------------------
		
		self.container = QVBoxLayout()
		self.container.addWidget(self.header)		
		self.container.addWidget(self.textbox)
		self.container.addWidget(self.buttons)
		self.container.addWidget(self.dev)
		
		self.setLayout(self.container)
		self.setWindowTitle("Dyslexia Reader")
		#self.setWindowIcon(QIcon("<IMAGE FILE PATH>")) # Custom window icon (next to window title)

	@pyqtSlot()
	def go(self):
		self.go_button.setDisabled(True)
		#if text to speech is selected
		if self.options_combo_box.currentText() == self.options[0]:
			text = self.text_area.toPlainText()
			self.dev_results.setText(self.text_area.toPlainText())
			voice_engine.speak(text, "en")

		#if speech to text is selected
		elif self.options_combo_box.currentText() == self.options[3]:
			audio_to_text = voice_engine.get_audio()
			self.text_area.setText(audio_to_text)
			
		self.go_button.setDisabled(False)

	@pyqtSlot()
	def dev_clear(self):
		self.dev_results.setText("")

def main():
	app = QApplication(sys.argv)
	gui = Window()
	gui.show()
	sys.exit(app.exec_())
		
if __name__ == "__main__":
	main()

