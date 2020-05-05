# CST 205 Final Project: Enuncreate
# By Diana Danvers, Syn Ng, Neva Yeh, Rodrigo Andrade Villafana
#
#

from gui import Window
from PyQt5.QtWidgets import QApplication
import sys

def main():
	app = QApplication(sys.argv)
	gui = Window()
	gui.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
