from PyQt5.QtWidgets import QApplication, QWidget, \
	QVBoxLayout, QHBoxLayout, \
	QTextEdit, QComboBox, QPushButton, QLabel, QMessageBox, QFrame, QFileDialog, QScrollArea
from PyQt5.QtCore import pyqtSlot
import sys

from translate import transClass
from webcam import webcam
from imageToText import ITT
import os
import cv2



class Window(QWidget):
	def __init__(self):
		super().__init__()
	
		# ------------------------------------
		#   GENERAL VARIABLE INITIALIZATION
		# ------------------------------------
		
		self.header_label_text = "Welcome!"
		self.instructions_label_text = "Enter text below:"
		self.options = ["Text To Speech", "Speech To Speech", "Text to Text", "Speech to Text"]
		
		self.title_label_text = "[TEMP] Developer Panel"
		self.results_label_text = "Results:"
		
		self.img_intro_text = "Select An Image Option:"

		self.translator = transClass()
		self.langList = self.translator.langDict	

		self.img = ITT()

		self.path = os.getcwd()

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
		#			   IMAGES
		# ------------------------------------

		self.img_input = QFrame()
		self.img_layout = QHBoxLayout()
		self.img_input.setLayout(self.img_layout)

		self.img_intro = QLabel()
		self.img_intro.setText(self.img_intro_text)

		self.wc_button = QPushButton("Open WebCam")
		self.wc_button.clicked.connect(self.wc)

		self.cp_button = QPushButton("Choose Picture")
		self.cp_button.clicked.connect(self.cp)

		self.img_layout.addWidget(self.img_intro)
		self.img_layout.addWidget(self.wc_button)
		self.img_layout.addWidget(self.cp_button)
		
		# ------------------------------------
		#			   BUTTONS
		# ------------------------------------

		self.buttons = QFrame()
		self.buttons_layout = QHBoxLayout()
		self.buttons.setLayout(self.buttons_layout)
		
		self.options_combo_box = QComboBox()
		for i in range(len(self.options)):
			self.options_combo_box.addItem(self.options[i])
		
		self.options_language_box = QComboBox()
		self.options_language_box.setStyleSheet("QComboBox { combobox-popup: 0; }");
		for i in self.langList:
			self.options_language_box.addItem(self.langList[i].title())
		self.options_language_box.setCurrentIndex(list(self.langList.keys()).index("en"))
		
		self.go_button = QPushButton("Go")
		self.go_button.clicked.connect(self.go)

		self.buttons_layout.addWidget(self.options_combo_box)
		self.buttons_layout.addWidget(self.options_language_box)
		self.buttons_layout.addWidget(self.go_button)

		# ------------------------------------
		#			RESULTS 
		# ------------------------------------
		
		self.text_result = ""
		self.img_result = ""
		self.returnResults = ""

		# ------------------------------------
		#			DETAILS 
		# ------------------------------------

		self.details_button = QPushButton("Detailed Results")
		self.details_button.setCheckable(True)
		self.details_button.clicked.connect(self.displayDetails)
		
		self.details_label = QLabel()
		self.details_scroll = QScrollArea()
		self.details_scroll.setWidgetResizable(True)
		self.details_scroll.setWidget(self.details_label)
		
		self.details = QFrame()
		self.details_scroll_layout = QVBoxLayout()
		self.details.setLayout(self.details_scroll_layout)
		self.details_scroll_layout.addWidget(self.details_scroll)

		# ------------------------------------
		#			  Results
		# ------------------------------------
		
		self.results = QFrame()
		self.results_layout = QVBoxLayout()
		self.results.setLayout(self.results_layout)

		#self.title_label = QLabel()
		#self.title_label.setText(self.title_label_text)
		
		self.results_label = QLabel()
		self.results_label.setText(self.results_label_text)
		
		self.results_product = QLabel() #where results go (for now)
		
		self.clear_button = QPushButton("Clear Results")
		self.clear_button.clicked.connect(self.clear)

		#self.results_layout.addWidget(self.title_label)
		self.results_layout.addWidget(self.results_label)
		self.results_layout.addWidget(self.results_product)
		self.results_layout.addWidget(self.clear_button)
		self.results_layout.addWidget(self.details_button)

		
		# ------------------------------------
		#	  PUTTING EVERYTHING TOGETHER
		# ------------------------------------
		
		self.container = QVBoxLayout()
		self.container.addWidget(self.header)		
		self.container.addWidget(self.textbox)
		self.container.addWidget(self.img_input)
		self.container.addWidget(self.buttons)
		self.container.addWidget(self.results)
		self.container.addWidget(self.details)
		
		self.setLayout(self.container)
		self.setWindowTitle("Dyslexia Reader")
		#self.setWindowIcon(QIcon("<IMAGE FILE PATH>")) # Custom window icon (next to window title)


	# ------------------------------------
	#	  Helper Functions
	# ------------------------------------
	
	# Main translator function	
	def translate(self, text):
		self.langCode = self.translator.langCodes[self.options_language_box.currentText().lower()]
		if(self.langCode == "en"):
			self.translator.transEN(text)
		else:
			self.translator.transChoose(text, self.langCode)

	# Sometimes we can't get text from an image, let user know
	def parseError(self, image):
		if(image == ""):
			self.img_result = "Couldn't Parse Text"

	# ------------------------------------
	#	  Button Functions
	# ------------------------------------

	@pyqtSlot()
	def go(self):
		self.text_result = self.text_area.toPlainText()
		if(self.text_result != ""):
			self.translate(self.text_result)
			self.resultsText = self.translator.destText
		elif(self.img_result != ""):
			self.translate(self.img_result)
			self.resultsText = self.translator.destText
		else:
			self.resultsText = "No Text Entered!!!"

		self.results_product.setText(self.resultsText)

	# Clear all results
	@pyqtSlot()
	def clear(self):
		self.results_product.setText("")
		self.text_area.setText("")
		self.details_label.setText("")
		self.translateDetails = ""
		self.detailedResults = ""
		self.returnResults = ""
		self.img_result = ""
		self.text_result = ""
		self.details_button.setChecked(False)
		self.options_language_box.setCurrentIndex(list(self.langList.keys()).index("en"))
		cv2.destroyAllWindows()

	# Using webcam, takes temp picture, parses best it can, deletes temp pic
	@pyqtSlot()
	def wc(self):
		self.webcam = webcam()
		self.webcam.showWebcam()
		self.webcam.screenshot()
		
		self.img_result = self.img.imageToText(self.path + "/" + "temp.jpg", "eng")
		os.remove("temp.jpg")
		self.parseError(self.img_result)
	
	# User choose an image, opens window finder
	@pyqtSlot()
	def cp(self):
		self.dialog = QFileDialog()
		self.img_dir = self.dialog.getOpenFileName(self, "File", self.path, "Image files (*.jpg *.png)")[0]
		self.img_result = self.img.imageToText(self.img_dir, "eng")
		self.parseError(self.img_result)

	@pyqtSlot()
	def displayDetails(self):
		# Do we want to show details?
		if self.details_button.isChecked():
			if(self.text_result != ""):
				# Parsed text
				self.detailedResults = (
					"[Text Data]\n" +	
					"-Texbox: " + self.text_result + "\n\n"
				)
			elif(self.img_result != ""):
				# Parsed an image
				self.detailedResults = (
					"[Image Data] \n" +
					"-Source: " + self.img_dir + "\n" +
					"-Image Text: \n" + self.img_result + "\n\n"  
				)
			else:
				# Nothing yet
				self.detailedResults = ""

			# Get translator data
			if(self.detailedResults != ""):	
				self.translateDetails = (
					"[Translation Data] \n"
					"-Source Language: " + self.translator.srcLang + "\n" + 
					"-Source Text: " + self.translator.srcText + "\n" + 
					"-Source Pronunciation: " + self.translator.howToS + "\n\n" + 
					"-Destination Language: " + self.translator.destLang + "\n" + 
					"-Destination Text: " + self.translator.destText + "\n" + 
					"-Destination Pronunciation: " + self.translator.howToD + "\n\n"
				)
			else:
				self.translateDetails = ("")

			self.returnResults = self.detailedResults + self.translateDetails
			self.details_label.setText(self.returnResults)
			self.details_label.show()
		else:
			self.details_label.hide()

	
def main():
	app = QApplication(sys.argv)
	gui = Window()
	gui.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
