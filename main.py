# IMPORT MODULES
import os
import sys
# IMPORT qt_core
from qt_core import *
# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Curso de Python e PySide6")

        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # EXIBI A NOSSA APLICAÇÃO
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
