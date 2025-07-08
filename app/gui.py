import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLineEdit, QFileDialog, QVBoxLayout, QWidget
)
from PySide6.QtCore import Qt 

from . import file_manager
from . import utils
from . import constant 

from pathlib import Path

class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Path Selector")

        self.resize(500, 300) # Width: 500 pixels, Height: 300 pixels

        # main layout 
        main_layout = QVBoxLayout()

        # button select folder
        self.browse_button = QPushButton("Select folder")
        self.browse_button.setObjectName("browseFolderButton") # Como en Designer
        main_layout.addWidget(self.browse_button)

        # show the route
        self.folder_path_line_edit = QLineEdit()
        self.folder_path_line_edit.setObjectName("folderPathLineEdit") 
        self.folder_path_line_edit.setPlaceholderText("path route")
        self.folder_path_line_edit.setReadOnly(True) 
        main_layout.addWidget(self.folder_path_line_edit)


        # button run app
        self.runButton = QPushButton("Organize")
        self.runButton.setObjectName("runButton") 
        main_layout.addWidget(self.runButton)

        # show the route
        self.statusLabel = QLineEdit()
        self.statusLabel.setObjectName("statusLabel") 
        self.statusLabel.setReadOnly(True) 
        main_layout.addWidget(self.statusLabel)

        # Widget 
        container_widget = QWidget()
        container_widget.setLayout(main_layout)
        self.setCentralWidget(container_widget)

        # connect the button to the (slot)
        self.browse_button.clicked.connect(self.select_folder)
        self.runButton.clicked.connect(self.run_function) 
        
    def run_function(self):
        file_manager.group_by_type(constant.PATH_DIRECTORY)
        pdf_route = Path(constant.PATH_DIRECTORY) / "WFM_Organized/pdf_files"
        utils.create_from_route(pdf_route)
        self.statusLabel.setText("SUCCES BRO 😎")
        print("Succes!!!!")


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
            constant.PATH_DIRECTORY = selected_folder
            print(f"Selected!!: {constant.PATH_DIRECTORY}")
        else:
            print("Selection Aborted")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow() 
    window.show()
    sys.exit(app.exec())