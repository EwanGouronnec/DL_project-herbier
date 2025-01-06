from PySide6.QtWidgets import QDialog, QLineEdit, QPushButton, QLabel, QGridLayout
from PySide6.QtGui import QIcon

class SearchEngine(QDialog):
    def __init__(self):
        super().__init__()

        # Setup UI
        self.setWindowTitle("Dialog")
        self.setGeometry(0, 0, 632, 377)

        # Create widgets
        self.SearchEdit = QLineEdit(self)
        self.SearchEdit.setText("Enter your query here")

        self.SearchButton = QPushButton("Search", self)

        self.Information = QLineEdit(self)
        self.Information.setText("Search information")
        self.Information.setMinimumSize(150, 0)

        self.ZoomIn = QPushButton(self)
        self.ZoomIn.setIcon(QIcon("zoom+.png"))
        self.ZoomIn.setMinimumSize(75, 0)

        self.ZoomOut = QPushButton(self)
        self.ZoomOut.setIcon(QIcon("zoom-.png"))

        self.Image = QLabel(self)
        self.Image.setMinimumSize(200, 0)
        self.Image.setStyleSheet(
            "border: 2px solid black; border-radius: 10px;"
        )

        self.label = QLabel(self)
        self.label.setMinimumSize(250, 300)
        self.label.setStyleSheet(
            "border: 2px solid black; border-radius: 10px;"
        )

        # Set layout
        self.layout = QGridLayout(self)

        self.layout.addWidget(self.SearchEdit, 0, 0, 1, 2)
        self.layout.addWidget(self.SearchButton, 0, 2)
        self.layout.addWidget(self.Information, 2, 0)
        self.layout.addWidget(self.ZoomIn, 2, 1)
        self.layout.addWidget(self.ZoomOut, 2, 2)
        self.layout.addWidget(self.Image, 1, 0)
        self.layout.addWidget(self.label, 1, 1, 1, 2)
