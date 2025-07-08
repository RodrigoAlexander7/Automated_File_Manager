import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFileDialog, QVBoxLayout, QWidget
)
from PySide6.QtCore import Qt 

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Path Selector")

        self.resize(500, 300) # Width: 500 pixels, Height: 300 pixels

        # main layout 
        main_layout = QVBoxLayout()

        # button select folder
        self.browse_button = QPushButton("Seleccionar Carpeta")
        self.browse_button.setObjectName("browseFolderButton") # Como en Designer
        main_layout.addWidget(self.browse_button)

        # show the route
        self.folder_path_line_edit = QLineEdit()
        self.folder_path_line_edit.setObjectName("folderPathLineEdit") 
        self.folder_path_line_edit.setPlaceholderText("path route")
        self.folder_path_line_edit.setReadOnly(True) 
        main_layout.addWidget(self.folder_path_line_edit)

        # Widget 
        container_widget = QWidget()
        container_widget.setLayout(main_layout)
        self.setCentralWidget(container_widget)

        # connect the button to the (slot)
        self.browse_button.clicked.connect(self.select_folder)

    def select_folder(self):
        # QFileDialog.getExistingDirectory(parent, caption, directory, options)
        # parent: main windows
        # caption: title
        # directory: initial directory to show 
        # options: aditional flags (ej. QFileDialog.ShowDirsOnly)

        selected_folder = QFileDialog.getExistingDirectory(
            self,
            "Select folder",
            self.folder_path_line_edit.text() if self.folder_path_line_edit.text() else "", 
            QFileDialog.Option.ShowDirsOnly # just select direcotories
        )

        if selected_folder:
            self.folder_path_line_edit.setText(selected_folder)
            print(f"Carpeta seleccionada: {selected_folder}")
        else:
            print("Selección de carpeta cancelada.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow() 
    window.show()
    sys.exit(app.exec())