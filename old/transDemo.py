# Diana Danvers 4/28/2020
# Demo program for language translation

from translate import transClass

def main():
	x = transClass()
	choice = '0'
	while choice == '0':
		print("\nWelcome to the Language Translator Beta!")
		print("Choose from the following:")
		print("1) Translate Text to English")
		print("2) Translate Text to a Chosen Language")
		print("3) See Available languages")
		print("4) Exit")

		choice = input("\nInput: ")
		if choice == "1":
			text = input("Enter text: ")
			x.transEN(text)
			x.report()
			choice = '0'
		elif choice == "2":
			text = input("Enter text: ")
			langCode = input("Enter a Language Code: ")
			x.transChoose(text, langCode)
			x.report()
			choice = '0'
		elif choice == "3":
			x.langCodesDisplay()
			print("")
			choice = '0'
		elif choice == "4":
			print("Goodbye!\n")
		else:
			print("ERROR")

main()
