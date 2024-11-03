import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout
)


class ArrayReversalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        input_layout = QHBoxLayout()

        self.array_label = QLabel("Массив(через запятую)")
        self.array_input = QLineEdit()
        input_layout.addWidget(self.array_label)
        input_layout.addWidget(self.array_input)

        layout.addLayout(input_layout)
        self.setLayout(layout)

        self.setWindowTitle("Реверсивный массив")
        self.setGeometry(300, 300, 600, 400)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayReversalApp()
    window.show()
    sys.exit(app.exec_())
