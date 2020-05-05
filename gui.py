
# PqQt Widgets
from PyQt5.QtWidgets import QApplication, QWidget, \
	QVBoxLayout, QHBoxLayout, \
	QTextEdit, QComboBox, QPushButton, QLabel, QMessageBox, QFrame, QFileDialog, QScrollArea
from PyQt5.QtCore import pyqtSlot, Qt
# Important systems
import sys
import os
import cv2
# Our Classes <3
from translate import transClass
from webcam import webcam
from imageToText import ITT
from speechToText import STT

class Window(QWidget):
	def __init__(self):
		super().__init__()
	
		# ------------------------------------
		#   GENERAL VARIABLE INITIALIZATION
		# ------------------------------------
		
		self.header_label_text = "Welcome!"
		self.instructions_label_text = "Enter text below:"

		self.options_in = ["Text", "Speech", "Image"]
		self.options_out = ["Text", "Speech"]

		self.title_label_text = "[TEMP] Developer Panel"
		
		self.translator = transClass()
		self.langList = self.translator.langDict	

		self.img = ITT()
		self.speech = STT()

		self.path = os.getcwd()

		self.go_status = False
		self.critError = False

		# ------------------------------------
		#			 	HEADER
		# ------------------------------------
		
		self.header = QFrame()
		self.header_layout = QHBoxLayout()
		self.header.setLayout(self.header_layout)
		
		self.header_label = QLabel()
		self.header_label.setText(self.header_label_text)
		self.header_label.setAlignment(Qt.AlignCenter)
		
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
		self.img_intro.setText("Select An Image Option:")

		self.wc_button = QPushButton("Open WebCam")
		self.wc_button.clicked.connect(self.wc)

		self.cp_button = QPushButton("Choose Picture")
		self.cp_button.clicked.connect(self.cp)

		self.img_layout.addWidget(self.img_intro)
		self.img_layout.addWidget(self.wc_button)
		self.img_layout.addWidget(self.cp_button)

		# ------------------------------------
		#			   AUDIO
		# ------------------------------------

		self.audio = QFrame()
		self.audio_layout = QHBoxLayout()
		self.audio.setLayout(self.audio_layout)

		self.audio_intro = QLabel()
		self.audio_intro.setText("Select An Audio Option:")

		self.mr_button = QPushButton("Make Recording")
		self.mr_button.clicked.connect(self.mr_S)

		self.open_mp3_button = QPushButton("Open MP3")
		self.open_mp3_button.clicked.connect(self.get_mp3)

		self.audio_layout.addWidget(self.audio_intro)
		self.audio_layout.addWidget(self.mr_button)
		self.audio_layout.addWidget(self.open_mp3_button)
		
		# ------------------------------------
		#			   OPTIONS
		# ------------------------------------

		self.options = QFrame()
		self.options_layout = QHBoxLayout()
		self.options.setLayout(self.options_layout)
		
		self.options.src_label = QLabel()
		self.options.src_label.setText("Source: ")
		self.options_in_combo_box = QComboBox()
		for i in range(len(self.options_in)):
			self.options_in_combo_box.addItem(self.options_in[i])

		self.options.dst_label = QLabel()
		self.options.dst_label.setText("Destination: ")
		self.options_out_combo_box = QComboBox()
		for i in range(len(self.options_out)):
			self.options_out_combo_box.addItem(self.options_out[i])
		
		self.options.lang = QLabel()
		self.options.lang.setText("Language: ")
		self.options_language_box = QComboBox()
		self.options_language_box.setStyleSheet("QComboBox { combobox-popup: 0; }");
		for i in self.langList:
			self.options_language_box.addItem(self.langList[i].title())
		self.options_language_box.setCurrentIndex(list(self.langList.keys()).index("en"))

		self.options_layout.addWidget(self.options.src_label)
		self.options_layout.addWidget(self.options_in_combo_box)
		self.options_layout.addWidget(self.options.dst_label)
		self.options_layout.addWidget(self.options_out_combo_box)
		self.options_layout.addWidget(self.options.lang)
		self.options_layout.addWidget(self.options_language_box)

		# ------------------------------------
		#			GO 
		# ------------------------------------
		
		self.go = QFrame()
		self.go_layout = QHBoxLayout()
		self.go.setLayout(self.go_layout)

		self.go_button = QPushButton("Go ! ! !")
		self.go_button.clicked.connect(self.goEXE)
		self.go_layout.addWidget(self.go_button)

		# ------------------------------------
		#			RESULTS 
		# ------------------------------------
		
		self.text_result = ""
		self.img_result = ""
		self.audio_result = ""
		self.mp3_dir = ""
		self.img_dir = ""
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
		#			  RESULTS
		# ------------------------------------
		
		self.results = QFrame()
		self.results_layout = QVBoxLayout()
		self.results.setLayout(self.results_layout)

		#self.title_label = QLabel()
		#self.title_label.setText(self.title_label_text)
		
		self.results_label = QLabel()
		self.results_label.setText("Results:")
		
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
		self.container.addWidget(self.audio)
		self.container.addWidget(self.options)	
		self.container.addWidget(self.go)
		self.container.addWidget(self.results)
		self.container.addWidget(self.details)
		
		self.setLayout(self.container)
		self.setWindowTitle("Enuncreate")

	# ------------------------------------
	#	  HELPER FUNCTIONS
	# ------------------------------------
	
	# Main translator function	
	def translate(self, text):
		self.langCode = self.translator.langCodes[self.options_language_box.currentText().lower()]
		if(self.langCode == "en"):
			self.translator.transEN(text)
		else:
			self.translator.transChoose(text, self.langCode)

	# Overall error handler + 
	# Sometimes we can't get text from a source, let user know
	def parseError(self, source, stype):
		error = "[Error]=>"
		if(source == "" and (stype == "t" or stype == "te")):
			text_response = "No Text Inputted"
			if(stype == "te"):
				text_response = error + text_response
				self.critError = True
			self.text_result = 	text_response
		if(source == "" and (stype == "i" or stype == "ie")):
			img_response = "Couldn't Parse Text from Image"
			if(stype == "ie"):
				img_response = error + img_response 
				self.critError = True
			self.img_result = img_response
		if(source == "" and (stype == "a" or stype == "ae")):
			audio_response = "Couldn't Parse Text from Audio"
			if(stype == "ae"):
				audio_response = error + audio_response 
				self.critError = True
			self.audio_result = audio_response
		
	# ------------------------------------
	#	  BUTTON FUNCTIONS
	# ------------------------------------

	@pyqtSlot()
	def get_mp3(self):
		self.dialog = QFileDialog()
		self.mp3_dir = self.dialog.getOpenFileName(self, "File", self.path, "Image files (*.mp3)")[0]
		self.options_in_combo_box.setCurrentIndex(1)

	@pyqtSlot()
	def mr_S(self):
		self.audio_result = self.speech.stt()
		self.mp3_dir = self.path
		self.parseError(self.audio_result, "a")
		self.options_in_combo_box.setCurrentIndex(1)

	# Using webcam, takes temp picture, parses best it can, deletes temp pic
	def wc(self):
		self.webcam = webcam()
		self.webcam.showWebcam()
		self.webcam.screenshot()
		
		# Temp picture made in local directory TODO: FIX HARDCODED LANGUAGE
		self.img_dir = self.path + "/" + "temp.jpg"
		self.img_result = self.img.imageToText(self.img_dir, "eng")
		self.parseError(self.img_result, "i")
		os.remove("temp.jpg")
		self.options_in_combo_box.setCurrentIndex(2)

	# User choose an image, opens window finder
	@pyqtSlot()
	def cp(self):
		self.dialog = QFileDialog()
		self.img_dir = self.dialog.getOpenFileName(self, "File", self.path, "Image files (*.jpg *.png *.jpeg)")[0]

		# Chosen picture is parsed TODO: FIX HARDCODED LANGUAGE
		self.img_result = self.img.imageToText(self.img_dir, "eng")
		self.parseError(self.img_result, "i")
		self.options_in_combo_box.setCurrentIndex(2)

	
	@pyqtSlot()
	def goEXE(self):

		# Text conversion
		self.text_result = self.text_area.toPlainText()

		# Inputs
		# Text Input
		if(self.options_in_combo_box.currentText() == self.options_in[0]):
			if(self.text_result == ""):
				self.parseError(self.text_result, "te")
			elif (self.text_result != "") :
				self.translate(self.text_result)

		# Audio Input
		elif(self.options_in_combo_box.currentText() == self.options_in[1]):
			if(self.audio_result == ""):
				self.parseError(self.audio_result, "ae")
			elif (self.audio_result != "") :
				self.translate(self.audio_result)

		# Image Input
		elif(self.options_in_combo_box.currentText() == self.options_in[2]):
			if(self.img_result == ""):
				self.parseError(self.img_result, "ie")
			elif (self.img_result != "") :
				self.translate(self.img_result)
	
		# Translation done on every call: if empty -> Something is wrong
		if(self.translator == None):
			self.resultsText = "Critical Error in Translation"
			self.critError = True
		else:
			self.resultsText = self.translator.destText

		# Outputs
		# Text Output
		if(self.options_out_combo_box.currentText() == self.options_out[0] and not self.critError):
			self.speech.stt()

		# Audio Output
		elif(self.options_out_combo_box.currentText() == self.options_out[1] and not self.critError):
			self.speech.tts(self.resultsText, "en")
			self.mp3_dir = "From Source"
			self.audio_result = "From Source"
		
		self.go_status = True
		self.results_product.setText(self.resultsText)

	# Clear all results
	@pyqtSlot()
	def clear(self):
		# Clear widgets
		self.results_product.setText("")
		self.text_area.setText("")
		self.details_label.setText("")

		#Reset widgets
		self.options_in_combo_box.setCurrentIndex(0)
		self.options_out_combo_box.setCurrentIndex(0)
		self.options_language_box.setCurrentIndex(list(self.langList.keys()).index("en"))
		self.details_button.setChecked(False)
		cv2.destroyAllWindows()

		# Clear results
		self.img_result = ""
		self.text_result = ""
		self.audio_result = ""

		# Clear Details
		self.returnResults = ""

		# Clear directories
		self.mp3_dir = ""
		self.img_dir = ""

		# Clear flags
		self.go_status = False
		self.critError = False

	# Detail Window	
	@pyqtSlot()
	def displayDetails(self):
		# Do we want to show details?
		if self.details_button.isChecked():
			if(self.go_status):
				self.textDetails = (
					"[Text Data]\n" +	
					"-Textbox: " + self.text_result + "\n\n"
				)
				self.imageDetails = (
					"[Image Data] \n" +
					"-Source: " + self.img_dir + "\n" +
					"-Image Text: \n" + self.img_result + "\n\n"  
				)
				self.audioDetails = (
					"[Audio Data] \n" +
					"-Source: " + self.mp3_dir + "\n" +
					"-Audio Text: " + self.audio_result + "\n\n"  
				)
				# Get translator data
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
				# Nothing yet
				self.textDetails = self.imageDetails = self.audioDetails = self.translateDetails = ""

			self.returnResults = self.textDetails + self.imageDetails + self.audioDetails + self.translateDetails
			self.details_label.setText(self.returnResults)
			self.details_label.show()
		else:
			self.details_label.hide()

