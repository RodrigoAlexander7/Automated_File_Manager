import app.pdf_reader as pdf_reader
import sys
from app.gui import MyMainWindow
import app.constant as constant 
import app.indexer as indexer 
from pathlib import Path

import app.file_manager as file_manager
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    

    app = QApplication(sys.argv)
    window = MyMainWindow() 
    window.show()
    sys.exit(app.exec())

