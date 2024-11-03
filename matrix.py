import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit,
    QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
)


class ArrayReversalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.process_button = None
        self.array_input = None
        self.array_label = None
        self.load_button = None
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

        self.process_button = QPushButton("Массив")
        self.process_button.clicked.connect(self.alg_matrix)
        layout.addWidget(self.process_button)

        self.load_button = QPushButton("Загрузить из файла")

def alg_matrix(self):
    try:
        array = list(map(int, self.array_input.text().split(',')))
        k = int(self.k_input.text()) - 1
        l = int(self.l_input.text()) - 1

        if not (0 <= k < l < len(array)):
            raise ValueError("K и L должны находиться в промежутке 1 ≤ K < L ≤ N")

        array[k:l + 1] = array[k:l + 1][::-1]
        self.output_text.setPlainText(f"{array}")

    except ValueError as e:
        QMessageBox.critical(self, "Ошибка", f"Неверный ввод: {e}")

def load_from_file(self):
    file_path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt)")
    if file_path:
        try:
            with open(file_path, 'r') as file:
                data = file.read().splitlines()
                if len(data) >= 3:
                    self.array_input.setText(data[0])
                    self.k_input.setText(data[1])
                    self.l_input.setText(data[2])
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArrayReversalApp()
    window.show()
    sys.exit(app.exec_())
