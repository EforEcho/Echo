import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QLabel, QMessageBox

class MainWindow(QMainWindow):
	def __init__(self) -> None:
		super().__init__()

		menu_bar = self.menuBar()

		file_menu = menu_bar.addMenu("&Datei")
		file_menu.addSeparator()
		help_menu = menu_bar.addMenu("&Hilfe")

		open_action = file_menu.addAction("\u00d6ffnen")
		save_as_action = file_menu.addAction("Speichern Als")
		close_action = file_menu.addAction("Beenden").triggered.connect(self.close)

		information_action = help_menu.addAction("Informationen")

	def closeEvent(self, event):
		msg_box = QMessageBox()
		msg_box.setWindowTitle("Paint")
		msg_box.setText("<b>Willst du das Programm wirklich schlie\u00dfen?</b>")
		msg_box.setInformativeText("Alle nicht gespeicherten \u00e4nderungen werden nicht gespeichert.")
		msg_box.setIcon(QMessageBox.Icon.Question)
	
		yes_button = msg_box.addButton("Ja", QMessageBox.ButtonRole.AcceptRole)
		no_button = msg_box.addButton("Nein", QMessageBox.ButtonRole.RejectRole)
	
		msg_box.setDefaultButton(no_button)
	
		msg_box.exec()
	
		if msg_box.clickedButton() == yes_button:
			event.accept()
		else:
			event.ignore()

def main() -> int:
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()
	app.exec()

	return 0

if __name__ == "__main__":
	sys.exit(main())